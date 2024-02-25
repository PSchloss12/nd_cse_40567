import caesar_cipher as caesar

cipher_text = "TTEUM GQNDV EOIOL EDIRE MQTGS DAFDR CDYOX IZGZP PTAAI TUCSI XFBXY SUNFE   SQRHI SAFHR TQRVS VQNBE EEAQG IBHDV SNARI DANSL EXESX EDSNJ AWEXA ODDHX EYPKS YEAES RYOET OXYZP PTAAI TUCRY BETHX UFINR"
before_repeat = "ZP PTAAI TUCSI XFBXY SUNFE   SQRHI SAFHR TQRVS VQNBE EEAQG IBHDV SNARI DANSL EXESX EDSNJ AWEXA ODDHX EYPKS YEAES RYOET OXY"
plain_text = "THE VIGENERE CIPHER IS A METHOD  OF ENCRYPTING ALPHABETIC TEXT BY USING A  SERIES OF INTERWOVEN CAESAR CIPHERS BASED ON THE LETTERS OF A KEY WORD IT EMPLOYS A FORM OF POLYALPHABETIC SUBSTITUTION"

def longest_repititions(X):
    m = len(X)
    sequence = [""]*m
    for i in range(m):
        for j in range(i+1,m):
            offset = 0
            temp = ""
            while j+offset<m and X[i+offset]==X[j+offset]:
                temp+=X[i+offset]
                offset+=1
            if len(temp)>len(sequence[i]):
                sequence[i]=temp
            
    return sequence

def repeat_distance(string, sub_string):
    locations = []
    loc = string.find(sub_string)
    print(loc, string[loc:loc+1])
    locations.append(loc)
    while string[loc+1:].find(sub_string)!=-1:
        loc = string[loc+1:].find(sub_string)+locations[-1]+1
        locations.append(loc)
        print(loc)
    distances = []
    for i in range(1,len(locations)):
        distances.append(locations[i]-locations[i-1])
    return distances

def period(cipher_text):
    sequences = longest_repititions(cipher_text)
    seq_count = {}
    for i in sequences:
        if len(i)>1:
            if i in seq_count:
                seq_count[i]+= cipher_text.count(i)
            else:
                seq_count[i]= cipher_text.count(i)
    candidates = []
    for string, count in seq_count.items():
        if count>2 or len(string)>2:
            flag = False
            for i in candidates:
                if string in i:
                    flag = True
                    break
            if flag:
                continue
            candidates.append(string)
    for i in candidates:
        print(repeat_distance(cipher_text, i))

def ic(c):
    n = len(c)
    total = 0
    for i in range(65,90+1):
        count = c.count(chr(i))
        total+= count*(count-1)
    return total/n/(n-1)

def divide_alphabets(c,p):
    alphas = [""]*p
    for i in range(len(c)):
        alphas[i%p]+=c[i]
    return alphas

def test_ic():
    for i in [2,4,5,10,20,25]:
        alphabets = divide_alphabets(cipher_text,i)
        avg_ic = 0
        for a in range(len(alphabets)):
            avg_ic+=ic(alphabets[a])
        print(f"With period of {i}, average ic is {avg_ic/len(alphabets)}")
        
    print(ic(cipher_text))

def letter_freq(text):
    freq = {}
    for i in range(65,90+1):
        freq[chr(i)] = text.count(chr(i))
    return freq

if __name__ == '__main__':
    cipher_text = cipher_text.replace(" ","")
    alphabets = divide_alphabets(cipher_text,5)
    for a in alphabets:
        print(caesar.decrypt(a))
        print()
    