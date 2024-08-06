#refresher

constant = 100
checkcount = int(input("Insert value  here:"))

newMsg = " Welcome to"
hotelName = "  Bedford Hotel"

#string manipulations

str1 = "Jeremy"
str2 = "Lans"
result1= str1 + " " + str2
result2 = len(result1)
errormsg = "Name too long"

def combinestring():
    if checkcount > result2:
        return errormsg
    else:
        return result1

result2 = combinestring()


#slicing 

#print(result2[0:5])
#print(result2[-5])
#print(result2[6:])

#capitalize and uppper with white space removal 

strippedMsg1 = newMsg.strip() 
strippedMsg2 = hotelName.strip()
newMsg3= (strippedMsg1 + " " + strippedMsg2)
#print(newMsg3.upper())


#find and replace 

newWord = "Fish in the lake"
newTrans = "hook in the pond"

neword2 = newWord.find("lake")
newTrans2 = newTrans.replace("lake","pond")
#print(neword2, newTrans2)

# reverse the string output 
 
reversednew4 = newTrans2[::-2]
#print(reversednew4)

#advanced string manipulation 

import re 

text = "She sells sea shells by the sea show, the sea shells that she sells by the sea show are sea shells am sure"
pattern = r"\bin\b"
matches = re.findall(pattern,text)
#print(matches)

new_text = re.sub(r"she\b", "xyz", text)
#print(new_text)

#creating a list of squares 

squarelist = [x **2 for x in range(100) ]
#print(squarelist)
evensquares = [x**2 for x in range(10) if x % 2  == 0]
#print(evensquares)

matrix1 = [[j for j in range(3)] for i in range(3)]
#rint(matrix1)

#list slicing 

mylist = [0,1,2,3,4,5,6,7,8,9]
reveversedlist = mylist[::-1]
#print(reveversedlist)

#skip list 
skiplist= mylist[::2]
#print(skiplist)

# slice this list 

slicedlist= mylist[:2]
#print(slicedlist)

poppedlist = mylist.pop()
insertlist = mylist.append(1.7)
removelist = mylist.remove(4)
insertlistpos = mylist.insert(3,1.8)

#print(mylist)

#hnadling disctionaries 

mydic= {
    "name": "Jeremy",
    "age" : 30,
    "loaction" :"New York"
}

#print(mydic["name"])

for key in mydic.keys():
    #print(key)

#tuples 

 t = (1,2,3,4,5,6,7,8)
 #print(t.count(5))

def somethingCool(a,b,c):
   return min(a),max(c),len(b)


t = (1,2,3,4,5,5)

a,b,c,d,e,f = t

#print(a)

#recursion

def thisRecursion(n):
   if n == 0:
      return 1
   else:
      return n * thisRecursion(n-1)
   
#print(thisRecursion(5))

#write some fibonacci 

def thisFibonnaci(n):
   if n == 0:
      return 0 
   elif n == 1:
      return 1
   else:
      return thisFibonnaci(n-1) + thisFibonnaci(n-2)
   
#print(thisFibonnaci(6))

#getting the latest element in the array


stack = []

firstElement = stack.append(4)
secondElement = stack.append(5)
thirdElement = stack.append(6)
fourthElement = stack.insert(2,9)

#print(stack)

# Queue operarions 

class Queue:
   def _init_(self):
      self.queue= []

   def isEmpty(self):
      return len(self.queue) == 0
   
   #def enqueue(self, item):
   #   return self.queue.append(item)
   

   def dequeue(self):
      if self.isEmpty():
         raise IndexError ("Empty from an empty array")
      else:
         return self.dequeue.pop(0)
      
   def peek(self):
      if self.isEmpty():
         raise IndexError ("Peek from an empty queue")
      else:
        return  self.queue.peek[0]
      

   def size(self):
      return len(self.queue)
   


#print(q.size())

#Circular queue 


#Graphs 

#build an adjacsncy matrix with a 2D array

import numpy as np

myArray = np.array([
   [0,1,2,3,8,6],
   [2,3,4,5,6,6],
   [5,6,3,2,5,8],
   [4,2,7,1,8,4]
])

#print(myArray)

#Adjacency lists 

myAdList = {
   0: [3,4,2,7],
   1: [3,5,4,1],
   3: [1,0,5,6],
   4: [6,7,5,9,]
}

#print(myAdList)


#Binary tree implementation (each node has at least 2 children)

class Node:
   def __init__(self,key):
      self.left = None
      self.right = None
      self.value = key







































