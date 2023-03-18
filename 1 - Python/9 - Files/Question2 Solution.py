data = []


for i in range(5):
    line = input("Enter Sentence For Us : ")
    data.append(line)

with open("efile.txt", "w") as f:
    for line in data:
        f.write(line)
        f.write("\n")

with open("efile.txt", "r") as ff:
    contents = ff.read()
    print(contents)

