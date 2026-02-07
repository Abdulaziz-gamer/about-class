# 1-masala
#-----------------------------------------------------------------------------------
# class Transpotr:
#     def __init__(self, model: str,  yil: int) -> None:
#         self.model = model
#         self.yil = yil
#
#     def malumot(self):
#         return f"Model: {self.model} Yil: {self.yil}"
#
# class Avtomobil(Transpotr):
#     def __init__(self, model: str, yil: int, yonilgi_turi: str) -> None:
#         super().__init__(model, yil)
#         self.yonilgi_turi = yonilgi_turi
#
#     def malumot(self):
#         baza = super().malumot()
#         return f"Model: {baza} Yil: {self.yonilgi_turi}"
#
# class Avtobus(Transpotr):
#     def __init__(self, model: str, yil: int, orinlar_soni: int) -> None:
#         super().__init__(model, yil)
#         self.orinlar_soni = orinlar_soni
#
#     def malumot(self):
#         baza = super().malumot()
#         return f"{baza}, O'rinlar: {self.orinlar_soni}"
#
# a = Avtomobil("Cobalt", 2024, "metan")
# print(a.malumot())
#
# b = Avtobus("Isuzu", 2018, 36)
# print(b.malumot())
#-----------------------------------------------------------------------------------
# 2-masala
#-----------------------------------------------------------------------------------
# class Kitob:
#     def __init__(self, nom: str, muallif: str, yil: int):
#         self.nom = nom
#         self.muallif = muallif
#         self.yil = yil
#
#     def taqdimot(self):
#         return f"{self.nom} {self.muallif} {self.yil}"
#
# class Elektronkitob(Kitob):
#     def __init__(self, nom: str, muallif: str, yil: int, fayl_hajmi_mb: float):
#         super().__init__(nom, muallif, yil)
#         self.fayl_hajmi_mb = fayl_hajmi_mb
#
#     def taqdimot(self):
#         baza = super().taqdimot()
#         return f"{baza} {self.fayl_hajmi_mb}"
#
# class Audiokitob(Kitob):
#     def __init__(self, nom: str, muallif: str, yil: int, davomiylik_soat: float):
#         super().__init__(nom, muallif, yil)
#         self.davomiylik_soat = davomiylik_soat
#
#     def taqdimot(self):
#         baza = super().taqdimot()
#         return f"{baza} {self.davomiylik_soat}"
#
# a = Elektronkitob("Python asoslari", "Ali", 2023, 5)
# b = Audiokitob("O'tkan kunlar", "Abdulla Qodiriy", 2020, 12)
#
# print(a.taqdimot())
# print(b.taqdimot())
#-----------------------------------------------------------------------------------
# 3-masala
#-----------------------------------------------------------------------------------
# class Xodim:
#     def __init__(self, ism: str, asosiy_maosh: int):
#         self.ism = ism
#         self.asosiy_maosh = asosiy_maosh
# 
#     def oylik(self):
#         return f"{self.ism} {self.asosiy_maosh}"
#     
#     def malumot(self):
#         return f"{self.ism} {self.asosiy_maosh}"
# 
# class Oqsoch(Xodim):
#     def __init__(self, ism: str, asosiy_maosh: int, bonus_foiz: float):
#         super().__init__(ism, asosiy_maosh)
#         self.bonus_foiz = bonus_foiz
# 
# class SoatbayXodim(Xodim):
#     def __init__(self, ism, asosiy_maosh, soat, soatlik_stavka):
#         super().__init__(ism, asosiy_maosh)
#         self.soat = soat
#         self.soatlik_stavka = soatlik_stavka
#         self.soat = None
#         self.soatlik_stavka = None
# 
#     def hisobla_foiz(self):
#         return self.soat * self.soatlik_stavka / 100
#     
# 
# o = Oqsoch("Dilshod", 5_000_000, 20)
# s = SoatbayXodim("Aziza", soat=160, soatlik_stavka=50_000)
# 
# print(o.malumot())
# print(s.malumot())
#-----------------------------------------------------------------------------------
# 4-masala
#-----------------------------------------------------------------------------------

# class Mahsulot:
#     def __init__(self, nom: str, narx: int) -> None:
#         self.nom = nom
#         self.narx = narx
#
#     def chegirmali_narx(self, foiz: int):
#         chegirma = self.narx * foiz // 100
#         return self.narx - chegirma
#
# class Elektronika(Mahsulot):
#     def __init__(self, nom: str, narx: int, kafolat_oy: int) -> None:
#         super().__init__(nom, narx)
#         self.kafolat_oy = kafolat_oy
#
#     def malumot(self):
#         return f"Nom: {self.nom}, Narx: {self.narx}, Kafolat: {self.kafolat_oy} oy"
#
# class OziqOvqat(Mahsulot):
#     def __init__(self, nom: str, narx: int, yaroqlilik_kuni: str) -> None:
#         super().__init__(nom, narx)
#         self.yaroqlilik_kuni = yaroqlilik_kuni
#
#     def malumot(self):
#         return f"Nom: {self.nom}, Narx: {self.narx}, Yaroqlilik: {self.yaroqlilik_kuni}"
#
# telefon = Elektronika("Iphone", 15_000_000, 12)
# non = OziqOvqat("Non", 3000, 1)
# print(telefon.malumot())
# print(non.malumot())
#-----------------------------------------------------------------------------------
# 5-masala
#-----------------------------------------------------------------------------------

