# def rvc(x):
# 	if(x<0):
# 		x=abs(x)
# 		lst=[int(i) for i in str(x)]
# 		s=[str(i) for i in lst[::-1]]
# 		return int("".join(s))*-1
# 	else:
# 		lst=[int(i) for i in str(x)]
# 		s=[str(i) for i in lst[::-1]]
# 		return int("".join(s))
# print(rvc(-123))

# def fsuqchar(s):
# 	lst=[i for i in str(s)]
# 	# return lst
# 	for j in range(0,len(lst)):
# 		if(s.count(lst[j])==1):
# 			return j
# print(fsuqchar("loveleetcode"))

# def anagram(s,t):
# 	if(len(s)!=len(t)):
# 		return False
# 	else:
# 		lst1=[x for x in s]
# 		lst2=[x for x in t]
# 		lst1.sort()
# 		lst2.sort()
# 		if(lst1==lst2):
# 			return True
# 		else: 
# 			return False

# print(anagram("car","nagaram"))


# def(l1,l2):
# 	n1=len(l1)
# 	n2=len(l2)
# a=[2,4,3]
# a=a[::-1]
# b=[5,6,4]
# b=b[::-1]
# strn1=[str(i) for i in a]
# strn2=[str(i) for i in b]
# res=int("".join(strn1))+int("".join(strn2))
# # print(res)
# res1=[int(x) for x in str(res)]
# print(res1[::-1])

# a=[1,1,0,1,1,1]
# cnt=0
# maxl=[]
# for i in range(0,len(a)):
# 	if(a[i]==1):
# 		cnt=cnt+1
# 		maxl.append(cnt)
# 	else:
# 		cnt=0
# 		maxl.append(cnt)
# print(max(maxl))

# nums=[12,345,2,6,7896]
# cnt=0
# for i in range(0,len(nums)):
# 	if((nums[i]>=10 and nums[i]<100) or (nums[i]>=1000 and nums[i]<=9999)):
# 		cnt+=1
# print(cnt)

# A=[-4,-1,0,3,10]
# A.sort()
# A1=[i**2 for i in A]
# A1.sort()
# print(A1)

# nums1=[1,2,3,0,0,0,0,0,0]
# nums2=[2,5,6]
# j=0
# n=len(nums1)-1
# if(len(nums2)!=0):
#     while(len(nums1)>2*len(nums2)):
#         nums1.pop()
# else:
#     for i in range(0,len(nums1)):
#         nums1[i]=nums1[i]
# # if(2*len(nums2)!=len(nums1)):
# #     len(nums1)=2*len(nums2)
# for i in range(0,len(nums1)):
#     if(nums1[i]==0):
#         nums1[i]=nums2[j]
#         j+=1
#     else:
#         nums1[i]=nums1[i]
# nums1.sort()
# print(nums1)

# nums=[1,2,3,4,4,4,4]
# n=len(nums)
# for i in range(0,n):
#     print("Hello")

# arr=[-2,0,10,-19,4,6,-8]
# # arr.sort()
# # m=len(arr)-1
# n=len(arr)-1
# sum=0
# for i in range(0,n):
#     for j in range(len(arr)-1,-1,-1):
#         if(arr[i]==2*arr[j]):
#             print("True")

# # for j in range(len(arr)-1,-1,-1):
# #     print(arr[j])

# nums=[17,18,5,4,6,1]
# n=len(nums)-1
# m=len(nums)
# for i in range(0,n):
#     arr=nums[i+1:m]
#     nums[i]=max(arr)
# nums[n]=-1
# return nums

# lst1=[]
# lst2=[]
# A=[3,1,2,4]
# for i in range(0,len(A)):
#     if(A[i]%2==0):
#         lst1.append(A[i])
#     else:
#         lst2.append(A[i])
# print(lst1+lst2)

# ht=[2, 2, 3, 1]
# ht=list(set(ht))
# # ht1=[]
# # ht2=[]
# # s_ht = sorted(ht)
# # pos = 0
# # for pos_old, pos_new in zip(ht, s_ht):
# #     if pos_old != pos_new:
# #         pos += 1
# #         ht1.append(pos_old)
# #         ht2.append(pos_new)
# ht.sort(reverse=True)
# print(ht[2])

# nums=[4,3,2,7,8,2,3,1]
# nums=list(set(nums))
# nums.sort()
# m=1
# ab=[]
# for i in range(0,len(nums)):
#     if(m in nums):
#         ab.append(m)
#         m+=1
# print(ab)

# str1="hello"
# str2="ell"
# lst1=[str(x) for x in str1]
# # print(lst1)
# lst3=[]
# lst2=[str(x) for x in str2]
# n=len(lst1)
# if(str2 in str1):
#     for i in range(0,n-1):
#         for j in range(0,len(lst2)-1):
#             if((lst1[i]==lst2[j])and(lst1[i+1]==lst2[j+1])):
#                 lst3.append(i)
#     return lst3[0]
# else:
#     return "-1"

