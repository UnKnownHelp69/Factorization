n=int(input())

prime=""
i=2

while i*i<=n:
    
    while n % i == 0:
        
        prime+=str(i)+" "
        n//=i
    
    i+=1

if n>1:
    prime+=str(n)

print(prime)