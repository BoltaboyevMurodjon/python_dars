#7.  Butun N vа K sonlаri berilgаn. Quyidаgi yig’indini toping 
# N2 + (N+1)2 + (N+2)2+……+ (N+K)2

n = int(input("N:"))
k = int(input("K:"))
s=0
for m in range(0,k+1):
    s+=(n+m)**2
print(s)

# 4.2 misol

toplam = {2.3,5.9,6.6,6.3}
s=0
for n in toplam:
    k=(round(n))
    s += k
    print(k)
print(f"yigindisi {s}") 
