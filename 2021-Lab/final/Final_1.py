s = "3[a]2[bc]"

stack = []
def decoder(s:str) -> str:
    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s)
        
        else:
            substr = ""
            while stack[-1] != "[":
                substr = stack.pop() + substr
            stack.pop() # Popping the [

            num = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k

            stack.append(int(k) * substr)

    return "".join(stack)