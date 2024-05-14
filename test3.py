print("test")

def _check_undefined_vars(self, tree):
    undefined_vars = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            undefined_vars.discard(node.id)
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            undefined_vars.add(node.id)

    for var in undefined_vars:
        self.feedback.append(f"Variable '{var}' is used but not defined.")
#feature/pr2-merge-to-development-1

def _check_indentation_test(self, tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.body and not isinstance(node.body[0], ast.Expr):
                self.feedback.append(
                    f"Function '{node.name}' should have a docstring or 'pass' statement.")
        elif isinstance(node, (ast.For, ast.While, ast.If, ast.With)):
            if not isinstance(node.body[0], ast.Expr):
                self.feedback.append(
                    f"Indentation Error: Missing 'pass' statement for '{ast.dump(node)}'.")

