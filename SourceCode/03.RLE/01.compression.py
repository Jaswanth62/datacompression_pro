def encode_message(message):
    print(message)
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1): 
            if (message[j] == message[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string

def display():
    
    with open('D:/UBUNTU/BITS/year-1 sem-1/algorithms/implementation/FLASK/src/Input_Files/inputs/text2.txt') as f:
        lines = f.readlines()

    compressed_text = []
    for i in range(len(lines)):
        compressed_text.append(encode_message(lines[i]))

    with open("D:/UBUNTU/BITS/year-1 sem-1/algorithms/implementation/FLASK/src/Input_Files/03.RLE/compressed.txt", "w") as f:
        for line in compressed_text:
            f.write("".join(line))
            

    
display()

        
