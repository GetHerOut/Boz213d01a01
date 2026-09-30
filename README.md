# Boz213d0ta01
# Öğrenci Not ve Geçme Durumu Hesaplayıcı (Python OOP)

Bu proje, Python'da Nesne Yönelimli Programlama (OOP) mantığını kullanarak bir öğrencinin vize ve final notları üzerinden ağırlıklı ortalamasını ve dersi geçme durumunu hesaplayan temel bir uygulamadır.

## Ne İşe Yarar?
- Öğrenciye ait ad, vize ve final notu bilgilerini bir nesne çatısı altında tutar.
- Not ortalamasını **%40 Vize + %60 Final** formülüyle hesaplar.
- Ortalamanın **50 ve üzeri** olması durumunda öğrencinin dersi geçtiğini (`GEÇTİ`), 50'nin altında kalması durumunda ise kaldığını (`KALDI`) ekrana yazdırır.

## Kullanım

Projeyi klonladıktan veya dosyayı indirdikten sonra Python ortamında doğrudan çalıştırabilirsiniz:

```python
# Yeni bir öğrenci nesnesi oluşturma (Ad, Vize, Final)
ogr1 = Ogrenci("Ahmet", 40, 70)

# Durum ve ortalamayı ekrana yazdırma
ogr1.durum()
