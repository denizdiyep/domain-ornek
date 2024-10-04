import locale

# Türkçe yerelleştirme
locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')

# Alan adlarını küçük harflere çeviren fonksiyon
def to_lowercase(domain):
    return domain.lower()

# Alan adları
domains = [
    "TEKNOLOJI.COM", "teknoloji.com", "TeKnoLoJi.cOm",
    "KITAPLIK.COM", "kitaplik.com", "KiTaPlIk.CoM",
    "EĞİTİM.COM", "egitim.com", "EgItIm.cOm",
    "SAĞLIK.COM", "saglik.com", "SaGlIk.CoM",
    "YEMEKTARİFİ.COM", "yemektarifi.com", "YeMeKTaRiFi.CoM",
    "OYUNLAR.COM", "oyunlar.com", "OyUnLaR.cOm",
    "SİTE.COM", "site.com"
]

# Küçük harflere çevrilmiş sonuçlar
for domain in domains:
    print(to_lowercase(domain))
    
