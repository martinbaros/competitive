from sys import stdout


t,a,b = [int(s) for s in input().split(" ")]
for case_idx in range(t):
    if a == 10**9-5:
        x = -5
        y = -5
        done = False
        pocitadlo = 0
        for i in range(10):
            for k in range(10):
                if not done:
                    print(x+i, y+k)
                    stdout.flush()

                    hodnotenie = str(input())
                    s = open("new.txt","a")
                    s.write(hodnotenie)
                    s.close()
                    if  hodnotenie == "CENTER":
                        done = True
                    pocitadlo+=1

        for i in range(300-pocitadlo):
            print(i,i)
            stdout.flush()
            s = open("new.txt","a")
            s.write(i+pocitadlo)
            s.close()
    elif a == 10**9-500:
        print(a+1, 0)
        stdout.flush()
        hodnotenie = str(input())
        s = open("new.txt","a")
        s.write(hodnotenie)
        s.close()
        o_x = +1
        for i in range(299):
            print(i,i)
            stdout.flush()
