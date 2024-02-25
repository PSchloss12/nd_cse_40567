key = "0100110001001111010101100100010101000011010100110100111001000100"
ciphertext = "1100101011101101101000100110010101011111101101110011100001110011"

shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def drop_parity_bits(key):
    '''discarding of every 8th bit of the key produces a 56-bit key from the original 64-bit key'''
    l = len(key)
    new = ""
    for i in range(l):
        if i%8==0:
            continue
        new += key[i]
    return new

def shift_left(input, shift):
    input += input[:shift]
    return input[shift:]

def key_transformation(key, shift):
    '''used for subkey generation'''
    # if len(key)!=56:
    #     raise ValueError('key is of wrong length for subkey generation')
    mid = int(len(key)/2)
    combined = shift_left(key[:mid],shift)+shift_left(key[mid:],shift)
    print(combined)

key_transformation("123456",2)