# S1="words and 987"
# nums=['1','2','3','4','5','6','7','8','9','0','-']
# lst1=[x for x in S1]
# lst2=[]
# for i in range(0,len(lst1)):
#     if(lst1[i] in nums):
#         lst2.append(lst1[i])
# num=int("".join(lst2))
# print(num)


# a=[2, 3, 6, 6, 5]
# a=list(set(a))
# a.sort(reverse=True)

# a=[5,6,7]
# b=[3,6,10]
# cnt1=0
# cnt2=0
# c=a-b
# print(c)

# A = [[1, 4, 5], 
#     [-5, 8, 9],
#     [-6, 7, 11]]

# sum1=0
# sum2=0
# for i in range(0,len(A)):
#     for j in range(0,len(A)):
#         if(i==j):
#             sum1+=A[i][j]

# print(sum1)

# from pandas import *
# n=5
# rows,cols=(n,n)
# my_matrix = [([0]*cols) for i in range(rows)]
# # print(my_matrix)
# k=n
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==j):
#             my_matrix[i][j]='1'
#             k-=1
#         else:
#             my_matrix[i][j]='0'
        
# x=DataFrame(my_matrix)
# x.style.hide_index()
# print(x)

#left rotation
# import time

# a=[1,2,3,4,5]
# n=len(a)
# d=2
# t1=time.time()
# li1=a[d:n]+a[0:d]
# t2=time.time()
# print(t2-t1)
# print(li1)


#Compare triplets
# # a=[5,6,7]
# b=[3,6,10]
# alice=0
# bob=0
# for i,j in zip(a,b):
#     if(i>j):
#         alice+=1
#     elif(i<j):
#         bob+=1
#     else:
#         alice=alice
#         bob=bob

# print(alice,"",bob)

#Diag Difference
# import time
# a=[[11,21,1,1,4,41,1,1,5,6],[11,21,1,1,4,41,1,1,5,6],[11,21,1,1,4,41,1,1,5,6],[11,21,1,1,4,41,1,1,5,6],[11,21,1,1,4,41,1,1,5,6],[11,21,1,1,4,41,1,1,5,6],[11,21,1,1,4,41,1,1,5,6],[11,21,1,1,4,41,1,1,5,6],[11,21,1,1,4,41,1,1,5,6],[11,21,1,1,4,41,1,1,5,6]]
# sum1=0
# sum2=0
# k=len(a[0])-1
# # print(len(a[0]))
# t1=time.clock()
# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if(i==j):
#             sum1+=a[i][j]

# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if(j==k):
#             sum2+=a[i][j]
#             k-=1
# print('Time Taken',time.clock()-t1)
# # return abs(sum1-sum2)

# # print(sum1)
# # print(sum2)
# print(abs(sum1-sum2))

# a=[-4,3,-9,0,4,1]
# pos,neg,zer=(len([x for x in a if x > 0])/len(a),len([x for x in a if x < 0])/len(a),len([x for x in a if x == 0])/len(a))
# # print(format(pos/len(a),'.6f'),"\n",format(neg/len(a),'.6f'),"\n",format(zer/len(a),'.6f'))
# print(format(pos,".6f"),format(neg,".6f"),"\n",format(zer,".6f"))

# arr=[1,2,3,4,5]
# arr.sort()
# sum1=0
# sum2=0
# arr.sort()
# for i in range(0,len(arr)-1):
#     sum1+=arr[i]
# arr.sort(reverse=True)
# for i in range(0,len(arr)-1):
#     sum2+=arr[i]

# print(sum1)
# print(sum2)

# import re
# def isMatch(s:str,pat:str):
#     try:
#         expr = re.compile(f"^{pat}$")
#         return bool(expr.match(s))
#     except Exception:
#         return False

# print(isMatch("aa",".*"))
# nums=[73,67,38,33]
# for i in range(0,len(nums)):
#     if(nums[i]>38 and 5-(nums[i]%3)<3):
#         nums[i]=nums[i]+(5-(nums[i]%3))
#     else:
#         nums[i]=nums[i]


    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     for i in range(1,1000):
    #         if i not in nums:
    #             return i


# num=2.00000
# n=0
# prod=1
# if(n>0):
#     for i in range(1,n+1):
#         prod*=num
#     print(format(prod,'.5f'))    
# elif(n<0):
#     for i in range(0,abs(n)):
#         prod*=num
#     print(1.00000/prod)
# else:
#     print(1)

# for i in range(0,abs(n)):
#     prod*=num
# print(1.00000/prod)
# print(format(prod,'.5f'))

