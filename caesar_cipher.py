
probs = {
"E":12.02,
"T":9.10,
"A":8.12,
"O":7.68,
"I":7.31,
"N":6.95,
"S":6.28,
"R":6.02,
"H":5.92,
"D":4.32,
"L":3.98,
"U":2.88,
"C":2.71,
"M":2.61,
"F":2.30,
"Y":2.11,
"W":2.09,
"G":2.03,
"P":1.82,
"B":1.49,
"V":1.11,
"K":0.69,
"X":0.17,
"Q":0.11,
"J":0.10,
"Z":0.07,
}

def shift_letter(letter, shift):
    return chr(((ord(letter)-65+shift) % 26)+65)

def decrypt(input):
    frequencies = {}
    for letter in input:
        frequencies[letter] = input.count(letter)/len(input)
    correlations = []
    for i in range(0,25):
        cur_sum = 0
        for letter in input:
            cur_sum+= frequencies[letter]*probs[shift_letter(letter, i)]
        correlations.append((i,cur_sum))
    correlations = sorted(correlations, key = lambda x: x[1], reverse=True)
    for shift, prob in correlations:
        word = ""
        for letter in input:
            word+=shift_letter(letter, shift)
        print(f"Soluion: {word}; Probability: {round(prob,2)}")
        print(f"Shift: {shift}")

if __name__ == "__main__":
    decrypt("XJHWJY")