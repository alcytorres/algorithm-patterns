# '' and '.' → ignored
# '..' → pop the last directory
# Anything else → add to stack

def simplifyPath(path):
    stack = []

    for part in path.split('/'):
        if part == '' or part == '.':
            continue
        if part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    # print(stack)
    # return '/' + '/'.join(stack)


# path = "/a/b///c/.././d/../f/"
# print(simplifyPath(path))  # /a/b/f


['', 'a', 'b', '', '', 'c', '..', '.', 'd', '..', 'f', '']


['a', 'b', 'f']
# / 
# /a/b/f









