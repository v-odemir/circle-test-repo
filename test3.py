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