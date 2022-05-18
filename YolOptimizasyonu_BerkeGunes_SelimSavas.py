import datetime
from math import *
import pandas as pd

Rota1 = {'A':0,'B':100,'C':175,'D':275,'E':350,'F':425,'O':450}
Rota1_donus = {'O':0,'F':25,'E':100,'D':175,'C':275,'B':350,'A':450}

Rota2 = {'G':0,'H':77,'I':159,'F':209,'J':306,'K':406,'L':518,'GBas':618}

Rota3 = {'N':0,'K':100,'P':200,'R':275,'D':325,'S':375,'PSon':450}
Rota3_donus = {'PSon':0,'S':75,'D':125,'R':175,'P':250,'K':350,'N':450}

sutun_isimleri = ['istasyon','KacinciKM','OrtalamaHiz','Varis','Cikis','BeklemeSüresi']
hizlitrentablo = pd.DataFrame(columns=sutun_isimleri)
hizlitrendonus = pd.DataFrame(columns=sutun_isimleri)

hizlitren_hiz = 200
hizlitrentablo['istasyon'] = Rota1.keys()
hizlitrentablo['KacinciKM'] = Rota1.values()
hizlitrentablo['OrtalamaHiz'] = hizlitren_hiz
hizlitrentablo['BeklemeSüresi'] = 15

hizlitrendonus['istasyon'] = Rota1_donus.keys()
hizlitrendonus['KacinciKM'] = Rota1_donus.values()
hizlitrendonus['OrtalamaHiz'] = hizlitren_hiz
hizlitrendonus['BeklemeSüresi'] = 15

sutun_isimleri = ['istasyon','KacinciKM','OrtalamaHiz','Varis','Cikis','BeklemeSüresi']
anahattrentablo = pd.DataFrame(columns=sutun_isimleri)
anahattrendonus = pd.DataFrame(columns=sutun_isimleri)

anahattren_hiz = 100
anahattrentablo['istasyon'] = Rota3.keys()
anahattrentablo['KacinciKM'] = Rota3.values()
anahattrentablo['OrtalamaHiz'] = anahattren_hiz
anahattrentablo['BeklemeSüresi'] = 20

anahattrendonus['istasyon'] = Rota3_donus.keys()
anahattrendonus['KacinciKM'] = Rota3_donus.values()
anahattrendonus['OrtalamaHiz'] = anahattren_hiz
anahattrendonus['BeklemeSüresi'] = 20

sutun_isimleri = ['istasyon','KacinciKM','OrtalamaHiz','Varis','Cikis','BeklemeSüresi']
yuktrentablo = pd.DataFrame(columns=sutun_isimleri)

yuktren_hiz = 75
yuktrentablo['istasyon'] = Rota2.keys()
yuktrentablo['KacinciKM'] = Rota2.values()
yuktrentablo['OrtalamaHiz'] = yuktren_hiz
yuktrentablo['BeklemeSüresi'] = 0


gun_sayisi = int(input("Kaç Günlük Sefer Planlaması İstiyorsunuz: "))
HT_sayisi = int(input("Hızlı Treni Sayısını Giriniz: "))
AT_sayisi = int(input("Anahat Treni Sayısını Giriniz: "))
YT_sayisi = int(input("Yuk Treni Sayısını Giriniz: "))


def seyahat_uret(gun_sayisi,HT_sayisi,AT_sayisi,YT_sayisi):
    
    sutun_isimleri = ['istasyon','KacinciKM','OrtalamaHiz','Varis','Cikis','BeklemeSüresi']
    tablo3 = pd.DataFrame(columns=sutun_isimleri)
    
    
