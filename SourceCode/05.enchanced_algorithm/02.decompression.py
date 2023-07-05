with open('D:\\UBUNTU\\BITS\\year-1 sem-1\\algorithms\\implementation\\Input_Files\\inputs\\text2.txt') as f:
    lines = f.readlines()
# print(lines)

# print(lines[0][0])

t = []
t1_string = ""    
for i in range(len(lines[0])):
    if lines[0][i] == " ":
        t.append(t1_string)
        t1_string = ""
    else:
        t1_string += lines[0][i]

indexes = []
for i in range(0, len(t)-1, 2):
    indexes.append([t[i], int(t[i+1])])
# print(indexes)

base62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

for i in range(len(indexes)):
    base62form = indexes[i][0]
    lengthOfbase62Form = len(base62form) - 1
    count = 0
    decimal = 0
    while lengthOfbase62Form >= 0:
        x = base62.index(base62form[count])
        decimal += x * pow(62, lengthOfbase62Form)
        count+=1
        lengthOfbase62Form-=1
    indexes[i][0] = str(decimal)

# print()
# print()
print(indexes)

decompressed_indexes = []
for i in range(len(indexes)):
    for j in range(0, len(indexes[i][0]), indexes[i][1]):
        decompressed_indexes.append(int(indexes[i][0][j:j+indexes[i][1]]))
# print(decompressed_indexes)


words = lines[1].split()

# print(words)

for i in range(len(words)):
    t = words[i][0:2]
    if t == '\\n':
        continue    
    else:
        n = ""
        count = 0
        for j in range(len(words[i])):
            if words[i][j] >= '0' and words[i][j]<='9':
                n += words[i][j]
                count+=1
            else:
                break
            if n == "":
                break
            else:
                n = int(n)
                words[i] = words[i-1][:n] + words[i][count:]
                break
# print(words)

decompressed_words = []
for i in range(len(words)):
    t = words[i][0:2]
    if t == '\\n':
        m = int(words[i][2:])
        for i in range(m):
            decompressed_words.append("\n")    
    else:
        n = ""
        c=0
        for j in range(len(words[i])-1, -1, -1):
            if words[i][j] >= '0' and words[i][j]<='9':
                n += words[i][j]
                c+=1
            else:
                w = words[i][:-c]
                n = int(n)
                for i in range(n):
                    decompressed_words.append(w)              
                break
print()
print(decompressed_words)
print()
print(decompressed_indexes)
print()

combined = []
for i in range(len(decompressed_indexes)):
    combined.append([decompressed_words[i], decompressed_indexes[i]])
combined.sort(key=lambda x: x[1])
print(combined)

s = ""
for i in range(len(combined)):
    s += combined[i][0]
    if combined[i][0] == '\n':
        continue
    s += " "
print(s)

with open('D:\\UBUNTU\\BITS\\year-1 sem-1\\algorithms\\implementation\\text_files\\decompressed.txt', "w") as f:
    f.write(s)


