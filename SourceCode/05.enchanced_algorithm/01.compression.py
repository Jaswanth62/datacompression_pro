def utf8len(s):
    return len(s.encode('utf-8'))

def compression():
    with open('D:\\UBUNTU\\BITS\\year-1 sem-1\\algorithms\\implementation\\text_files\\text2.txt') as f:
        lines = f.readlines()
    print(lines)
    print()

    compressed_string = []
    word_count = 1

    for line in lines:
        temp = ""
        for char in line:
            if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z'):
                temp+=char
            elif char == ' ':
                compressed_string.append((temp, word_count))
                temp = ""
                word_count+=1
            elif char == '\n':
                compressed_string.append((temp, word_count))
                word_count+=1
                compressed_string.append(("\n", word_count))
                word_count+=1
    print()
    print(compressed_string)
    print()

    compressed_string.sort(key=lambda x:x[0])
    # print(compressed_string)

    words = []
    indexes = []
    for t in compressed_string:
        words.append(t[0])
        indexes.append(t[1])

    # print()
    print(words)
    # print(indexes)

    # *********************** PHASE 1 - WORDS ***************************
    # PART 1 APPLY RLE
    RLE = []
    occurance=1
    for i in range(len(words)-1):
        if words[i] == words[i+1]:
            occurance+=1    
        else:
            RLE.append(words[i] + str(occurance))
            occurance = 1
    RLE.append(words[len(words)-1] + str(occurance))    
    print(f'RLE: {RLE}')

    # PART 2 APPLY INCREMENTAL PREFIX ENCODING 

    IPE = []
    for i in range(len(RLE)):
        if (RLE[i][0] == '\n') or (RLE[i-1][0] != RLE[i][0]):
            IPE.append(RLE[i])
            continue
        elif len(RLE[i-1]) < len(RLE[i]):
            length = len(RLE[i-1])
        else :
            length = len(RLE[i])
        
        common_char = 0
        for j in range(length):
            if  RLE[i-1][j] == RLE[i][j]:
                common_char += 1
            else:
                if common_char == 0:
                    IPE.append(RLE[i])
                else:
                    IPE.append(str(common_char) + RLE[i][common_char:])
                    break
    # print(f'INCREMENTAL PREFIX: {IPE}')
    # print()
    # print()
    # print()
    # *********************** PHASE 2 - INDEXES ***************************

    print(f'indexes: {indexes}')
    count = []
    for i in indexes:
        c = 0
        if i == 0:
            c+=1
        while i != 0:
            i = i // 10
            c=c+1
        count.append(c)
    print(f"count: {count}")

    compressed_indexes = []
    compressed_indexes_length = 0
    num = -1
    for i in range(len(indexes)-1):
        if count[i] != count[i+1]:
            if num > 0:
                compressed_indexes.append([num, count[i]])
                num = -1
                compressed_indexes_length += 1
            else:
                compressed_indexes.append([indexes[i], count[i]])
                compressed_indexes_length += 1
        else:
            if num > 0:
                num = num*pow(10,count[i+1]) + indexes[i+1]

            else:
                num = indexes[i]*pow(10, count[i+1]) + indexes[i+1]
    print(f"num {num}")
    compressed_indexes.append([num, count[i]])

    # if count[i+1] == compressed_indexes[compressed_indexes_length-1][1]:
    #     compressed_indexes.append([compressed_indexes[compressed_indexes_length-1][0]*pow(10,count[i+1]) + indexes[i+1] , count[i+1]])
    # else:
    #     compressed_indexes.append([indexes[i+1],count[i+1]])

    print(f"qwerty{compressed_indexes}")


    base62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for t in compressed_indexes:
        n = t[0]
        k = ""
        while n != 0:
            t1 = n % 62
            k = base62[t1] + k
            n = n//62
        t[0] = k

    print()
    print(f'original file:\n{lines}\n')
    print(f'compressed words: \n{IPE}\n')
    print(f'compressed indexes: \n{compressed_indexes}\n')
    print()

    with open('D:\\UBUNTU\\BITS\\year-1 sem-1\\algorithms\\implementation\\text_files\\compressed.txt', 'w') as f:
        for i in compressed_indexes:
            f.write(i[0] + " " + str(i[1]))
            f.write(" ")
        f.write("\n")

        for s in IPE:
            if(s[0] == "\n"):
                f.write("\\n")
                f.write(s[1:])
                f.write(" ")
            else:
                f.write(s)
                f.write(" ")

