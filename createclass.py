class   PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar
    
    def __str__(self):
        return f"Persegi Panjang, Panjang {self.panjang} cm, dan lebar {self.lebar} cm"
    

try:
    panjang_input = int(input("Masukkan panjang (cm):"))
    lebar_input = int(input("Masukkan lebar (cm):"))

    PP = PersegiPanjang(panjang_input, lebar_input)
    print("Keliling:", PP.keliling(), "cm")
    print("Luas:", PP.luas(), "cm²")

except:
    print("Input harus berupa angka.")