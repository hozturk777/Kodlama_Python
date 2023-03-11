faiz = 1.50
vade = 35
krediAdi = "Araç Kredisi"

print(type(krediAdi))

#input
vade = 3 #int(input("Lütfen vade miktarı seçiniz : "))
print("Vade miktarınız : ", vade)
print("")

#.format
vade = 2 #input("lütfen vade gir : ")
print("Seçtiğiniz vade : {vadeSayisi}".format(vadeSayisi=vade))

isim = "Hüseyin"
soyisim = "Öztürk {name}".format(name = isim)
print(soyisim)
print("")

#f-string
metin = f"Hoşgeldin {1 + 1}"
print(metin)


#List
krediler = ["denem", 2]
for x in range(len(krediler)):
    print(krediler[x])

#List_append(eleman ekler)
krediler.append("Özel")
print(krediler[-1])

#List_pop(eleman silme)
krediler.pop(0)
for x in krediler:
    print(x)

#List_extend
krediler.extend(["denem1", "deneme2"])

#for
for i in range(len(krediler)):
    print(krediler[i])
for i in krediler:
    print(i)

x = int(input())
for y in range(x, 10):
    print(y)

vade = "12"
vade = int(vade) +12
print(vade) 


#While
while x < len(krediler):
    print(krediler[x])
    x += 1


#function
def calculate(sayi1, sayi2):
    sum = sayi1 + sayi2
    average = sum / 2
    return average

x = 20
y = 10
average = calculate(x, y)
print(average)