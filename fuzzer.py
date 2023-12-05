from concurrent.futures import ThreadPoolExecutor
import argparse
import os, subprocess, platform
import json
import time
import queue
import random

import mutations
from utils import *

import feedback as fb

FILE_COPIES = []
FILE_PATHS = []
INPUTS = set()

INPUT_DIR = 'inputs/'
TEST_DIR = 'tests/'
CWD = os.getcwd()

n_fails = 0

available_files = queue.Queue()

feedback = None

def run_command_windows(file, input):
    try:
        # Get basename for files
        base, _ = os.path.splitext(os.path.basename(file))
        data_file = base + '.coverage'
        report_file = base + '.json'

        # Run test with branch coverage, and write coverage data to data_file
        result = subprocess.run(['coverage', 'run', '--branch', '--data-file', data_file, file, input], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        # Get report in json format and write it to report_file
        cov = subprocess.run(['coverage', 'json', '--pretty', '--data-file', data_file, '-o', report_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        # Call mutation function
        with open(report_file) as report:
            coverage_data = json.load(report)
            mutator(result.returncode, coverage_data, input)
            available_files.put(file)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{file}':\n{e.stderr}")

def run_command(file, input):
    try:
        # Get basename for files
        base, _ = os.path.splitext(os.path.basename(file))
        data_file = os.path.join(CWD, base + ".coverage")
        report_file = os.path.join(CWD, base + ".json")

        # Run test with branch coverage, and write coverage data to data_file
        result = subprocess.run([f'coverage run --branch --data-file "{data_file}" "{file}" "{input}"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        # Get report in json format and write it to report_file
        cov = subprocess.run([f'coverage json --pretty --data-file "{data_file}" -o "{report_file}"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        # Call mutation function
        with open(report_file) as report:
            coverage_data = json.load(report)
            mutator(result.returncode, coverage_data, input)

        available_files.put(file)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{file}':\n{e.stderr}")

def mutator(return_code, coverage_data, input):
    global n_fails
    global feedback
    global INPUTS
    
    #get coverage data for the test file
    cov = [c for c in coverage_data["files"].values()]
        
    # Update count of failed tests, get feedback and update inputs
    if return_code != 0:
        n_fails += 1
        feedback.update(cov[0])
        INPUTS.add(input)
    elif feedback.get_feedback(cov[0]):
        INPUTS.add(input)
    
        
def get_next_input():
    # TODO: Select next input to run test on
    return random.choice(list(INPUTS))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", help="Target for fuzzer", required=True)
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers")
    parser.add_argument("--timeout", type=int, default=5, help="Duration of fuzzing")
    args = parser.parse_args()

    global feedback
    feedback = fb.fuzzerFeedback()
    
    # Create temporary copies so we can parallelize the execution
    # Copies needed because only one worker can execute the same test file at a time
    for _ in range(args.workers):
        temp = TemporaryCopy(f"{TEST_DIR}{args.test}")
        FILE_COPIES.append(temp)
        FILE_PATHS.append(temp.__enter__())

    print(f"Fuzzing '{(args.test)}' in parallel with {args.workers} workers.")

    # Read starting inputs from directory
    for input in read_inputs(INPUT_DIR):
        INPUTS.add(input)

    # Populate the available files queue
    for file in FILE_PATHS:
        available_files.put(file)

    futures = []
    START_TIME = time.time()

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        while time.time() - START_TIME < args.timeout:
            # Gets next available file or blocks until a new one is enqueued
            cur_file = available_files.get(block=True)

            # Get next input
            next_input = get_next_input()

            # Mutate input
            print('Mutating..')
            next_input = mutations.select_mutation_function()(next_input)
            print('Done mutating..')

            # Submit each command to the ThreadPoolExecutor
            if platform.system() == 'Windows':
                futures.append(executor.submit(run_command_windows, cur_file, next_input))
            else:
                futures.append(executor.submit(run_command, cur_file, next_input))

        # Wait for all remaining to complete
        for future in futures:
            future.result()

    # Close all file copies
    for file in FILE_COPIES:
        file.__exit__(None, None, None)

    # Delete data files and reports
    cleanup(available_files)
    print("Final Inputs: ", INPUTS)
    print("Feedback: ", 
          "\n  lines covered: ", feedback.lines, 
          "\n  branches covered: ", feedback.branches, 
          "\n  highest coverage: ", feedback.percentage ,"%")
    print(f'Found {n_fails} fails')

if __name__ == "__main__":
    main()