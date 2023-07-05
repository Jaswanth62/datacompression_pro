import sys
from huffman_encoding_and_decoding import huffman_encoding_func, huffman_decoding_func

sentences_file = open("data.txt", "r")
sentences = sentences_file.readlines()
for number, senctence in enumerate(sentences, 1):
    print("The size of the data is: {}".format(sys.getsizeof(senctence)))
    print("The content of the data is: {}".format(senctence))
    print("Encoding process: ")
    tree, encoded_data = huffman_encoding_func(senctence)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))
    print("Decoding process: ")
    decoded_data = huffman_decoding_func(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))
sentences_file.close()

