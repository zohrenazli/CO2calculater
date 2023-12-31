a=float(input("Yıllık ortalama kaç ton tekstil ürünü satın alıyorsunuz?"))
#Üretilen her bir ton tekstil başına, 0.002 ton CO2 havaya salınıyor.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
tekstilCO2salınımı=a*0.002
print("CO2 salınımı:",tekstilCO2salınımı)

b=float(input("Yıllık yükettiğiniz fosil yakıt(doğalgaz,kömür vb.) miktarı ne kadardır?"))
#Tüketilen her bir m3 fosil yakıt için havaya 50,95 ton CO2 salınıyor.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
fosilCO2salınımı=b*50.95
print("CO2 salınımı:",fosilCO2salınımı)

c=float(input("Yıllık tükettiğiniz elektrik enerjisi ne kadardır?"))
#Bir insanın yıllık tükettiği elektrik için 8.75 ton CO2 salınıyor.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
elektrikCO2salınımı=c*8.75
print("CO2 salınımı:",elektrikCO2salınımı)

d=float(input("İnsanlar barınma ihtiyacı için betonarme yapılara ihtiyaç duyarlar. Birey olarak toplumda barınma ihtiyacınızı karşılamak için kaç ton çimento sarfiyatında bulunuyorsunuz?"))
#Bir insanın yıllık çimento sarfiyatı için yıllık 0.829215 ton CO2 salınıyor.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
çimentoCO2salınımı=d*0.829215
print("CO2 salınımı:",çimentoCO2salınımı)

e=float(input("Yıllık tükettiğiniz et(küçükbaş/büyükbaş) miktarı ne kadardır?"))
#Bir insanın yıllık ortalama tükettiği et miktarı başına 0.8 ton CO2 salınıyor.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
etCO2salınımı=e*0.8
print("CO2 salınımı:",etCO2salınımı)

f=float(input("Yıllık ortalama ne kadar miktar plastik ürün satın alıyorsunuz?"))
#Bir insanın yıllık satın aldığı plastik ton başına 136.875 ton CO2 sarfiyatına sebep olur.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
plastikCO2salınımı=f*136.875
print("CO2 salınımı:",plastikCO2salınımı)

g=float(input("Yıllık ortalama kaç ton kağıt tüketiyorsunuz?"))
#Yıllık tüketilen 1 ton kağıt başına ortalama 0.084 ton CO2 salınıyor.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
kağıtCO2salınımı=g*0.084
print("CO2 salınımı:",kağıtCO2salınımı)

h=float(input("Yıllık ortalama tükettiğiniz su miktarı nedir?"))
#Bir insanın yıllık tükettiği 1 ton su başına 1272 ton CO2 salınımına sebep olur.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
suCO2salınımı=h*1272
print("CO2salınımı",suCO2salınımı)

i=float(input("Yıllık ortalama market alışverişlerinizde ne kadar plastik poşet kullanıyorsunuz?"))
#Bir insanin bir yılda kullandığı 1 ton plastik poşet başına 4.9 ton CO2 salınıyor.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
poşetCO2salınımı=i*4.9
print("CO2salınımı",poşetCO2salınımı)

j=float(input("Yıllık ne kadar deniz ürünü tüketiyorsunuz?"))
#Bir insanın yıllık ortalama tükettiği deniz ürünü ton başına 11.5 ton CO2 salınımına sebep olur.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
denizürünüCO2salınımı=j*11.5
print("CO2salınımı",denizürünüCO2salınımı)

k=float(input("Yıllık ne kadar tarımsal gıda tüketimi gerçekleştiriyorsunuz?"))
#Bir insanın yıllık ortalama tükettiği tarımsal gıda ton başına 4.25 CO2 salınımına sebep olur.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
tarımCO2salınımı=k*4.25
print("CO2salınımı",tarımCO2salınımı)

while True:
    leh=input("Kozmetik ürün kullanıyor musunuz (evet/hayır)?")
    if leh=="evet":
        l=float(input("Yıllık ortalama ne kadar miktar kozmetik ürün satın alıyorsunuz? "))
        #Yıllık ortalama kişisel bakım için aldığımız ürünler 0.6 ton CO2 sarfiyatına sebep olur.
        #CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
        kozmetikCO2salınımı=l*0.6
        print("CO2 salınımı:",kozmetikCO2salınımı)
        break
    elif leh=="hayır":
        kozmetikCO2salınımı=0
        print("CO2 salınımı:",kozmetikCO2salınımı)
        break
    else:
        print("Yalnızca evet ya da hayır şeklinde değer giriniz.")

m=float(input("Yıllık ortalama seyahatlerinizde kaç kere uçağı tercih ediyorsunuz?"))
#Bir uçağın tek bir uçuşta yaptığı ortalama CO2 salınımı 0.25 CO2'dir.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
uçakCO2salınımı=m*0.25
print("CO2salınımı",uçakCO2salınımı)

