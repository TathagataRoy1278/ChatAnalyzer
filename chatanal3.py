import chatanalyzer as c
import chatanal2 as ca2
ca2.run(c.name1,c.name2)
a = open(c.name1+" chats with "+c.name2+".txt",encoding = "utf8")
stri = a.read()
l = stri.split("\n")
ctr = 0
li = []
ctr = 0
mat = [c.name1,c.name2]
tmp = ""
f=0
str = ""
ct = 0
try:
    while(True):        
        if(l[ct].startswith(mat[ctr%2])):
            if f == 0:
                tmp += mat[ctr%2]+":"
                f=1
            tmp += l[ct][l[ct].index(mat[ctr%2])+len(mat[ctr%2])+2:]
            ct = ct+1
        else:
            st = tmp
            if(st!=""):
                li.append((st+"\n"))
            ctr = ctr+1
            tmp = ""
            f=0
            ct = ct+1
except:
    pass
print(li)
k = open("corrected.txt","w+",encoding = "utf8")
k.write("".join(li))
