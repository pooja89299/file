my_file=open("question3.txt","r")
for j in my_file:
    if "delhi" in j:
        a=open("delhi.txt","a")
        a.write(j)
    elif "shimla" in j:
        b=open("shimla.text","a")
        b.write(j)
    else:
        c=open("others.text","a")
        c.write(j)