# li=[4,-1,2,1]
# sum1=0
# sumli=[]
# for i in range(0,len(li)):
#     j=i+4
#     sli=li[i:j]
#     for i in sli:
#         sum1+=i
#     sumli.append(sum1)
#     sum1=0
#     sli=[]
# print(max(sumli))

# path=[[1,3,1],[1,5,1],[4,2,1]]
# pathli=[]
# pathli.append(path[0][0])
# for i in range(0,len(path)-1):
#     for j in range(0,len(path)-1):
#         if(path[i+1][j]<path[i][j+1]):
#             pathli.append(path[i+1][j])
#         else:
#             pathli.append(path[i][j+1])
# pathli.append(path[len(path)-1][len(path)-1])
# print(pathli)

# path=[[1,3,1],[1,5,1],[4,2,1]]
# pathli=[]
# k,m=0,0
# pathli.append(path[k][m])
# for i in range(0,len(path)-1):
#     for j in range(0,len(path)-1):
#         if(i==len(path)-1):
#             pathli.append(path[i][j+1])
#             k,m=0,0
#             k,m=i,j+1
#         elif(j==len(path)-1):
#             pathli.append(path[i+1][j])
#             k,m=0,0
#             k,m=i+1,j
#         else:
#             if(path[k+1][m]<path[k][m+1]):
#                 pathli.append(path[k+1][m])
#                 k,m=0,0
#                 k,m=i+1,j
#             else:
#                 pathli.append(path[k][m+1])
#                 k,m=0,0
#                 k,m=i,j+1
# # pathli.append(path[len(path)-1][len(path)-1])
# # pathli.append(path[len(path)-1][len(path)-1])
# print(pathli)

# wordli=["leet","code"]
# str1="leetcode"
# strlst=[]
# str1li=[x for x in str1]
# wordstr=[]
# for i in range(0,len(str1li)):
#     strlst.append(str1li[i])
#     strc=""
#     for ele in strlst:
#         strc+=ele
#     if(strc in wordli):
#         print("True")
#         wordstr.append(strc)
#         strc=""
#     else:
#         print("False")
#         strc=""
#     for j in range(i+1,len(str1li)):
#         str2=str1li[i]+str1li[j]
#         strlst.append(str2)
# print(wordstr)
# print(strlst)

# # Reverse the words of the string.
# str1="Hello world"
# str2=""
# lst=str1.split()
# for words in lst[::-1]:
#     str2+=words
#     str2+=" "
# print(str2.lower())

# fibo
# Function for nth Fibonacci number

# FibArray = [0,1]
# def fibonacci(n)-> list:
# 	if n<=0:
# 		print("Incorrect input")
# 	elif n<=len(FibArray):
# 		return FibArray[n-1]
# 	else:
# 		temp_fib = fibonacci(n-1)+fibonacci(n-2)
# 		FibArray.append(temp_fib)
# 	return FibArray
# li=fibonacci(9)
# print(li)

# fibli=[-1]*6
# fibli[0]=0
# fibli[1]=1
# for i in range(2,6):
#     fibli[i]=fibli[i-2]+fibli[i-1]

#Climbing Stairs Dynamic Programming
# n=3
# dp=[None]*6
# dp[0]=1
# dp[1]=1
# # print(len(dp))
# for i in range(2,n+1):
#     dp[i]=dp[i-2]+dp[i-1]

# print(dp[n])

#Climbing stairs
# def stairs(n:int)->int:
#     dp=[]
#     for i in range(0,n+1):
#         dp.append(0)
#     dp[0],dp[1]=1,1
#     for i in range(2,n+1):
#         dp[i]=dp[i-1]+dp[i-2]
#     return dp[n]
# print(stairs(3))


# a=[[1,1,0],[1,0,1],[0,0,0]]
# for i in range(0,len(a)):
#     a[i]=a[i][::-1]

# # nums=[[1,1,1],[1,1,1],[1,1,1]]
# a=[e1-e2 for e1 in a for e2 in nums]
# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if(a[i][j]==0):
#             a[i][j]=1
#         else:
#             a[i][j]=0
# print(a)

# li=[-2,1,-3,4,-1,2,1,-5,4]
# sumli=[]
# sum1=0
# for i in range(0,len(li)):
#     # li1=li[i:i+4]
#     # sum1=sum(li1)
#     # sumli.append(sum1)
#     for j in range(i+1,len(li)):
#         li1=li[i:j]
#         sumli.append(sum(li1))
# print(sumli)

# houses=[2,7,9,3,1]
# sumli=[]
# sum1=0
# for i in range(0,len(houses)):
#     for j in range(i+2,len(houses)):
#         sum1+=sum([houses[i],houses[j]])
#         sumli.append(sum1)
# print(sumli)

#Best time to buy and sell the stock.















