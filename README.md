# BOZ213d01a01-KettleKontrolProgrami
[TR]
# Kettle Kontrol Programı 
Bu program, su ısıtıcısının durumunu gösteren basit bir simülasyondur.

## Özellikler
-Kettle'a su koyma
-Kettle'ı çalıştırma(su varsa)
-Kettle'ı tehlike oluşturcak bir durum varsa kapatma(su yoksa)
-Kettle'ın durumunu kontrol etme/ekrana yazdırma

## Sınıf ve Metotlar
'__init__()' -- Kettle'ın baştaki durumunu söyler
'su_koy()' -- Kettle'a su koyar, zaten varsa durumu söyler
'calistir()' -- Kettle'ı su varsa çalıştırır, su yoksa durumu söyler
'kapat()' -- Kettle'ı kapatır, zaten kapalıysa durumu söyler
'durumu_kontrol_et() -- Kettle durumunu söyler, su var/yok ve kettle açık/kapalı

## Nasıl Çalıştırılır
1. Bilgisayarına Python'u kur.
2. Bu repoyu indir.
3. Terminalde proje klasörüne şunu yaz: python kettle.py

[EN]
# Kettle Control Program 
This program is a simple simulation that displays the status of a kettle.

## Features
- Add water to the kettle
- Turn on the kettle (if there is water)
- Turn off the kettle if a dangerous situation arises (if there is no water)
- Check the kettle's status and display it on the screen
  
## Classes and Methods
‘__init__()’ -- Reports the kettle’s initial state
‘fill_with_water()’ -- Fills the kettle with water; if there is already water, reports the current state
‘start()’ -- Starts the kettle if there is water; if there is no water, reports the current state
‘stop()’ -- Stops the kettle, If it's already off, it reports the status
'check_status() -- Reports the kettle's status: water present/absent and kettle on/off

## How to Run It
1. Install Python on your computer.
2. Download this repo.
3. In the terminal, type the following in the project folder: python kettle.py


## Yazar
Ruhan Sadef USTA - 25040221 - BÖTE 2.Sınıf 
