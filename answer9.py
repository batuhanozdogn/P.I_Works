import random
#rastgele yeni bir tür oluşturacağımız için random ekledik


#belirtilen özelliklere göre sınıf oluşturduk
#__init__ niye kullandık sınıfın örnekleri oluşturulduğunda ilk çağrılan metodudur.
#self ise o anki örenğin özellklerine erişmek için kullandık
class Animal:
    def __init__(self, tür, cinsiyet, x, y):
        self.tür = tür
        self.cinsiyet = cinsiyet
        self.x = x
        self.y = y
#kaç birim hareket edeicekerini yazdık koordinatta
#move ile hareket etmelerini sağladık hayvanların
# konumunu, -1 ile 1 arasında rastgele bir sayı kadar değiştirir(ranndom.randit ile). anlamına gelir. Yani, hayvanın yatayda (sağa-sola) nasıl hareket ettiğini düşünün.
#X yatayda Y dikey koordinatlarında
    def move(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

#hayvanların başlangıç sayılarını ve içinde hareket edecekleri sınırları yazdık sonra bunları hayvanlar sınıfınfa ekledik
#yeni_hayvan adlı bu fonksiyon, başlangıçta boş bir liste olan hayvanlar listesini oluşturur. Ardından, bu listeye farklı türlerde ve cinsiyetlerde hayvanlar ekler.
def yeni_hayvan():
    hayvanlar = []

    for i in range(15):
        hayvanlar.append(Animal("Koyun", random.choice(["Erkek", "Dişi"]), random.randint(0, 499), random.randint(0, 499)))

    for i in range(5):
        hayvanlar.append(Animal("Inek", random.choice(["Erkek", "Dişi"]), random.randint(0, 499), random.randint(0, 499)))

    for i in range(0, 10, 5):
        cinsiyet = random.choice(["Dişi", "Erkek"])
        hayvan_turu = random.choice(["Tavuk", "Horoz"])
        if hayvan_turu == "Tavuk":
            cinsiyet = "Dişi"
        else:
            cinsiyet = "Erkek"
        hayvanlar.append(Animal(hayvan_turu, cinsiyet, random.randint(0, 499), random.randint(0, 499)))

    for i in range(5):
        hayvanlar.append(Animal("Horoz", "Erkek", random.randint(0, 499), random.randint(0, 499)))

    for i in range(5):
        hayvanlar.append(Animal("Kurt", random.choice(["Erkek", "Dişi"]), random.randint(0, 499), random.randint(0, 499)))

    for i in range(4):
        hayvanlar.append(Animal("Aslan", random.choice(["Erkek", "Dişi"]), random.randint(0, 499), random.randint(0, 499)))

    for i in range(8):
        hayvanlar.append(Animal("Avcı", "Erkek", random.randint(0, 499), random.randint(0, 499)))

    return hayvanlar
#öklid cinsinden mesafeyi hesapladık iki hayvan arasındaki mesafeyi hesapladık
def distance(hayvan1, hayvan2):
    return ((hayvan1.x - hayvan2.x) ** 2 + (hayvan1.y - hayvan2.y) ** 2) ** 0.5

# -------------Avcının belirli türdeki hayvanları avlamasını sağlayan fonksiyon.
def avlandi(yeni_hayvanlar, avci, avlanacak_türler, mesafe):
    avlandi = False # avlanamaz olasılığı
    for hayvan in yeni_hayvanlar:
        if hayvan.tür in avlanacak_türler and distance(avci, hayvan) <= mesafe: #Her hayvanın türü, avlanacak_türler listesindeki türlerden biri mi kontrol edilir ve hayvanın avcıya olan mesafesi mesafe değerinden küçük veya eşit mi kontrol edilir.
            yeni_hayvanlar.remove(hayvan) # # Avlanan hayvanı listeden kaldır
            yeni_hayvanlar.append(Animal(hayvan.tür, random.choice(["Erkek", "Dişi"]), random.randint(0, 499), random.randint(0, 499)))

            avlandi = True
            break
    return avlandi

#reproduce kullanrak hayvanların üremesini sağladık  aynı cins farklı tür üremeyi sağladık 3 birim yaklaştığında
#soruda verilen diğer bir trick horoz ve tavuk diye iki farklı tür hayvan varmış gibi  halbuki ikiside aynı tür bunuda üremede ortadan kaldırdık :)

def reproduce(hayvan1, hayvan2):
    if hayvan1.tür == hayvan2.tür and distance(hayvan1, hayvan2) <= 3 and hayvan1.cinsiyet != hayvan2.cinsiyet:
        if hayvan1.tür == "Tavuk":
            if hayvan2.tür == "Horoz":
                return Animal("Tavuk", random.choice(["Dişi"]), hayvan1.x, hayvan1.y)
            elif hayvan2.tür == "Tavuk":
                return Animal("Horoz", random.choice(["Erkek"]), hayvan1.x, hayvan1.y)
    else:
        return None


def simulate(hayvanlar, adım):
    for i in range(adım):
        for hayvan in hayvanlar:
            hayvan.move()
            hayvan.x = max(0, min(hayvan.x, 499))
            hayvan.y = max(0, min(hayvan.y, 499))

        yeni_hayvanlar = []

        for hayvan in hayvanlar:
            if hayvan.tür == "Kurt" and not avlandi(yeni_hayvanlar, hayvan, ["Koyun", "Tavuk", "Horoz"], 4):
                yeni_hayvanlar.append(Animal("Kurt", random.choice(["Erkek", "Dişi","Tavuk","Horoz"]), random.randint(0, 499), random.randint(0, 499)))

            elif hayvan.tür == "Aslan" and not avlandi(yeni_hayvanlar, hayvan, ["Inek", "Koyun"], 5):
                yeni_hayvanlar.append(Animal("Aslan", random.choice(["Erkek", "Dişi"]), random.randint(0, 499), random.randint(0, 499)))

            for hayvan in hayvanlar:
                if hayvan.tür == "Avcı":
                    avlanacak_türler = ["Aslan", "Kurt", "Koyun", "Tavuk", "Horoz", "Inek"]
                    avlanacak_hayvanlar = [i for i in hayvanlar if i.tür in avlanacak_türler]

                    if avlanacak_hayvanlar:
                        avlanan_hayvan = random.choice(avlanacak_hayvanlar)
                        hayvanlar.remove(avlanan_hayvan)
                        yeni_hayvanlar.append(
                            Animal(avlanan_hayvan.tür, avlanan_hayvan.cinsiyet, random.randint(0, 499),
                                   random.randint(0, 499)))

        hayvanlar.extend(yeni_hayvanlar)


        #başlangıç değerlerini ekledik
if __name__ == "__main__":
    hayvanlar_listesi = yeni_hayvan()
    tür_sayilari = {"Koyun": {"Erkek": 15, "Dişi": 15},
                    "Inek": {"Erkek": 5, "Dişi": 5},
                    "Tavuk": {"Dişi": 10},
                    "Horoz": {"Erkek": 10},
                    "Kurt": {"Erkek": 5, "Dişi": 5},
                    "Aslan": {"Erkek": 4, "Dişi": 4},
                    "Avcı": 1}

    tür_sayilari_son = {tür: {cinsiyet: 0 for cinsiyet in cinsiyet_sayilari} if isinstance(cinsiyet_sayilari, dict) else cinsiyet_sayilari for tür, cinsiyet_sayilari in tür_sayilari.items()}

    print("BAŞLANGIÇ HAYVANAT BAHÇESİ HAYVAN SAYILARI:")
    for tür, cinsiyet_sayilari in tür_sayilari.items():
        if isinstance(cinsiyet_sayilari, dict):
            for cinsiyet, sayi in cinsiyet_sayilari.items():
                print(f"{tür} - {cinsiyet}: {sayi}")
        else:
            print(f"{tür}: {cinsiyet_sayilari}")

    simulate(hayvanlar_listesi, 5)

    for hayvan in hayvanlar_listesi:
        if hayvan.tür != "Avcı":
            if hayvan.tür not in tür_sayilari_son:
                tür_sayilari_son[hayvan.tür] = {}
            if hayvan.cinsiyet not in tür_sayilari_son[hayvan.tür]:
                tür_sayilari_son[hayvan.tür][hayvan.cinsiyet] = 0
            tür_sayilari_son[hayvan.tür][hayvan.cinsiyet] += 1

    print("\nSON HAYVANAT BAHÇESİ HAYVAN SAYILARI:")
    for tür, cinsiyet_sayilari in tür_sayilari_son.items():
        if isinstance(cinsiyet_sayilari, dict):
            for cinsiyet, sayi in cinsiyet_sayilari.items():
                print(f"{tür} - {cinsiyet}: {sayi}")
        else:
            print(f"{tür}: {cinsiyet_sayilari}")
