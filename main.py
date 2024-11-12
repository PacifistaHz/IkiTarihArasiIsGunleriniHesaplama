import datetime
baslangic=input("Başlangıç giriniz (dd.mm.yyyy şeklinde giriniz): ")
bitis=input("Bitis giriniz (dd.mm.yyyy şeklinde giriniz): ")
baslangic=datetime.datetime.strptime(baslangic,"%d.%m.%Y")
bitis=datetime.datetime.strptime(bitis,"%d.%m.%Y")

fark = bitis-baslangic
haftaSonu = 0
haftaIci = 0

while baslangic <= bitis:
    if baslangic.weekday() in [5,6]:
        haftaSonu+=1
    else:
        haftaIci+=1
    baslangic=baslangic+datetime.timedelta(days=1)

print("Hafta içi çalışma günleri: {0}".format(haftaIci))
print("Hafta sonu tatil günleri: {0}".format(haftaSonu))