n = int(input("Enter characters: "))

file = open("class-notes.txt", "r")
print(file.read(n))
file.close()
print(n)

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()

print("Total Lines: ", len(lines))

for i in range(len(lines)):
    print(i+1, "->", lines[i].strip())
print()

word = input("Skip lines starting with: ")
file = open("class-notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("Skip ->", line.strip())
    else:
        print("keep ->", line.strip())
file.close()
print()

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()

out = open("class-notes-out.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd Lines saved to odd-lines.txt")