# class Shaxs:
#     def __init__(self, ism):
#         self.ism = ism
#
# class Talaba(Shaxs):
#     def __init__(self, ism, id_raqam):
#         super().__init__(ism)
#         self.id_raqam = id_raqam
#
# class ImtihonNatijasi(Talaba):
#     def __init__(self, ism, id_raqam, baholar):
#         super().__init__(ism, id_raqam)
#         self.baholar = baholar
#
#     def ortalama(self):
#         ortacha = sum(self.baholar) / len(self.baholar)
#         return ortacha
#
#     def status(self):
#         o = self.ortalama()
#         if o >= 86:
#             return "A'lo"
#         elif 71 <= o <= 86:
#             return "Yaxshi"
#         elif 56 <= o <= 70:
#             return "Qoniqarli"
#         else:
#             return "Qoniqarsiz"
#
# natija = ImtihonNatijasi("Abdulaziz", "IT001", [87, 95, 100])
#
# print(natija.ism)
# print(natija.id_raqam)
# print(natija.ortalama())
# print(natija.status())

# -----------------------------------------------------------------------------------
# 7-masala
# -----------------------------------------------------------------------------------

# class Hisob:
#     def __init__(self, raqam, egasi, balans):
#         self.raqam = raqam
#         self.balans = balans
#         self.egasi = egasi
# 
#     def kirim(self, summa):
#         self.balans += summa
# 
#     def chiqim(self, summa):
#         self.balans -= summa
# 
# class JamgArmaMixin:
#     def __init__(self):
#         self.balans = None
#         self.foiz_stavka = None
# 
#     def hisobla_foiz(self):
#         return self.balans * self.foiz_stavka / 100
# 
# class KiriditMixin:
#     def __init__(self):
#         self.limit = None
#         self.balans = None
# 
#     def chiqim(self, summa):
#         if self.balans - summa >= -self.limit:
#             self.balans -= summa
#         else:
#             print("Kiridit limiti oshib ketdi!")
# 
# class Viphisob(JamgArmaMixin, KiriditMixin, Hisob):
#     def __init__(self, raqam, egasi, balans, foiz_stavka, limit):
#         super().__init__(raqam, egasi, balans)
#         self.foiz_stavka = foiz_stavka
#         self.limit = limit
# 
# 
# 
# V = Viphisob("001", "Amirxon", 2_000_000, foiz_stavka=12, limit=2)
# 
# V.chiqim(10000000)
# print(V.balans)

# -----------------------------------------------------------------------------------
# 8-masala
# -----------------------------------------------------------------------------------

# class Taom:
#     def __init__(self, nom, narx):
#         self.nom = nom
#         self.narx = narx
#
#     def tavsif(self):
#         return f"Taom: {self.nom}, Narx: {self.narx}"
#
# class IssiqTaom(Taom):
#     def __init__(self, nom, narx, kaloriya):
#         super().__init__(nom, narx)
#         self.kaloriya = kaloriya
#
#     def tavsif(self):
#         return f"Taom: {self.nom}, Narx: {self.narx}, Kaloriya: {self.kaloriya}"
#
# class Ichimlik(Taom):
#     def __init__(self, nom, narx, hajm_ml):
#         super().__init__(nom, narx)
#         self.hajm_ml = hajm_ml
#
#     def tavsif(self):
#         return f"Taom: {self.nom}, Narx: {self.narx}, Hajm ML: {self.hajm_ml}"





# -----------------------------------------------------------------------------------
# 9-masala
# -----------------------------------------------------------------------------------

# from abc import ABC, abstractmethod
# from typing import List
#
# class JamoaAzo(ABC):
#     def __init__(self, ism):
#         self.ism = ism
#
#     @abstractmethod
#     def vazifa(self):
#         """Har bir rol uchun aniq vazifalarni qaytaradi"""
#         return NotImplementedError
#
# class Bakenddasturchi(JamoaAzo):
#     def vazifa(self):
#         return "API va ma'lumotlar bazasi bilan ishlaydi"
#
# class Fronteddasurchi(JamoaAzo):
#     def vazifa(self):
#         return "UI va foydalanuvchi interfeysini yaratadi"
#
# class Tester(JamoaAzo):
#     def vazifa(self):
#         return "tizimni test qiladi"
#
#     def hisobot(azolar: List[JamoaAzo]):
#         for azo in azolar:
#             print(f" ism: {azo.ism} vazifa: {azo.vazifa()}")
#
# Jamoa = [
#     Bakenddasturchi("Akmurod"),
#     Fronteddasurchi("Sherzod"),
#     Fronteddasurchi("Muhammadjon"),
#     Tester("Abdulaziz"),
# ]
#
# hisobot(Jamoa)