all = []
s = open("gogly_out.txt", "w")
with open("google.txt","r") as f:
    for line in f:
        line = line.strip()

        all.append(line)

i = 0
print(all)
for case in all:
    if i!= 0:
        a = ""
        b = ""
        for letter in case:
            print(letter)
            if letter == "4":
                a+="2"
                b += "2"
            else:
                a+=letter
                b+= "0"
        print(f"Case #{i}: {int(a)} {int(b)}",file=s)

    i+=1
s.close()
