
x=[]
print(" enter 5 elements in set A\n")
for i in range(0,5):
	x.append(int(input()))
	
setA = set(x)
x.clear()	
print(" enter 5 elements in set B\n")
for i in range(0,5):
	x.append(int(input()))
	
setB = set(x)

print(" union of sets \n")
print(setA | setB)

print(" intersection of sets \n")
print(setA & setB)

print(" difference of sets \n")
print(setA - setB)

print(" symmetric difference of sets \n")
print(setA.symmetric_difference(setB))

