def kilo_hesapla():
 
 kilo = float(input("Kilonuzu Giriniz: "))

 print()

 boy = float(input("Boyunuzu Giriniz: "))

 print("-------------------------------")

 indeks = boy / kilo

 if indeks >=2.2 and indeks <= 2.5:
  print("Zayıfsınız.")

 elif indeks >2.5:
   print("Aşırı zayıfsınız.")

 elif indeks <= 1.8 and indeks >= 1.5:
  print("Şişmansınız.")

 elif indeks < 1.5:
   print("Aşırı şişmansınız.")

 elif indeks >= 1.8 and indeks <= 2.2:
  print("Normal kilodasınız.")

 print()

 cevap = input("Devam etmek istiyor musunuz? (E/H): ")

 if cevap == "E" or cevap == "e":
    print()
    print("===============================")
    kilo_hesapla()

 else:
    print("Görüşürüz!")   

kilo_hesapla()