n=float(input("Yıllık ortalama kişisel bakımınız için ne kadar miktar ürün kullanıyorsunuz?"))
#Yıllık ortalama kişisel bakım için aldığımız ürünler 0.6ton co2 sarfiyatına sebep olur.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
kişiselbakımCO2salınımı=n*0.6
print("CO2salınımı",kişiselbakımCO2salınımı)

x=(input("Ulaşım için kullandığınız araç tipi nedir(dizel veya benzinli)?"))
if x=="benzinli":
 y=float(input("Kullanmış olduğunuz araç ile ortalama kaç km yolculuk yapıyorsunuz?"))
 #Benzinli araç ortalama olarak 1 kilometre başına 0.0023 ton CO2 salınımına neden oluyor.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
 araçCO2salınımı=y*0.0023
 print("CO2salınımı",araçCO2salınımı)
elif x=="dizel":
 y=float(input("Kullanmış olduğunuz araç ile ortalama kaç km yolculuk yapıyorsunuz?"))
 #Dizel araç ortalama olarak 1 kilometre başına 0.0027 ton CO2 salınımına neden oluyor.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
 araçCO2salınımı=y*0.0027
 print("CO2salınımı",araçCO2salınımı)
else:
 print("Geçersiz araç tipi. Lütfen benzinli veya dizel olarak giriniz.")

o=float(input("Yıllık ortalama ne kadar pil tüketiyorsunuz(kg değerinde ifade giriniz.)?"))
#Bir lityum-iyon pilin yaşam döngüsü boyunca ortalama olarak 0.15 ton CO2 salınımına sebep olur.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
pilCO2salınımı=o*0.15
print("CO2salınımı",pilCO2salınımı)

p=float(input("Yıllık ne kadar tek kullanımlık saklama araç gereçlerini(kağıt bardak,plastik servis eşyaları,streç fil vb.) kullanıyorsunuz?"))
#Yıllık olarak evimizde tek kullanımlık kullandığımız plastim atıklar 0.041 ton co2 salınımına sebep olur.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
tekkullanımlıkCO2salınımı=p*0.041
print("CO2salınımı",tekkullanımlıkCO2salınımı)

while True:
  reh=input("Yıl içerisinde herhangi bir ormancılık faaliyetinde bulunuyor musunuz?(evet/hayır)")
  if reh=="evet":
    r=float(input("Yılda kaç tane ağaç dikiyorsunuz?"))
    #Bir ağaç yılda ortalama 0.02 ton CO2 absorbe eder.#CO2 Eşdeğeri (ton) = Miktar (ton) x Küresel Isınma Potansiyeli (GWP)
    ağaçCO2absorbansı=-r*0.02
    print("CO2absorbansı",ağaçCO2absorbansı)
    break
  elif reh=="hayır":
    ağaçCO2absorbansı=0
    print("Bir ağaç yılda ortalama 0.02 ton CO2 absorbe eder.Yıllık olarak olabildiğince ağaçlandırma faaliyetinde bulunmanızı öneririz :)")
    break
  else:
    print("Yalnızca evet ya da hayır şeklinde değer giriniz.")

TOPLAMCO2AYAKİZİ=tekstilCO2salınımı+fosilCO2salınımı+elektrikCO2salınımı+çimentoCO2salınımı+etCO2salınımı+plastikCO2salınımı+kağıtCO2salınımı+suCO2salınımı+poşetCO2salınımı+denizürünüCO2salınımı+tarımCO2salınımı+kozmetikCO2salınımı+uçakCO2salınımı+kişiselbakımCO2salınımı+araçCO2salınımı+pilCO2salınımı+tekkullanımlıkCO2salınımı+ağaçCO2absorbansı
print("Toplam CO2 Ayak İzi",TOPLAMCO2AYAKİZİ)

#CO2 Ayak İzi Dağılımı için Sütun Grafiği

import matplotlib.pyplot as plt

#Her bir kategori için veriler
Kategoriler=["Tekstil", "Fosil", "Elektrik", "Çimento", "Et", "Plastik", "Kağıt", "Su", "Poşet", "Deniz Ürünü", "Tarım", "Kozmetik", "Uçak", "Kişisel Bakım", "Araç", "Pil", "Tek Kullanımlık", "Ağaç"]
Veriler = [
    tekstilCO2salınımı, fosilCO2salınımı, elektrikCO2salınımı, çimentoCO2salınımı, etCO2salınımı, 
    plastikCO2salınımı, kağıtCO2salınımı, suCO2salınımı, poşetCO2salınımı, denizürünüCO2salınımı, 
    tarımCO2salınımı, kozmetikCO2salınımı, uçakCO2salınımı, kişiselbakımCO2salınımı, araçCO2salınımı, 
    pilCO2salınımı, tekkullanımlıkCO2salınımı, ağaçCO2absorbansı]
#Grafiği düzenle
plt.figure(figsize=(10, 6))
plt.bar(Kategoriler,Veriler,color='blue')

plt.xlabel('Kategoriler')
plt.ylabel('CO2 Salınımı (ton)')
plt.title('Yıllık CO2 Ayak İzi Dağılımı')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Display the plot
plt.show()