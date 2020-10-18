print("zadávanie ukončíte stlačením x")

zoznam={}
tovar=[]

a=0
while a!="x":
    a=input("Zadajte tovar: ")
    zoznam[a]=0
    tovar.append(a)
if a == "x":
        print("koniec")
        del zoznam["x"]
        tovar.remove("x")
        print("Stav:",zoznam)

b=0
while b!= "x":
    for nazov in tovar:
        b=input(f"zmena počtu {nazov}: ")
        if b!= "x":
            c=zoznam[nazov]
            c+=int(b)
            if c<0:
                print("KLESLI BY STE POD 0")
                c-=int(b)
                print(c)
            zoznam[nazov] = c
        else:
            print("KONIEC")
            break
    if b!= "x":
        hodnota=0
        for key,value in zoznam.items():
            if value<=hodnota:
                print(f"nedostatočný počet položky {key}")
print(zoznam)
