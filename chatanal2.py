def run(name1,name2):
    a = open(name1+" chats with "+name2+".txt",encoding="utf8")
    stri = a.read()
    g = stri
    ctr = 0
    for i in range(1,len(g)-1):
        try:
            if stri[ctr-1]==stri[ctr]=='\n' or (stri[ctr] == "\n" and stri[ctr-1] == ""):
                tmp = list(stri)
                tmp[ctr] = ""
                stri = "".join(tmp)
            else:
                ctr=ctr+1
        except:
            pass
    b = open(name1 +" chats with "+name2+".txt","w+",encoding = "utf8")
    b.write(stri)
