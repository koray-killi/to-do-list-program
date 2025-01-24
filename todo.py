# The To-Do List Program  by koraykilli
# Date: 2025-01-23
# Objective: Re-using and praticing most important python and programing skills.

task_list = [] # Task list for using in import/export/editing etc.

#This functions for more readability.
def red_yaz(x):
    return print(f"\033[31m{x}\033[0m")
def green_yaz(x):
    return print(f"\033[32m{x}\033[0m")
# The 'Gorev' class for tasks.
class Gorev():
    id = 0
    def __init__(self,isim,aciklama,durum):
        self.id = Gorev.id
        Gorev.id+=1
        self.isim = isim
        self.aciklama = aciklama
        self.durumr = durum
        self.durum = (True if durum == "True" else False)
        self.durumd = ("Tamamlandı" if self.durum == True else "Tamamlanmadı")
    def tamamla(self):
        self.durum = True
        self.durumr = "True"
        self.durumd = "Tamamlandı"
        green_yaz(f"'{self.isim}' isimli görev tamamlandı!")
#Import function to read tasks.txt via open built-in function and converting it to 'task_list' list.        
def ice_aktar():
    with open("tasks.txt","r",encoding='utf-8') as tasks:
        for i in tasks.readlines():
            temp_list = i.strip().split(",")
            task_list.append(Gorev(temp_list[0],temp_list[1],temp_list[2]))
    return
ice_aktar()
# Programs functions
def gorev_ekle():
    isim_girdi = input("Lütfen eklenecek görevin adını yazınız: ")
    aciklama_girdi = input("Lütfen eklenecek görevin açıklamasını giriniz: ")
    if isim_girdi == "" or aciklama_girdi == "":
        return red_yaz("HATA: Boş bırakılan alanları lütfen doldurunuz!")
    task_list.append(Gorev(isim_girdi,aciklama_girdi,"False"))
    return green_yaz(f"{isim_girdi} isimli görev başarıyla eklendi.")
def gorev_goruntule():
    print("ID\tGörev Adı\tGörev Açıklaması\tGörev Durumu")
    for i in task_list:
        print(f"{i.id}\t{i.isim}\t{i.aciklama}\t{i.durumd}")
def görev_tamamlandi():
    try:
        secim = int(input("Lütfen tamamlanmış görevin ID'sini giriniz: "))
    except ValueError:
        return red_yaz("HATA: Lütfen geçerli ID giriniz!")
    try:
        task_list[secim].tamamla()
    except Exception:
        return red_yaz("HATA: Lütfen geçerli ID giriniz!")
    return
def gorev_sil():
    try:
        secim = int(input("Lütfen silinecek görevin ID'sini giriniz: "))
    except ValueError:
        return red_yaz("HATA: Lütfen geçerli ID giriniz.")
    try:
        del task_list[secim]
        green_yaz(f"{secim} ID'li görev başarıyla silindi.")
    except Exception:
        red_yaz("HATA: Lütfen geçerli ID giriniz!")
def disa_aktar_ve_cik():
    with open("tasks.txt","w", encoding='utf-8') as tasks:
        for i in task_list:
            tasks.write(f"{i.isim},{i.aciklama},{i.durumr}\n")
    try:
        return exit()
    except Exception:
        print("Hata.")

# UI and Main menu which is recursively loop itself.
print("To-Do List Programına Hoş geldiniz! -- by koray")
def liste():
    print("1. Görev Ekle\n2. Görevleri Görüntüle\n3. Görev Tamamlandı Olarak İşaretle\n4. Görev Sil\n5. Çıkış")
    secim = input("Lütfen Seçiminizi Yapınız: ")
    if secim == "1":
        gorev_ekle()
        return liste()
    elif secim == "2":
        gorev_goruntule()
        return liste()
    elif secim == "3":
        görev_tamamlandi()
        return liste()
    elif secim == "4":
        gorev_sil()
        return liste()
    elif secim == "5":
        disa_aktar_ve_cik()
    else:
        red_yaz("HATA: Geçerli işlem seçiniz.")
        return liste()
liste()