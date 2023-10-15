import logging, sys

with open(sys.argv[1]) as filewrapper:
    argcode = filewrapper.read()

def closestIndex(string: str, search: str, userIndex: int) -> int: # how the fuck does this work?
    indexes = [
        pos for pos, char in enumerate(string)
        if char == search and pos > userIndex
    ]
    if not indexes:
        return None
    return min(indexes, key=lambda x: abs(x - userIndex)) # what

def runcode(code: str):
    debug = False
    byteIndex = 0 # current byte
    bytes = [0] * 1000000 # the cell array
    loop = ""
    loopPos = 0 # index of the loop's starting position
    comment = False
    skips = [] # chars to skip
    imports = [] # imports to print if in debug
    for index, char in enumerate(code):
        selectedByte = bytes[byteIndex]
        if comment:
            if char == "#": comment = False
        else:
            if index in skips: pass
            elif char == "+": bytes[byteIndex] += 1
            elif char == "-": bytes[byteIndex] -= 1
            elif char == ".":
                if selectedByte >= 0: print(chr(selectedByte), end="")
            elif char == "^": print(selectedByte, end="")
            elif char == "[":
                loop = "while"
                loopPos = index
            elif char == "]":
                if loop == "while":
                    if selectedByte != 0: index = loopPos
                else:
                    print(f"Error at character {index}: Unclosed loop ('[]')")
                    break
            elif char == ">": byteIndex += 1
            elif char == "<": byteIndex -= 1
            elif char == ",": 
                inp = input()
                bytes[byteIndex] = ord(inp)
            elif char == "#": comment = True
            elif char == ":": 
                skips.append(index)
                index = selectedByte
            elif char == "{":
                if selectedByte != 0:
                    if closestIndex(code, "}", index): index = closestIndex(code, "}", index)
                    else:
                        print(f"Error at character {index}: Unclosed branch ('{'{}'}')")
                        break
            elif char == "@": byteIndex = selectedByte
            elif char == "_": print("") # newline btw
            elif char == "~": debug = not debug # aka the inverse of 'debug'
            elif char == "|":
                imports.append(code.split("\n")[index - 1][1:])
                runcode(open(code.split("\n")[index - 1][1:]).read())
                index = closestIndex(code, "\n", index - 1)
            elif char == "%" and debug: print(bytes)
        if debug: print(f"\nDEBUG: Char #{index} (on byte {byteIndex}; {selectedByte}): {char}\n")
    if debug: print(f"Program finished: {len(code)} characters, with {len(imports)} import{'s' if len(imports) != 1 else ''}{f', them being: {imports}' if imports else '.'}")
if __name__ == "__main__": runcode(argcode)
