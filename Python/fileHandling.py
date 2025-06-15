#reading a file
semFile=open("sem.txt","r") #r=read w=write r+=read and write both a=append
print(semFile.readable()) #checks if file is readdable or not
print(semFile) #details of file
#print(semFile.read()) # reads the complete content of file
# print(semFile.readline()) #reads each line by line
# print(semFile.readline())
print(semFile.readlines()) #form an array of each line
semFile.close() #closes the file

#writing a file
semFile=open("sem.txt","a") #if we use w it changes the complete file
semFile.write("\nRoh:144") #for a new line \n
semFile.close()