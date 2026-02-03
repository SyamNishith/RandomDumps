'''f=open("file_handling1.txt","r")#to open the files
#print(f.read())#to read all the content
print(f.readline(),end="#")#to read line by line.
f1=open("syamnishith","w")# if we dont have a file with filename it will create a new file.
f1.write("hello")#write is just to write data into file it will not save
f1=open("syamnishith","a")#append mode is used to add data to file
f1.write(" how are you")#we can copy data from one file to another file as well
for data in f:
    f1.write(data)'''
f2=open("REDBULL.jpg","rb")
'''print(f2.read())'''
f3=open("newphoto2.jpg","wb")
for i in f2:
    f3.write(i)


