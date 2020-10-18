cases = 3
lower = 1
upper = 301
cisla = []
import random
print("Prime numbers between", lower, "and", upper, "are:")
s = open("input_file.txt","w")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 2:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           cisla.append(num)



print(cases, file=s)
for i in range(cases):
    poradie = []
    while len(poradie) < 26:
        cisielko = random.choice(cisla)
        if cisielko not in poradie:
            poradie.append(cisielko)
    poradie.sort()
    slovnik = {}
    nove = []
    pismenka = []

    for r in range(26):
        pismenka.append(chr(65+r))
        slovnik[chr(65+r)] = poradie[r]
    if i == 0:
        sprava = "PROGRAMOVANIE NA X HODIN QWERTZUIOPASDFGHJKLYXCVBNM"
    else:
        sprava = ""
        for i in range(2):
            random.shuffle(pismenka)
            for pismeno in pismenka:
                sprava+=pismeno

    for pismeno in sprava:
        if pismeno != " ":
            nove.append(slovnik[pismeno])
    vysledok = []
    for i in range(len(nove)-1):
        vysledok.append(str(nove[i]*nove[i+1]))

    print(f"{upper} {len(vysledok)}",file = s)
    print(" ".join(vysledok),file = s)
    print(sprava)
