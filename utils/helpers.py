"""Some helper functions for editing text."""

import ast


def strip_comments(lines, comment_str="%"):
    new_text = []
    for line in lines:
        if line.startswith(comment_str):
            continue
        else:
            new_text.append(line)
    return new_text


def add_new_line_sep(lines):
    return [line + "\n" for line in lines]


def remove_function_docstrings(text):
    parsed = ast.parse(text)

    for node in ast.walk(parsed):
        # let's work only on functions & classes definitions
        if not isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            continue

        if not len(node.body):
            continue

        if not isinstance(node.body[0], ast.Expr):
            continue

        if not hasattr(node.body[0], 'value') or not isinstance(node.body[0].value, ast.Str):
            continue

        # Uncomment lines below if you want print what and where we are removing
        # print(node)
        # print(node.body[0].value.s)

        node.body = node.body[1:]
        
    return ast.unparse(parsed)