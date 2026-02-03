f=open("myphoto.jpg","rb")
f1=open("newpic.jpg","wb")
for i in f:
    f1.write(i)
f1=open("newpic.jpg","rb")
print(f1.read())
f.close()
f1.close()