# HİZLİ TREN BÖLÜMÜ
    Cikis_suresi = datetime.datetime(2022,5,17,0,0,0)
    hizlitren_genelbakimkm = 6000
    hizlitren_anlikkm = 0
    hizlitren_birseferkm = 450
    hizlitren_kazanc = 0
    
    Bitis_suresi = datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(days=gun_sayisi)
    print(Bitis_suresi)
    sefer_sayisi = gun_sayisi * 5
    
    # tren dagitimi
    
    if(HT_sayisi%2==0):
        solkalkan = HT_sayisi/2
        sagkalkan = HT_sayisi/2
    else:
        solkalkan = int(floor(HT_sayisi/2))
        sagkalkan = int(ceil(HT_sayisi/2))
        
    
    for i in range(int(solkalkan)):
        print("A-O Güzergahı")
        print("HT-",i+1)
        seferadi = "HT-"+ str(i+1) +"A-O Güzergahı"
        
        if(i != 0):
            Cikis_suresi = datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(minutes = 20*i)

        hizlitren_genelbakimkm = 6000
        hizlitren_anlikkm = 0
        hizlitren_birseferkm = 450
        
        for i in range(sefer_sayisi):
            hizlitrentablo['SeferAdi'] = seferadi
            
            hizlitren_anlikkm = hizlitren_anlikkm + hizlitren_birseferkm

            if(hizlitren_anlikkm>6000):
                print("BAKIM LAZIM")
                # Bakim süresi ekle
                hizlitrentablosu['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 12*60)
                hizlitren_anlikkm = 0


            #if(hizlitrentablo['Cikis'][6]>datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(days = ,ntgun_sayisi)):
               #break


            if(i==0):
                hizlitrentablo['Cikis'] = Cikis_suresi

            else:
                hizlitrentablo['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 120)

            for i in range(hizlitrentablo['istasyon'].count()):
                hizlitrentablo['SeferAdi'] = seferadi

                if i == 0:

                    hizlitrentablo.iloc[i,3] = None # Varis
                    hizlitrentablo.iloc[i,5] = None # Bekleme Suresi
                    

                else:
                    istasyon_mesafe = hizlitrentablo.iloc[i,1]-hizlitrentablo.iloc[i-1,1]
                    hizlitrentablo.iloc[i,3] = hizlitrentablo.iloc[i-1,4] + datetime.timedelta(minutes = istasyon_mesafe/hizlitrentablo.iloc[i,2]*60)
                    hizlitrentablo.iloc[i,4] = hizlitrentablo.iloc[i,3] + datetime.timedelta(minutes = hizlitrentablo.iloc[i,5])

            hizlitren_kazanc += 60000
            print("Kazanc: ", hizlitren_kazanc," TL")

            Cikis_suresi = hizlitrentablo.iloc[-1,4]

            hizlitrendonus['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 120)
            
            
            #print(hizlitrentablo[hizlitrentablo['istasyon']=='A'])
            
            
            print(hizlitrentablo)
            tablo3 = tablo3.append(hizlitrentablo)
            #print(tablo3)
            #print(hizlitren_anlikkm)


            hizlitren_anlikkm = hizlitren_anlikkm + hizlitren_birseferkm

            if(hizlitren_anlikkm>6000):
                print("BAKIM LAZIM")
                # Bakim süresi ekle
                hizlitrendonus['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 12*60)
                hizlitren_anlikkm = 0

            if(hizlitrendonus['Cikis'][6]>datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(days = gun_sayisi)):
                break

            for i in range(hizlitrendonus['istasyon'].count()):
                hizlitrendonus['SeferAdi'] = seferadi
                if i == 0:
                    hizlitrendonus.iloc[i,3] = None # Varis
                    #hizlitrendonus.iloc[i,4] = Cikis_suresi + datetime.timedelta(minutes = 120)
                    hizlitrendonus.iloc[i,5] = None # Bekleme Suresi

                else:
                    istasyon_mesafe = hizlitrendonus.iloc[i,1]-hizlitrendonus.iloc[i-1,1]
                    hizlitrendonus.iloc[i,3] = hizlitrendonus.iloc[i-1,4] + datetime.timedelta(minutes = istasyon_mesafe/hizlitrendonus.iloc[i,2]*60)
                    hizlitrendonus.iloc[i,4] = hizlitrendonus.iloc[i,3] + datetime.timedelta(minutes = hizlitrendonus.iloc[i,5])
            
            
            hizlitren_kazanc += 60000
            print("Kazanc: ", hizlitren_kazanc," TL")
            Cikis_suresi = hizlitrendonus.iloc[-1,4]


            print(hizlitrendonus)
            tablo3 = tablo3.append(hizlitrendonus)
            print(hizlitren_anlikkm)
          
        ## TERS İSTİKAMATTEN KALKAN TREN
        
        Cikis_suresi = datetime.datetime(2022,5,17,0,0,0)
        hizlitren_genelbakimkm = 6000
        hizlitren_anlikkm = 0
        hizlitren_birseferkm = 450
    
        sefer_sayisi = gun_sayisi * 5
        
        for i in range(int(sagkalkan)):
            print("O-A Güzergahı")

            print("HT-",i+1+int(sagkalkan))
            
            seferadi = "HT-"+ str(i+1+sagkalkan) +"O-A Güzergahı"


            if(i != 0):
                Cikis_suresi = datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(minutes = 20*i)
            
            hizlitren_genelbakimkm = 6000
            hizlitren_anlikkm = 0
            hizlitren_birseferkm = 450
            
            for i in range(sefer_sayisi):
                hizlitrendonus['SeferAdi'] = seferadi

                hizlitren_anlikkm = hizlitren_anlikkm + hizlitren_birseferkm

                if(hizlitren_anlikkm>6000):
                    print("BAKIM LAZIM SÜRME BENİ LA")
                    # Bakim süresi ekle
                    hizlitrendonus['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 12*60)
                    hizlitren_anlikkm = 0


                #if(hizlitrentablo['Cikis'][6]>datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(days = gun_sayisi)):
                   # break


                if(i==0):
                    hizlitrendonus['Cikis'] = Cikis_suresi

                else:
                    hizlitrendonus['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 120)

                for i in range(hizlitrendonus['istasyon'].count()):
                    hizlitrendonus['SeferAdi'] = seferadi

                    if i == 0:

                        hizlitrendonus.iloc[i,3] = None # Varis
                        hizlitrendonus.iloc[i,5] = None # Bekleme Suresi

                    else:
                        istasyon_mesafe = hizlitrendonus.iloc[i,1]-hizlitrendonus.iloc[i-1,1]
                        hizlitrendonus.iloc[i,3] = hizlitrendonus.iloc[i-1,4] + datetime.timedelta(minutes = istasyon_mesafe/hizlitrendonus.iloc[i,2]*60)
                        hizlitrendonus.iloc[i,4] = hizlitrendonus.iloc[i,3] + datetime.timedelta(minutes = hizlitrendonus.iloc[i,5])

                
                hizlitren_kazanc += 60000
                print("Kazanc: ", hizlitren_kazanc,' TL')
                Cikis_suresi = hizlitrendonus.iloc[-1,4]

                hizlitrentablo['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 120)

                print(hizlitrendonus)
                tablo3 = tablo3.append(hizlitrendonus)
                print(hizlitren_anlikkm)
                

                hizlitren_anlikkm = hizlitren_anlikkm + hizlitren_birseferkm

                if(hizlitren_anlikkm>6000):
                    print("BAKIM LAZIM")
                    # Bakim süresi ekle
                    hizlitrentablo['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 12*60)
                    hizlitren_anlikkm = 0

                if(hizlitrentablo['Cikis'][6]>datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(days = gun_sayisi)):
                    break

                for i in range(hizlitrentablo['istasyon'].count()):
                    hizlitrentablo['SeferAdi'] = seferadi
                    if i == 0:
                        hizlitrentablo.iloc[i,3] = None # Varis
                        #hizlitrendonus.iloc[i,4] = Cikis_suresi + datetime.timedelta(minutes = 120)
                        hizlitrentablo.iloc[i,5] = None # Bekleme Suresi

                    else:
                        istasyon_mesafe = hizlitrentablo.iloc[i,1]-hizlitrentablo.iloc[i-1,1]
                        hizlitrentablo.iloc[i,3] = hizlitrentablo.iloc[i-1,4] + datetime.timedelta(minutes = istasyon_mesafe/hizlitrendonus.iloc[i,2]*60)
                        hizlitrentablo.iloc[i,4] = hizlitrentablo.iloc[i,3] + datetime.timedelta(minutes = hizlitrentablo.iloc[i,5])
                
                
                
                hizlitren_kazanc += 60000
                print("Kazanc: ", hizlitren_kazanc,' TL')
                
                
                
                Cikis_suresi = hizlitrentablo.iloc[-1,4]


                print(hizlitrentablo)
                tablo3 = tablo3.append(hizlitrentablo)
                print(hizlitren_anlikkm)
                
# HİZLİ TREN BOLUMU BİTİS


# ANAHAT TREN BOLUMU
    
    Cikis_suresi = datetime.datetime(2022,5,17,0,0,0)
    anahattren_genelbakimkm = 2500
    anahattren_anlikkm = 0
    anahattren_birseferkm = 450
    anahattren_kazanc = hizlitren_kazanc
    
    sefer_sayisi = gun_sayisi * 7
    
    # tren dagitimi
    
    if(AT_sayisi%2==0):
        solkalkan = AT_sayisi/2
        sagkalkan = AT_sayisi/2
    else:
        solkalkan = int(floor(AT_sayisi/2))
        sagkalkan = int(ceil(AT_sayisi/2))
        
    
    for i in range(int(solkalkan)):
        print("N-P Güzergahı")
        print("AT-",i+1)
        
        seferadi = "AT-"+ str(i+1) +"N-P Güzergahı"
        anahattrentablo['SeferAdi'] = seferadi


        
        if(i != 0):
            Cikis_suresi = datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(minutes = 25*i)

        anahattren_genelbakimkm = 2500
        anahattren_anlikkm = 0
        anahattren_birseferkm = 450
        
        for i in range(sefer_sayisi):
            
            anahattren_anlikkm = anahattren_anlikkm + anahattren_birseferkm

            if(anahattren_anlikkm>2500):
                print("BAKIM LAZIM")
                # Bakim süresi ekle
                anahattrentablo['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 24*60)
                anahattren_anlikkm = 0


            #if(hizlitrentablo['Cikis'][6]>datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(days = gun_sayisi)):
               # break


            if(i==0):
                anahattrentablo['Cikis'] = Cikis_suresi

            else:
                anahattrentablo['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 4*60)

            for i in range(anahattrentablo['istasyon'].count()):

                if i == 0:

                    anahattrentablo.iloc[i,3] = None # Varis
                    anahattrentablo.iloc[i,5] = None # Bekleme Suresi

                else:
                    istasyon_mesafe = anahattrentablo.iloc[i,1]-anahattrentablo.iloc[i-1,1]
                    anahattrentablo.iloc[i,3] = anahattrentablo.iloc[i-1,4] + datetime.timedelta(minutes = istasyon_mesafe/anahattrentablo.iloc[i,2]*60)
                    anahattrentablo.iloc[i,4] = anahattrentablo.iloc[i,3] + datetime.timedelta(minutes = anahattrentablo.iloc[i,5])

            anahattren_kazanc += 45000
            print("Kazanc: ", anahattren_kazanc, ' TL')

            Cikis_suresi = anahattrentablo.iloc[-1,4]

            anahattrendonus['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 4*60)

            print(anahattrentablo)
            tablo3 = tablo3.append(anahattrentablo)
            print(anahattren_anlikkm)


            anahattren_anlikkm = anahattren_anlikkm + anahattren_birseferkm

            if(anahattren_anlikkm>2500):
                print("BAKIM LAZIM")
                # Bakim süresi ekle
                anahattrendonus['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 12*60)
                anahattren_anlikkm = 0

            if(anahattrendonus['Cikis'][6]>datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(days = gun_sayisi)):
                break

            for i in range(anahattrendonus['istasyon'].count()):
                if i == 0:
                    anahattrendonus.iloc[i,3] = None # Varis
                    #hizlitrendonus.iloc[i,4] = Cikis_suresi + datetime.timedelta(minutes = 120)
                    anahattrendonus.iloc[i,5] = None # Bekleme Suresi

                else:
                    istasyon_mesafe = anahattrendonus.iloc[i,1]-anahattrendonus.iloc[i-1,1]
                    anahattrendonus.iloc[i,3] = anahattrendonus.iloc[i-1,4] + datetime.timedelta(minutes = istasyon_mesafe/anahattrendonus.iloc[i,2]*60)
                    anahattrendonus.iloc[i,4] = anahattrendonus.iloc[i,3] + datetime.timedelta(minutes = anahattrendonus.iloc[i,5])
            
            
            anahattren_kazanc += 45000
            print("Kazanc: ", anahattren_kazanc,' TL')
            Cikis_suresi = anahattrendonus.iloc[-1,4]


            print(anahattrendonus)
            tablo3 = tablo3.append(anahattrendonus)
            print(anahattren_anlikkm)
          
        ## TERS İSTİKAMATTEN KALKAN TREN
        
        Cikis_suresi = datetime.datetime(2022,5,17,0,0,0)# + datetime.timedelta(minutes = 7.5)
        anahattren_genelbakimkm = 2500
        anahattren_anlikkm = 0
        anahattren_birseferkm = 450
    
        sefer_sayisi = gun_sayisi * 5
        
        for i in range(int(sagkalkan)):
            print("P-N Güzergahı")

            print("AT-",i+1+sagkalkan)
            
            seferadi = "AT-"+ str(i+1+sagkalkan) +"P-N Güzergahı"



            if(i != 0):
                Cikis_suresi = datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(minutes = 25*i)
            
            anahattren_genelbakimkm = 2500
            anahattren_anlikkm = 0
            anahattren_birseferkm = 450
            
            for i in range(sefer_sayisi):
                anahattrendonus['SeferAdi'] = seferadi


                anahattren_anlikkm = anahattren_anlikkm + anahattren_birseferkm

                if(anahattren_anlikkm>2500):
                    print("BAKIM LAZIM")
                    # Bakim süresi ekle
                    anahattrendonus['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 24*60)
                    anahattren_anlikkm = 0


                #if(hizlitrentablo['Cikis'][6]>datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(days = gun_sayisi)):
                   # break


                if(i==0):
                    anahattrendonus['Cikis'] = Cikis_suresi

                else:
                    anahattrendonus['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 4*60)

                for i in range(anahattrendonus['istasyon'].count()):
                    
                    if i == 0:

                        anahattrendonus.iloc[i,3] = None # Varis
                        anahattrendonus.iloc[i,5] = None # Bekleme Suresi

                    else:
                        istasyon_mesafe = anahattrendonus.iloc[i,1]-anahattrendonus.iloc[i-1,1]
                        anahattrendonus.iloc[i,3] = anahattrendonus.iloc[i-1,4] + datetime.timedelta(minutes = istasyon_mesafe/anahattrendonus.iloc[i,2]*60)
                        anahattrendonus.iloc[i,4] = anahattrendonus.iloc[i,3] + datetime.timedelta(minutes = anahattrendonus.iloc[i,5])

                
                anahattren_kazanc += 45000
                print("Kazanc: ", anahattren_kazanc,' TL')
                Cikis_suresi = anahattrendonus.iloc[-1,4]

                anahattrentablo['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 4*60)

                print(anahattrendonus)
                tablo3 = tablo3.append(anahattrendonus)
                print(anahattren_anlikkm)
                

                anahattren_anlikkm = anahattren_anlikkm + anahattren_birseferkm

                if(anahattren_anlikkm>2500):
                    print("BAKIM LAZIM")
                    # Bakim süresi ekle
                    anahattrentablo['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 24*60)
                    anahattren_anlikkm = 0

                if(anahattrentablo['Cikis'][6]>datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(days = gun_sayisi)):
                    break

                for i in range(anahattrentablo['istasyon'].count()):
                    
                    if i == 0:
                        anahattrentablo.iloc[i,3] = None # Varis
                        #hizlitrendonus.iloc[i,4] = Cikis_suresi + datetime.timedelta(minutes = 120)
                        anahattrentablo.iloc[i,5] = None # Bekleme Suresi

                    else:
                        istasyon_mesafe = anahattrentablo.iloc[i,1]-anahattrentablo.iloc[i-1,1]
                        anahattrentablo.iloc[i,3] = anahattrentablo.iloc[i-1,4] + datetime.timedelta(minutes = istasyon_mesafe/anahattrendonus.iloc[i,2]*60)
                        anahattrentablo.iloc[i,4] = anahattrentablo.iloc[i,3] + datetime.timedelta(minutes = anahattrentablo.iloc[i,5])
                
                
                
                anahattren_kazanc += 45000
                print("Kazanc: ", anahattren_kazanc, ' TL')
                
                
                
                Cikis_suresi = anahattrentablo.iloc[-1,4]


                print(anahattrentablo)
                tablo3 = tablo3.append(anahattrentablo)
                print(anahattren_anlikkm)



# ANAHAT TREN BOLUMU BİTİS


# YUK TREN BOLUMU
    Cikis_suresi = datetime.datetime(2022,5,17,0,0,0)
    yuktren_genelbakimkm = 3000
    yuktren_anlikkm = 0
    yuktren_birseferkm = 618
    yuktren_kazanc = anahattren_kazanc
    
    sefer_sayisi = gun_sayisi * 7
    # tren dagitimi
    
    for i in range(int(YT_sayisi)):
        print("G-L Güzergahı")
        print("YT-",i+1)
        
        seferadi = "YT-"+ str(i+1) +"G-L Güzergahı"
        yuktrentablo['SeferAdi'] = seferadi

        
        yuktren_genelbakimkm = 3000
        yuktren_anlikkm = 0
        yuktren_birseferkm = 618
        
        if(i != 0):
            Cikis_suresi = datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(minutes =  5*i)

        for i in range(sefer_sayisi):
            
            
            if(yuktren_anlikkm>3000):
                print("BAKIM LAZIM")
                # Bakim süresi ekle
                yuktrentablo['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 36*60)
                yuktren_anlikkm = 0
           
            if(i!=0):
                if(yuktrentablo['Cikis'][7]>datetime.datetime(2022,5,17,0,0,0) + datetime.timedelta(days = gun_sayisi)):
                    break

            if(i==0):
                yuktrentablo['Cikis'] = Cikis_suresi

            else:
                yuktrentablo['Cikis'] = Cikis_suresi + datetime.timedelta(minutes = 3*60)

            for i in range(yuktrentablo['istasyon'].count()):

                if i == 0:

                    yuktrentablo.iloc[i,3] = None # Varis
                    yuktrentablo.iloc[i,5] = None # Bekleme Suresi
                

                else:
                    istasyon_mesafe = yuktrentablo.iloc[i,1] - yuktrentablo.iloc[i-1,1]
                    yuktrentablo.iloc[i,3] = yuktrentablo.iloc[i-1,4] + datetime.timedelta(minutes = istasyon_mesafe/yuktrentablo.iloc[i,2]*60)
                    yuktrentablo.iloc[i,4] = yuktrentablo.iloc[i,3] + datetime.timedelta(minutes = yuktrentablo.iloc[i,5])
                    

            yuktren_kazanc += 50000
            print("Kazanc: ", yuktren_kazanc)

            Cikis_suresi = yuktrentablo.iloc[-1,4]

            print(yuktrentablo)
            tablo3 = tablo3.append(yuktrentablo)

            print(yuktren_anlikkm)


            yuktren_anlikkm = yuktren_anlikkm + yuktren_birseferkm
           
    return tablo3
# YUK TREN BOLUMU BİTİS
        
if HT_sayisi>=2 and AT_sayisi>=1 and YT_sayisi>=1:
    print("Hesaplama başlıyor.")
    tablo3 = seyahat_uret(int(gun_sayisi),int(HT_sayisi),int(AT_sayisi),int(YT_sayisi))
    pd.set_option('display.max_rows', None)

    tablo3['istasyon'] = tablo3['istasyon'].str.replace('PSon', 'P')
    tablo3['istasyon'] = tablo3['istasyon'].str.replace('GBas', 'G')
    #tablo3.Varis.fillna(value='KalkanTren', inplace=True)

    tablo3 = tablo3.drop(['KacinciKM','OrtalamaHiz','BeklemeSüresi'],axis=1)
    tablo3 = tablo3.drop_duplicates(keep=False)
    tablo3 = tablo3.sort_values(by=['istasyon','Cikis'])


