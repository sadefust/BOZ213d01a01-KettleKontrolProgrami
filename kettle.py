Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Kettle:

    def __init__(self):
        self.su_var_mi = False
        self.acik_mi = False

    def su_koy(self):
        if self.su_var_mi:
            print("Kettle'da zaten su var.")
        else:
            self.su_var_mi = True
...             print("Kettle'a su koyuldu.")
... 
...     def calistir(self):
...         if not self.su_var_mi:
...             print("UYARI: Kettle'da su yok! Önce su koymalısın.")
...         elif self.acik_mi:
...             print("Kettle zaten çalışıyor.")
...         else:
...             self.acik_mi = True
...             print("Kettle çalıştırıldı, su ısınıyor...")
... 
...     def kapat(self):
...         if self.acik_mi:
...             self.acik_mi = False
...             print("Kettle kapatıldı.")
...         else:
...             print("Kettle zaten kapalı.")
... 
...     def durum_kontrol_et(self):
...         print("--- Kettle Durumu ---")
... 
...         if self.su_var_mi:
...             print("Su: Var")
...         else:
...             print("Su: Yok")
... 
...         if self.acik_mi:
...             print("Kettle AÇIK! Kapatmayı unutma!")
...         else:
...             print("Kettle kapalı, içiniz rahat olsun.")
... 
... 
... if __name__ == "__main__":
...     kettle = Kettle()
...     kettle.calistir()        
...     kettle.su_koy()
...     kettle.calistir()
...     kettle.durum_kontrol_et()
...     kettle.kapat()
