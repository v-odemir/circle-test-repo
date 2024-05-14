print("test")

#feature/pr2-merge-to-development-1

def _check_indentation(self, tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.body and not isinstance(node.body[0], ast.Expr):
                self.feedback.append(
                    f"Function '{node.name}' should have a docstring or 'pass' statement.")
        elif isinstance(node, (ast.For, ast.While, ast.If, ast.With)):
            if not isinstance(node.body[0], ast.Expr):
                self.feedback.append(
                    f"Indentation Error: Missing 'pass' statement for '{ast.dump(node)}'.")