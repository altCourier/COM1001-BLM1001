def gluecommon(a,b):
    stack = ""
    i = 0
    for j in a:
        if j != b[i]:
            stack = stack + j
        else:
            i += 1
            stack = stack + j

    for k in range(i, len(b)):
        stack += b[k]
    
    return stack

print(gluecommon("ankara", "rakam"))
