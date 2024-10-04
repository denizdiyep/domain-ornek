# Alan adlarını küçük harfe çeviren fonksiyon
def lowercase_domains(*domains):
    # Gelen tüm domainleri küçük harfe çevirir ve liste olarak döner
    return [domain.lower() for domain in domains]

# Alan adları
domain1 = "EXAMPLE1.COM"
domain2 = "example2.com"
domain3 = "ExAmPlE3.cOm"
domain4 = "TEST4.COM"
domain5 = "test5.com"
domain6 = "TeSt6.Com"
domain7 = "DOMAIN7.COM"
domain8 = "domain8.com"
domain9 = "DoMaIn9.Com"
domain10 = "SAMPLE10.COM"
domain11 = "sample11.com"
domain12 = "SaMpLe12.cOm"
domain13 = "SITE13.COM"
domain14 = "site14.com"
domain15 = "SiTe15.CoM"
domain16 = "WEB16.COM"
domain17 = "web17.com"
domain18 = "WeB18.cOm"
domain19 = "ADDRESS19.COM"
domain20 = "address20.com"

# Fonksiyonu çağırarak tüm domainleri küçük harfe çevirme
lowercase_domains_list = lowercase_domains(
    domain1, domain2, domain3, domain4, domain5,
    domain6, domain7, domain8, domain9, domain10,
    domain11, domain12, domain13, domain14, domain15,
    domain16, domain17, domain18, domain19, domain20
)

# Küçük harfe çevrilmiş domainleri yazdırma
for domain in lowercase_domains_list:
    print(domain)