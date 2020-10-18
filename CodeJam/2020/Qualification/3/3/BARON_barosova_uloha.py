s = open("input_file.txt","r")

y = 0 
for riadok in s:
    y += 1
    riadok = riadok.split()
    if y == 1:
        krat = riadok[0]

    if y > 1 and y%2==0:
        vsetky = []
        pismena = []
        nove = []
        cisla = []
        text = []
        p = True
        slovnik = {}
        N = int(riadok[0])
        T = int(riadok[1])
        
        for i in range (3,N+1):
            vsetky.append(i)
        for i in range(N):
            x = vsetky[0]  
            for i in vsetky:
                if i%x==0:
                    vsetky.remove(i)
            vsetky.append(x)
        vsetky.sort()
        
    if y > 1 and y%2!=0:
        l = int(riadok[0])
        for item in riadok:
            dane = int(item)
            
            for u in vsetky:
                if dane%u==0:
                    pismena.append(u)
                
        
        for i in pismena:
            if i not in nove:
                nove.append(i)
        nove.sort()
        
        for i in nove:
            if p == True:
                if l%i==0:
                    p = False
                    cisla.append(i)
        for i in riadok:
            dane = int(i)
            x = dane/int(cisla[-1])
            cisla.append(int(x))
        
        


                    
        for i in range(65,91):
            slovnik[nove[i-65]] = chr(i)
            #slovnik.update({nove[i-65]:chr(i)})
            

        for i in cisla:
            print(i, slovnik.get(i))
            text.append(slovnik.get(i))
        print(i, text)
        print(*text)
       


        
   
            
        
    
