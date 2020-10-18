klasifikacny = {}
with open("ziaci.txt", "r")as s:
    for line in s:
        line = line.strip()
        zoznam = line.split(" ")
        meno = zoznam[0]
        znamky = [int(zoznam[1]),int(zoznam[2]),int(zoznam[3]),int(zoznam[4]),int(zoznam[5])]
        priemer = sum(znamky)/len(znamky)
        klasifikacny[meno] = priemer
        print(priemer)

def priemer_triedy(klasifikacny):
    priemery = 0
    for priemer in klasifikacny.values():
        priemery += priemer
    p_t = priemery/len(klasifikacny)
    return p_t
def naj(klasifikacny):
    top_p = 0
    najhorsie_p = 0
    i= 1
    for meno in sorted(klasifikacny, key = klasifikacny.get):
        if i < 3:
            top_p += klasifikacny[meno]
        elif i >= len(klasifikacny)-2:
            najhorsie_p += klasifikacny[meno]
        i+=1
    return [top_p/2, najhorsie_p/3]
def vypis(klasifikacny):
    for meno in sorted(klasifikacny, reverse = True):
        print(meno)

def lepsi(klasifikacny,p_t):
    pocet = 0
    for priemer in klasifikacny.values():
        if priemer < p_t:
            pocet += 1
    return pocet



print(naj(klasifikacny))
zadane = ""
while zadane != "x":
    print(f"Priemer triedy je: {priemer_triedy(klasifikacny)}")
    print(f"Priemer top dvoch je: {naj(klasifikacny)[0]} a priemer najhorších troch je: {naj(klasifikacny)[1]}")
    print("Mená zoradené: ")
    vypis(klasifikacny)
    print(f"Počet žiakov s priemerom lepším ako priemer triedy je: {lepsi(klasifikacny,priemer_triedy(klasifikacny))}")
    zadane = input("Zadajte meno nového žiaka a jeho priemer alebo 'x': ")
    if zadane != "x":
        zadal = zadane.split(" ")
        klasifikacny[zadal[0]] = float(zadal[1])
