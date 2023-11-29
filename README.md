# cis5470-final-project
CIS 5470 Software Analysis Final Project

### Usage
To use the fuzzer, call it from the root directory as
`python .\fuzzer.py --test <TEST_FILE> --workers <NUM_WORKERS> --timeout <DURATION>`

where `<TEST_FILE>` is a file in the _tests_ directory, `<NUM_WORKERS>` is the number
of parallel threads to execute tests (default 1), and `<DURATION>` is the timeout
duration in seconds for the fuzzer (default 5).

For example: `python .\fuzzer.py --test test0.py --workers 3 --timeout 5`