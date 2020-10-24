def countSetBits(n): 
	count = 0
	while n: 
		count+=1
		n &=(n-1) 
	return count 

def FlippedCount(a , b): 
	return countSetBits(a^b) 

x, y = input().split()
a=int(x)
b=int(y)
print(FlippedCount(a,b)) 
nums-]