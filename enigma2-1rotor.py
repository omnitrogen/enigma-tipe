#enigma2
#un seul rotor (sans OOP)

alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
alphabetDict = {'G': 7, 'U': 21, 'T': 20, 'L': 12, 'Y': 25, 'Q': 17, 'V': 22, 'J': 10, 'O': 15, 'W': 23, 'N': 14, 'R': 18, 'Z': 26, 'S': 19, 'X': 24, 'A': 1, 'M': 13, 'E': 5, 'D': 4, 'I': 9, 'F': 6, 'P': 16, 'B': 2, 'H': 8, 'K': 11, 'C': 3, ' ':27}
rotor1 = ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H']
rotor2 = ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q']
rotor3 = ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q','Z','P','O','S','G','X','N','R','M','W','F','L']
reflector = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']

def rotationRotor(liste1):
    liste1.append(liste1[0])
    del liste1[0]
    return liste1

def estValide(liste1):
    for elt in liste1:
        if alphabetList.count(elt.upper()) < 1:
            return False
    return True

print("Welcome to the enigma machine")
messageList = []
while estValide(messageList) == False or len(messageList) <= 0:
    try:
        message = str(input("Write the message you want to (de)crypt: \n"))
        messageList = list(message)
    except ValueError:
        print("You must only enter letter without special characters!")
g = []
for i in range(0,len(messageList),1):
    if messageList[i] == ' ':
        g.append(' ')
    else:
        a = alphabetDict[messageList[i].upper()]
        b = rotor1[a-1]
        c = alphabetDict[b]
        d = reflector[c-1]
        e = rotor1.index(d)
        f = alphabetList[e]
        g.append(f)
    if (i+1)%1 == 0:
        rotationRotor(rotor1)
print("(de)crypted message: ",''.join(g))
