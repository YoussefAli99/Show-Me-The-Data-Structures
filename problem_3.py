import sys

def huffman_encoding(data):
    global huff
    huff = dict()
    for c in data:
        huff[c] = huff.get(c, 0)+1
    tr = dict()
    temp = '1'
    for n in sorted(huff.items(), key = lambda x: x[1]):
        tr[n[0]] = temp
        temp = '0'+temp
    enc = ''
    for d in data:
        enc += tr[d]
    return enc, tr

def huffman_decoding(data,tree):
    huff = dict()
    for c in tree:
        huff[tree[c]] = c
    temp, dec = '', ''
    for d in data:
        if d == '1':
            dec += huff[temp + d]
            temp = ''
        else:
            temp += d
    return dec

def testing(x):
    print ("The size of the data is: {}\n".format(sys.getsizeof(x)))
    print ("The content of the data is: {}\n".format(x))

    encoded_data, tree = huffman_encoding(x)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


if __name__ == "__main__":
    codes = {}

    great_sentences = ['The bird is the word', 'aaaaaaaaaaa', ' ']
    for e in great_sentences:
        testing(e)

    