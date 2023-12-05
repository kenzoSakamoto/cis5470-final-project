class fuzzerFeedback():
    def __init__(self):
        self.branches = set()
        self.percentage = 0
        self.lines = set()
        
    def update(self, coverage):
        """updates coverage if new lines explore, new branches explore, or coverage percentage increased

        Args:
            coverage (dict): coverage data
        """
        for line in coverage["executed_lines"]:
            self.lines.add(line)
        for branch in coverage["executed_branches"]:
            self.branches.add(tuple(branch))
        if coverage["summary"]["percent_covered"] > self.percentage:
            self.percentage = coverage["summary"]["percent_covered"]
        
    def get_feedback(self, coverage):
        """checks whether coverage increased and updates

        Args:
            coverage (dict): coverage data

        Returns:
           bool: whether coverage increased in terms of lines, branches, or percentage
        """
        self.update(coverage)
        summary = coverage["summary"]
        
        if summary["percent_covered"] > self.percentage:
            return True
        
        for line in coverage["executed_lines"]:
            if line not in self.lines:
                return True
        
        for branch in coverage["executed_branches"]:
            if tuple(branch) not in self.branches:
                return True

        return False
    
    
        

        