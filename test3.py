print("test")

def _check_comments(self, code):
    lines = code.split('\n')
    for i, line in enumerate(lines):
        if line.strip().startswith('#'):
            # Check for empty comments or comments without space after '#'
            if len(line.strip()) == 1 or line.strip()[1] != ' ':
                self.feedback.append(
                    f"Improve comment style in line {i + 1}: '{line.strip()}'")