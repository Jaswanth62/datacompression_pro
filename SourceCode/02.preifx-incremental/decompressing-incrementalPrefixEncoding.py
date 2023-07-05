with open('text_files/compressed_text1.txt') as f:
    lines = f.readlines()
print(lines)

decompressed_string = []
for k in range(len(lines)):
    t = []
    inp = lines[k].split()

    for i in range(len(inp)):
        c = ''
        for j in range(len(inp[i])):
            if '0' <= inp[i][j] <= '9':
                c += inp[i][j]
        if c == '':
            t.append(inp[i])
            continue
        commonSubstringLength = int(c)
        t.append(t[i-1][:commonSubstringLength] + inp[i][len(c):])
    decompressed_string.append(t)

for line in decompressed_string:
    print(line)

with open("text_files/decompressed_text1.txt", 'w') as f:
    for line in decompressed_string:
        f.write(" ".join(line))
        f.write("\n")




