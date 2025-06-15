#intro to lists (more like arrays lol)
friends=["AAS","AB","AP","TD","TG"] #0 , 1, 2 
print(friends) #complete list
print(friends[4]) #last element
print(friends[-1]) #also last element
print(friends[1:]) #prints the elements from index 1 to end
print(friends[1:3]) #prints from element 1 to the element before 3

#We can modify list
friends[2]="AM"
print(friends)

#functions for list
friends.append("AP") #Add element at the end of the list
friends.insert(1,"Bolbona") #inserts at the index and movs the rest to next index respectively
print(friends)
friends.remove("Bolbona") #removes the element
print(friends)
#friends.clear() #empties the list
#print(friends)
#friends.pop() #removes the last element
#print(friends)
#friends.count("AAS") #counts the number of times AAS occured
friends.sort() #ascending order or like dictionary
print(friends)
friends.reverse() #reverses the list
print(friends)
luckyNums=[4,8,15,16,23,42]
friends2=friends.copy() #to copy a list
print(friends2)