def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')


def greet(name):
    print("Hello", name)

# pass argument
greet("John")


#feature/pr1-merge-to-development-1

def analyze_python_code(self, code):
    try:
        # Parse the Python code into an Abstract Syntax Tree (AST)
        tree = ast.parse(code)
    except SyntaxError as e:
        self.feedback.append(f"Syntax Error: {e}")
        return

    # Check for indentation errors and undefined variables
    self._check_indentation(tree)
    self._check_undefined_vars(tree)

    # Check code style using pycodestyle
    self._check_code_style(code)

    # Check code comments
    self._check_comments(code)


    print("ISSUE-4")
