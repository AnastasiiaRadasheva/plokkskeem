#V5 3. rühm 20
for õ in range(20):
    print(f'soritab eksamit {õ+1} õpilane')
    for e in range(3):
        print(f'{e+1}eksam')
#V4
p=int(input('mitu korda kordame?'))
vastus=0
while True:
    arv=float(input('sisesta arv '))
    if arv<0:
        vastus+=arv
    p-=1
    if p == 0:
        print(f'vastus on {vastus}')
        break
V1 4
try:
    K = int(input("skok koklet: "))
    M = int(input("skok pomestitsja na skovorodku: "))

    if M < 0:
        print("viga")
    else:
        skokmesta = (K + M - 1) // M 
        print(f"nado {skokmesta} skovorodok")
        ostanetsja =K%M
        print(f"na skovorodke ostanetsja {ostanetsja} mesta")
except:
    print("viga ")
#V1 4
skokmesta = 0
kokku = 100
panni_maht= 6 
aeg= 1
try:
    if kokku < -1:
        print("viga")
    else:
        skokmesta = ( kokku + panni_maht - 1) // panni_maht
        print(f"nado {skokmesta} podhodov")
except:
    print("viga ")