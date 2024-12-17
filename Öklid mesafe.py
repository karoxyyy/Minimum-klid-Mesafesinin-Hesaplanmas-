
import math

# Öklid Mesafesi Hesaplayan Fonksiyon
def oklid_mesafesi(nokta1, nokta2):
    x1, y1 = nokta1
    x2, y2 = nokta2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Noktaların Tanımlanması
noktalar = [(1, 2), (3, 4), (5, 1), (6, 7)]

# Mesafeleri Saklamak İçin Liste
mesafeler = []

# Tüm Nokta Çiftleri Arasındaki Mesafelerin Hesaplanması
for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklid_mesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

# Minimum Mesafenin Bulunması
en_kısa_mesafe = min(mesafeler)

# Sonuçların Yazdırılması
print(f"Noktalar: {noktalar}")
print(f"Hesaplanan Mesafeler: {mesafeler}")
print(f"En Kısa Mesafe: {en_kısa_mesafe}")