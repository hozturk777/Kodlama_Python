class Math:
    def __init__(self, sayi1, sayi2): #constructor
        self._sayi1 = sayi1
        self._sayi2 = sayi2
        print("ref")

    def topla(self):
        return self._sayi1 + self._sayi2

    def cikar(self):
        return self._sayi1 - self._sayi2 


math = Math(3, 4)
topla = math.topla()
cikar = math.cikar()
print(f"Toplama : {topla} Çıkarma : {cikar}")
