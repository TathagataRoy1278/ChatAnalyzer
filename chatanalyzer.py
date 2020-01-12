import re
import chatanal2 as ca2
a = open("chat.txt", encoding = "utf8")
first = input()
second = input()
str = a.read()
str = re.sub("../../....","",str)
str = re.sub(".:.. .m - ","**&**",str)
in1 = str.index(first+":")
in2 = str.index(second+":")
ino = 0
inl = 0
if in1>in2:
    ino = in2
    inl = in1
else:
    ino = in1
    inl = in2

l = str.split("**&**")

name1 = ""
name2 = ""
if str.startswith("**&**"+first):
    name1 = first
    name2 = second
else:
    name1 = second
    name2 = first
li = []
ctr = 0
mat = [name1,name2]
tmp = ""
f = 0
for i in l:
    if(i.startswith(mat[ctr%2])):
        if f ==0:
            tmp += mat[ctr%2]+":"
            f=1
        tmp += i[i.index(mat[ctr%2])+len(mat[ctr%2])+2:].replace("\n"," ")
    else:
        st = tmp
        li.append((st+"\n"))
        ctr = ctr+1
        tmp = ""
        f=0
print(l)
fin = []
ctr = 0

g = open(name1+" chats with "+name2+".txt","w+",encoding = "utf8")
for i in range(int(len(li)/2)):
    fin.append([li[ctr],li[ctr+1]])
    ctr = ctr+2
for i in fin:
    g.write("".join(i))
'''
for i in li:
    print(i)
    print(":")'''
