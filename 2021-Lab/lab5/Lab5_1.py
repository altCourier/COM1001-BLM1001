s = "orta dogu teknik universitesi"

def abbrev(s:str) -> str:
    substr = s[0]
    for i, char in enumerate(s):
        if char.isalnum() and s[i-1] == " ":
            substr += char

    return substr

print(abbrev(s))
