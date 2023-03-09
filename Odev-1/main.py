
print("Question #1")
x = str("Hello World")      #string değer tutar
x = int(20)     #integer değer tutar
x = float(20.5)     #ondalıklı integer değer tutar
x = complex(1j)     #karmaşık sayı tutar
x = list(("Hello", "World"))        #list halinde birden fazla değer tutar
x = True        #boolean yani true false 


print("Question #2")
#Ders tarihleri string değer
#Ders tamamlama oranı integer değer

print("Question #3")
#İlgili ödevi bitir ve devam et butonuna basıldığın da tamamlama oranının artması
dersOrani = 0
tamamlamaTrue = True

if tamamlamaTrue:
    print("Tamamlandı",dersOrani + 10)
elif dersOrani == 10:
    print("ders zaten işlenilmiş")
else:
    print("Lütfen dersi tamamlayın")

