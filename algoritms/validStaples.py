def scobki(s):
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []
    for i in s:
        if i in "([{":
            stack.append(i)
        elif not stack or stack[-1] != pairs[i]:
            return False
        else:
            stack.pop()

    return len(stack) == 0

s = "(][{}])"
print(scobki(s))
