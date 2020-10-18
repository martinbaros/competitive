from sys import stdout
n,q = [int(s) for s in input().split(" ")]
a = []

for pp in range(n):
  	a.append(chr(65+pp))
pos = chr(65+pp)
aktual = "A"
done = set()
for case_idx in range(q):
    ind = a.index(aktual)
    if ind != n-1:
        f,s = a[ind], a[ind+1]
        if ((f+s) not in done) and ((s+f) not in done):
            #print(done)
            print("? {} {}".format(f,s))
            done.add(f+s)
            done.add(s+f)
            stdout.flush()
            if str(input()) == ">":
                a[ind], a[ind+1] = a[ind+1], a[ind]
            else:
                if aktual != pos:
                    aktual = chr(ord(aktual)+1)
        else:
            if aktual != pos:
                q+=1
                aktual = chr(ord(aktual)+1)
    else:
        if aktual != pos:
            q+=1
            aktual = chr(ord(aktual)+1)

print("! {}".format("".join(a)))
stdout.flush()
