# str1="PAYPALISHIRING"
# k=1
# n=3
# count=0
# count1=1
# count2=1
# zigzag=[[0,0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
# # print(zigzag)
# # print('Rows',len(zigzag))
# # print('Columns',len(zigzag[0]))
# strli=[x for x in str1]
# for i in range(0,n,2):
#     for j in range(0,n):
#         if(j!=n):
#             zigzag[i][j]=strli[count]
#             count+=1
#         else:
#             zigzag[count1][count2]=strli[count]
#             count+=1
#             count1+=2
#             count2+=2
# print(zigzag)
n=121
rev=0
while(n > 0): 
            a = n % 10
            rev = rev * 10 + a 
            n = n // 10
# if(n==rev):
#     print("True")
# else:
#     print("False")
print(n)