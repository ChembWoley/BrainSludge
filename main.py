import sys

argcode = open(sys.argv[1]).read()

def closestIndex(string: str, search: str, userIndex: int) -> int:
    indexes = [pos for pos, char in enumerate(string) if char == search and pos > userIndex]
    if not indexes:
        return None
    return min(indexes, key=lambda x: abs(x - userIndex))

def runcode(code: str):
    debug = False
    byteIndex = 0
    bytes = [0 for _ in range(30000)]
    loop = ""
    loopPos = 0
    comment = False
    skips = []
    imports = []
    for index, char in enumerate(code):
        selectedByte = bytes[byteIndex]

        if comment:
            if char == ";":
                comment = False
        else:
            if index in skips:
                pass
            elif char == "+":
                bytes[byteIndex] += 1
            elif char == "-":
                bytes[byteIndex] -= 1
            elif char == ".":
                if selectedByte >= 0:
                    print(chr(selectedByte), end="")
            elif char == "^":
                print(selectedByte, end="")
            elif char == "[":
                loop = "while"
                loopPos = index
            elif char == "]":
                if loop == "while":
                    if selectedByte != 0:
                        index = loopPos
                else:
                    print(f"\n Error at character {index}: loose ']'.")
                    break
            elif char == ">":
                byteIndex += 1
            elif char == "<":
                byteIndex -= 1
            elif char == ",":
                inp = input()
                bytes[byteIndex] = ord(inp)
            elif char == "#":
                comment = True
            elif char == ":":
                skips.append(index)
                index = selectedByte
            elif char == "{":
                if selectedByte != 0:
                    index = closestIndex(code, "}", index)
            elif char == "@":
                byteIndex = selectedByte
            elif char == "_":
                print("")
            elif char == "~":
                debug = False if debug else True
            elif char == "|":
                imports.append(code.split("\n")[index-1][1:])
                runcode(open(code.split("\n")[index-1][1:]).read())
                index = closestIndex(code, "\n", index-1)
            elif char == "%" and debug: print(bytes)
        if debug:
            print(f"\nDEBUG: Char #{index} (on byte {byteIndex}; {selectedByte}): {char}\n")
    if debug:
        print(f"Program finished: {len(code)} characters, with {len(imports)} import{'s' if len(imports) != 1 else ''}{f', them being: {imports}' if imports else '.'}")
if __name__ == "__main__":
    runcode(argcode)
