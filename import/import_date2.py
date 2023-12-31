#weekday komutu günleri 0dan başlatır.
#isoweekday komutu 1den başlatır.

from datetime import date

gecmis_tarih= date(2017,9,25)

print(gecmis_tarih.weekday())
print(gecmis_tarih.isoweekday())

