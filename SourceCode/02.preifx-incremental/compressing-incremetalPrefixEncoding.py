
    # IPE = []
    # for i in range(len(RLE)):
    #     if (RLE[i][0] == '\n') or (RLE[i-1][0] != RLE[i][0]):
    #         IPE.append(RLE[i])
    #         continue
    #     elif len(RLE[i-1]) < len(RLE[i]):
    #         length = len(RLE[i-1])
    #     else :
    #         length = len(RLE[i])
        
    #     common_char = 0
    #     for j in range(length):
    #         if  RLE[i-1][j] == RLE[i][j]:
    #             common_char += 1
    #         else:
    #             if common_char == 0:
    #                 IPE.append(RLE[i])
    #             else:
    #                 IPE.append(str(common_char) + RLE[i][common_char:])
    #                 break
    # # print(f'INCREMENTAL PREFIX: {IPE}')








def utf8len(s):
    return len(s.encode('utf-8'))


with open('D:/UBUNTU/BITS/year-1 sem-1/algorithms/implementation/FLASK/src/Input_Files/inputs/text2.txt') as f:
    lines = f.readlines()

compressed_string = []
for x in range(len(lines)):
    t = []
    inp = lines[x].split()
    print(inp)
    for i in range(len(inp)):
        length=0
        if i == 0:
            t.append(inp[i])
            continue
        if (inp[i][0] == '\n') or (inp[i-1][0] != inp[i][0]):
            t.append(inp[i])
        elif len(inp[i - 1]) < len(inp[i]):
            length = len(inp[i - 1])
        else:
            length = len(inp[i])

        count=0
        print(i, length)
        for k in range(length):
            if inp[i-1][k] == inp[i][k]:
                count = count + 1
            else:
                if count == 0:
                    t.append(inp[i])
                else:
                    print(count)
                    t.append(str(count) + inp[i][count:])
                    break
        if length == count:
            t.append(str(count) + inp[i][count:])
    compressed_string.append(t)
print(compressed_string)
with open("D:/UBUNTU/BITS/year-1 sem-1/algorithms/implementation/FLASK/src/Input_Files/02.IPE/compressed.txt", 'w') as f:
    for line in compressed_string:
        f.write(" ".join(line))
        f.write("\n")