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
#V1 4
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
#V1 4(2)
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


    #V4 2. Koostage programmi plokkskeem, et arvutada ainult negatiivsete P antud arvude summa.
vastus=0
P=int(input("Mitu korda kordame?"))
while True:
    arv=float(input("Sisesta arv: "))
    if arv<0: vastus+=arv
    P-=1
    if P==0: break
print("Summa on: ",vastus)

vastus=0
P=int(input("Mitu korda kordame?"))
for i in range(P):
    arv=float(input("Sisesta arv: "))
    if arv<0: vastus+=arv
print("Summa on: ",vastus)
#V1 4.(3) Koostage plokkskeem kotlette praadiva roboti jaoks.
kokku=int(input("Kokku kotlete: "))
panni_maht=int(input("Panni maht: "))
aeg=1
lahenemine=kokku//panni_maht
jaak=kokku%panni_maht
if jaak>0: lahenemine+=1
print(f"Praeme. Tuleb {lahenemine} lahenemist.")
for l in range(lahenemine):
    if jaak>0 and l==lahenemine-1:
        print(f"Panni peal on {jaak} kotlet.")
    else:
        print(f"Panni peal on {panni_maht} kotlet.")
    print(f"{l+1}. lahenemine. Praeme esimene pool.")
    sleep(aeg)
    print("Ümberpöörame")
    print(f"{l+1}. lahenemine. Praeme teine pool.")
    sleep(aeg)
    print(f"Valmis!")

print("Kõik kotletid on praetud!")

#V4 3 ül
T = int(input("Sisesta sõprade arv: "))
loendur = 0

for i in range(T):
    vanus = int(input(f"Sõbra {i + 1} vanus: "))
    if vanus > 16:
        loendur += 1

print(f"Õhtusöögile pääseb {loendur} sõpra.")
