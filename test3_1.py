import sys
fname = input("Enter data file name: ")
try:
    fH = open(fname)
except FileNotFoundError as e:
    print("No such file: " + fname)
    sys.exit()

wordcount = {}
for line in fH:
    words = line.split()

    for word in words:
	wordcount[word] = wordcount.get(word, 0) + 1		
fH.close()

for word in wordcount:
    print(word, ":", wordcount[word])
