import sys

def eprint(*args, **kwargs):
    if DEBUG:
        print(*args, file=sys.stderr, **kwargs, flush=True)
    else:
        pass
def sprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)
    eprint(*args, **kwargs)

DEBUG=False
t,a,b=map(int,input().split())
magic=[(-5*10**8,-5*10**8),(5*10**8,-5*10**8),(5*10**8,5*10**8),(-5*10**8,5*10**8),(0,-5*10**8),(-5*10**8,0),(0,5*10**8),(5*10**8,0)]

for i in range(t):
    for gx,gy in magic:
        sprint(gx,gy)
        resp=input()
        if resp=='CENTER' or resp=='WRONG'or resp=='HIT':break
    else:
        eprint('Not so magic?')
        break
    if resp=='WRONG':break
    if resp=='CENTER':continue
    xlhigh=gx
    xllow=-10**9
    while xlhigh!=xllow:
        sprint((xlhigh+xllow)//2,gy)
        resp=input()
        if resp=='CENTER' or resp=='WRONG':break
        if resp=='HIT':
            xlhigh=(xlhigh+xllow)//2
        else:
            xllow=(xlhigh+xllow)//2+1
    if resp=='WRONG':break
    if resp=='CENTER':continue
    ylhigh=gy
    yllow=-10**9
    while ylhigh!=yllow:
        sprint(gx,(ylhigh+yllow)//2)
        resp=input()
        if resp=='CENTER' or resp=='WRONG':break
        if resp=='HIT':
            ylhigh=(ylhigh+yllow)//2
        else:
            yllow=(ylhigh+yllow)//2+1
    if resp=='WRONG':break
    if resp=='CENTER':continue
    xrhigh=10**9
    xrlow=gx
    while xrhigh!=xrlow:
        sprint((xrhigh+xrlow+1)//2,gy)
        resp=input()
        if resp=='CENTER' or resp=='WRONG':break
        if resp=='HIT':
            xrlow=(xrhigh+xrlow+1)//2
        else:
            xrhigh=(xrhigh+xrlow+1)//2-1
    if resp=='WRONG':break
    if resp=='CENTER':continue
    yrhigh=10**9
    yrlow=gy
    while yrhigh!=yrlow:
        sprint(gx,(yrhigh+yrlow+1)//2)
        resp=input()
        if resp=='CENTER' or resp=='WRONG':break
        if resp=='HIT':
            yrlow=(yrhigh+yrlow+1)//2
        else:
            yrhigh=(yrhigh+yrlow+1)//2-1
    if resp=='WRONG':break
    if resp=='CENTER':continue
    sprint((xllow+xrlow)//2,(yllow+yrlow)//2)
    resp=input()
    if resp!='CENTER':
        eprint('Huh?')
        break
