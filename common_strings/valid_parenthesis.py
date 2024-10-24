# Valid Parenthesis
# we're gonna use a stack for this one, chief
def valid_parenthesis(s):
    stack = []

    close_to_open = { ")" : "(", "}" : "{", "]" : "[" }

    for c in s:
        if c in close_to_open:
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False

if __name__ == "__main__":
    print(valid_parenthesis("()[]{}"))
    print(valid_parenthesis("(]"))
    print(valid_parenthesis("([])"))