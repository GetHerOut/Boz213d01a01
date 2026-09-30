class Ogrenci:
    def __init__(self, ad, vize, final):
        self.ad = ad
        self.vize = vize
        self.final = final

    def ortalama(self):
        return (self.vize * 0.4) + (self.final * 0.6)

    def durum(self):
        ort = self.ortalama()
        if ort >= 50:
            print(f"\nSonuc: {self.ad} {ort:.1f} ortalama ile GECTI.")
        else:
            print(f"\nSonuc: {self.ad} {ort:.1f} ortalama ile KALDI.")

# Programın doğrudan çalışması için kullanıcıdan bilgi alıyoruz:
print("--- OGRENCI NOT VE DURUM HESAPLAYICI ---")
ad = input("Ogrenci Adi: ")
vize = float(input("Vize Notu: "))
final = float(input("Final Notu: "))

ogr = Ogrenci(ad, vize, final)
ogr.durum()

# Pencere anında kapanmasın diye bekletme satırı:
input("\nCikmak icin Enter'a basiniz...")