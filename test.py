aa=[]
ab=[]
ac=[]
print("the fisrt matrix")
for u in range(1,4):
    print("enter the numbers of ",u,"colum")
    if u==1:
        for i in range(3):
            a=eval(input())
            aa.append(a)
    if u==2:
        for i in range(3):
            a=eval(input())
            ab.append(a)
    if u==3:
        for i in range(3):
            a=eval(input())
            ac.append(a)
print("the second matrix")
ba=[]
bb=[]
bc=[]
for l in range(1,4):
    print("enter the numbers of ",l,"colum")
    if l==1:
        for k in range(3):
            b=eval(input())
            ba.append(b)
    if l==2:
        for k in range(3):
            b=eval(input())
            bb.append(b)
    if l==3:
        for k in range(3):
            b=eval(input())
            bc.append(b)
ca=[]
cb=[]
cc=[]

order=str(input("enter the opreation you want(collection,subtracوmultiply,turn,value,invesre)"))
if order=="collection":
    for h in range(3):
        c=aa[h]+ba[h]
        ca.append(c)
    for j in range(3):
        c=ab[j]+bb[j]
        cb.append(c)
    for k in range(3):
        c=ac[k]+bc[k]
        cc.append(c)
    print(ca)
    print(cb)
    print(cc)
elif order=="subtract":
    for h in range(3):
        c=aa[h]-ba[h]
        ca.append(c)
    for j in range(3):
        c=ab[j]-bb[j]
        cb.append(c)
    for k in range(3):
        c=ac[k]-bc[k]
        cc.append(c)
    print(ca)
    print(cb)
    print(cc)
elif order=="multiply":
    for t in range(3):
        c=(aa[0]*ba[t])+(aa[1]*bb[t])+(aa[2]*bc[t])
        ca.append(c)
    for p in range(3):
        c=(ab[0]*ba[p])+(ab[1]*bb[p])+(ab[2]*bc[p])
        cb.append(c)
    for o in range(3):
        c=(ac[0]*ba[o])+(ac[1]*bb[o])+(ac[2]*bc[o])
        cc.append(c)
    print(ca)
    print(cb)
    print(cc)
elif order=="turn":
    ca=[aa[0],ab[0],ac[0]]
    cb=[aa[1],ab[1],ac[1]]
    cc=[aa[2],ab[2],ac[2]]
    print(ca)
    print(cb)
    print(cc)

elif order=="value":
    x=(aa[0](ab[1]*ac[2]-ab[2]*ac[1])-(aa[1](ab[0]*ac[2]-ab[2]*ac[0]))+(aa[2](ab[0]*ac[1]-ab[1]*ac[0])))
    print(x)

elif order=="inverse":
    x=(aa[0](ab[1]*ac[2]-ab[2]*ac[1])-(aa[1](ab[0]*ac[2]-ab[2]*ac[0]))+(aa[2](ab[0]*ac[1]-ab[1]*ac[0])))
    a=((ab[1]*ac[2])-(ab[2]*ac[1]))
    b=-((ab[0]*ac[2])-(ab[2]*ac[0]))
    c=((ab[0]*ac[1])-(ab[1]*ac[0]))
    d=-((aa[1]*ac[2])-(aa[2]*ac[1]))
    v=((aa[0]*ac[2])-(aa[2]*ac[0]))
    n=-((aa[0]*ac[1])-(aa[1]*ac[0]))
    m=(aa[1]*ab[2])-(aa[2]*ab[1])
    s=-((aa[0]*ab[2])-(aa[2]*ab[0]))
    f=((aa[0]*ab[1])-(aa[1]*ab[0]))
    z=1/x
    a=a*z
    b=b*z
    c=c*z
    d=d*z
    v=v*z
    n=n*z
    m=m*z
    s=s*z
    f=f*z
    ca.append(a)
    cb.append(b)
    cc.append(c)
    ca.append(d)
    cb.append(v)
    cc.append(n)
    ca.append(m)
    cb.append(s)
    cc.append(f)
    print(ca)
    print(cb)
    print(cc)