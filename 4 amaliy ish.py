#7.  Butun N vа K sonlаri berilgаn. Quyidаgi yig’indini toping 
# N2 + (N+1)2 + (N+2)2+……+ (N+K)2

n = int(input("N:"))
k = int(input("K:"))
s=0
for m in range(0,k+1):
    s+=(n+m)**2
print(s)
