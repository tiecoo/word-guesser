import sys
 
word = input("Write word to guess\n")

possiblewords = []
with open("words.txt", "r", encoding="utf8") as file:
    for line in file:
        line = line.lower()
        if len(word) != len(line.replace("\n", "")):
            continue

        ispossible = True
        for i in range(len(word)):
            if(word[i] != "_"):
                if (word[i].lower() != line[i]):
                    ispossible = False
        
        if ispossible:
            possiblewords.append(line)

print("possible words are: ")
for word in possiblewords:
    print(word)