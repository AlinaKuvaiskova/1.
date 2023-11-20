def F(n):
   if n==1 or n==2:
       return 1
   else:
       return F(n-2)+ F(n-1)
 
n=int(input("n="))
print(F(n+2)-1)
