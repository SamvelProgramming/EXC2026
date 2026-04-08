def breckets(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for i in text:
        if i in ['(', '[', '{']:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if stack[-1] == pairs[i]:
                stack.pop()
            else:
                return False
    
    return len(stack) == 0

text = "[()]"
print(breckets(text))
text = "[(])"
print(breckets(text))
text = "["
print(breckets(text))
text = "[]"
print(breckets(text))