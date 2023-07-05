def decode_message(our_message):
    decoded_message = ""
    i = 0
    j = 0
    # splitting the encoded message into respective counts
    while (i <= len(our_message) - 1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        # displaying the character multiple times specified by the count
        for j in range(run_count):
            # concatenated with the decoded message
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message


def display():
    with open('D:/UBUNTU/BITS/year-1 sem-1/algorithms/implementation/FLASK/src/Input_Files/03.RLE/compressed.txt') as f:
        lines = f.readlines()

    decompressed_text = []
    for i in range(len(lines)):
        decompressed_text.append(decode_message(lines[i]))

    with open("D:/UBUNTU/BITS/year-1 sem-1/algorithms/implementation/FLASK/src/Input_Files/03.RLE/decompressed.txt", "w") as f:
        for line in decompressed_text:
            f.write("".join(line))
    
display()