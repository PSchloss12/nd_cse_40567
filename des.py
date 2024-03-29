key = "0100110001001111010101100100010101000011010100110100111001000100"
ciphertext = "1100101011101101101000100110010101011111101101110011100001110011"

# first key permutation table (drops every 8th bit)
PC_1 = [57, 49, 41, 33, 25, 17, 9,
1, 58, 50, 42, 34, 26, 18,
10, 2, 59, 51, 43, 35, 27,
19, 11, 3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,
7, 62, 54, 46, 38, 30, 22,
14, 6, 61, 53, 45, 37, 29,
21, 13, 5, 28, 20, 12, 4]

# second key permutation table
PC_2 = [14, 17, 11, 24, 1, 5,
3, 28, 15, 6, 21, 10,
23, 19, 12, 4, 26, 8,
16, 7, 27, 20, 13, 2,
41, 52, 31, 37, 47, 55,
30, 40, 51, 45, 33, 48,
44, 49, 39, 56, 34, 53,
46, 42, 50, 36, 29, 32]

# initial permutation
IP = [58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]

E = [32, 1, 2, 3, 4, 5, 4, 5,
    6, 7, 8, 9, 8, 9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32, 1]

# s boxes
sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
 
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
 
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
 
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
 
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
 
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
 
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
 
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

# f() output permutation
P = [16,  7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4, 25]

# final permutation
IP_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

K_ex = "0001001100110100010101110111100110011011101111001101111111110001"

# def drop_parity_bits(key):
#     '''discarding of every 8th bit of the key produces a 56-bit key from the original 64-bit key'''
#     l = len(key)
#     new = ""
#     for i in range(l):
#         if i%8==0:
#             continue
#         new += key[i]
#     return new

def shift_left(input, shift):
    input += input[:shift]
    return input[shift:]

def generate_keys(key):
    '''used for subkey generation'''
    shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    if len(key)!=64:
        raise ValueError('key is of wrong length for subkey generation')
    
    # permute the key
    k_permuted = ""
    for i in PC_1:
        k_permuted += key[i-1]
    if len(k_permuted)!=56:
        raise ValueError('key is of wrong length for subkey generation')

    # generate subkeys and then new keys
    mid = int(len(k_permuted)/2)
    c = k_permuted[:mid]
    d = k_permuted[mid:]

    keys = [""]*16
    for i in range(16):
        c = shift_left(c,shift_table[i])
        d = shift_left(d,shift_table[i])
        cd = c+d
        for j in PC_2:
            keys[i] += cd[j-1]

    return keys

def XOR(a,b):
    if len(a)!=len(b):
        raise ValueError('inputs are of different sizes')
    xor = lambda x,y: "1" if ((x=="1" and y=="0") or (y=="1" and x=="0")) else "0"
    c = ""
    for i in range(len(a)):
        c += xor(a[i],b[i])
    return c

def bin2dec(binary):
    '''https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/'''
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def dec2bin(num):
    '''https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/'''
    res = bin(num).replace("0b", "")
    if(len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res

def f(r,k):
    # expand input to 48 bits
    r_expanded = ""
    for i in E:
        r_expanded+= r[i-1]
    # plug into sboxes to reduce back to 32 bits
    b = XOR(k,r_expanded)
    s_out = ""
    for i in range(8):
        bi = b[i*6:(i+1)*6]
        row = bin2dec(int(bi[0]+bi[-1]))
        col = bin2dec(int(bi[1:-1]))
        s_out += dec2bin(sbox[i][row][col])
    # permute output
    output = ""
    for i in P:
        output += s_out[i-1]
    # print(output)
    return output

M = "0000000100100011010001010110011110001001101010111100110111101111"
def encode(message, keys):
    ip = ""
    for i in IP:
        ip+= message[i-1]
    
    mid = int(len(ip)/2)
    li = ip[:mid]
    ri = ip[mid:]

    for i in range(16):
        ri_1 = ri
        ri = XOR(li,f(ri_1,keys[i]))
        li = ri_1
    
    rl = ri+li
    output = ""
    for i in IP_1:
        output+= rl[i-1]
    return output

def decode(cipher, keys):
    keys.reverse()
    ip = ""
    for i in IP:
        ip+= cipher[i-1]
    
    mid = int(len(ip)/2)
    li = ip[:mid]
    ri = ip[mid:]
    # print(f"L0: {li} R0: {ri}")
    for i in range(16):
        ri_1 = ri
        ri = XOR(li,f(ri_1,keys[i]))
        li = ri_1
        # print(f"L{i+1}: {li} R{i+1}: {ri}")
    
    rl = ri+li
    output = ""
    for i in IP_1:
        output+= rl[i-1]
    return output

def decode_binary_string(s):
    '''https://stackoverflow.com/questions/40557335/binary-to-string-text-in-python'''
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

keys = generate_keys(key)
# print(keys)
binary = decode(ciphertext, keys)
plaintext = decode_binary_string(binary)
print(plaintext)