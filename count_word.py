fname = input("Enter file name: ")
word = input("Enter word to be searched:")
k = 0
line_no={}
count=0

with open(fname, 'r') as f:
    for line in f:
        count=count+1
        words = line.split()

        for i in words:

            if (i == word):
                k = k + 1
                line_no.setdefault(word, []).append(count)


print("Occurrences of the word:")

print(k)
print(line_no)
