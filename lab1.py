#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 09:55:26 2021
Yapay Zeka Lab. 1. Hafta 
@author: msoguz
"""
import pandas as pd
import numpy as np
# .csv formatında bu tabloyu oluşturup lokalde bu tabloyu Pandas kütüphanesini kullanarak açınız
veri=pd.read_csv('/Users/msoguz/Desktop/yapay zeka/1. hafta/Lab1.csv',sep=";",quotechar='"')

#Pandas kütüphanesi aracılığıyla tablodan “Sıcaklık” ve “Nem” değerlerini siliniz
sütunsil=veri.drop(['Sıcaklık'],axis=1)
nemsil=sütunsil.drop(['Nem'],axis=1)
print(veri)
print(nemsil)

#Pandas kütüphanesinin metodu olan DataFrame() ile yukarıda verilen tabloyu oluşturunuz 
d = {'Gün': ['G1', 'G2','G3','G4','G5','G6', 'G7','G8','G9','G10','G11', 'G12','G13','G14'], 
     'Hava Durumu': ['Güneşli', 'Güneşli','Kapalı','Yağmurlu','Yağmurlu','Yağmurlu','Kapalı','Güneşli', 'Güneşli','Yağmurlu', 'Güneşli','Kapalı','Kapalı','Yağmurlu'],
     'Sıcaklık':['Sıcak','Sıcak','Sıcak','Ilıman','Soğuk','Soğuk','Soğuk','Ilıman','Soğuk','Ilıman','Ilıman','Ilıman','Sıcak','Ilıman'],
     'Nem':['Yüksek','Yüksek','Yüksek','Yüksek','Normal','Normal','Normal','Yüksek','Normal','Normal','Normal','Yüksek','Normal','Yüksek'], 
     'Yağış':['Seyrek','Aşırı','Seyrek','Seyrek','Seyrek','Aşırı','Aşırı','Seyrek','Seyrek','Seyrek','Aşırı','Aşırı','Seyrek','Aşırı'],
     'Oyun':['Yok','Yok','Var','Var','Var','Yok','Var','Var','Yok','Var','Var','Yok','Var','Yok',]}
df = pd.DataFrame(data=d)
print(df)

#ve tablo hakkında betimleyici istatiksel bilgiler veriniz
print("Describe metodu: ")
print(df.describe())
print("İnfo metodu: ")
print(df.info())

#(3,4) boyutunda bir dizi oluşturunuz. Oluşturduğunuz bu dizinin boyutunu (6,2) olacak şekilde değiştiriniz

Dizi=np.arange(12).reshape(3,4)
print(Dizi)
dizi2=np.reshape(Dizi,(6,2))
print(dizi2)

#İki tane (3,3) boyutunda rastgele sayılardan meydana bir dizi oluşturunuz. 
dizi3=np.random.randint(1,150,size=(3,3),dtype=np.uint8)
print(dizi3)
dizi4=dizi3

#Oluşturulan bu diziyi hem yatay hem de dikey olacak şekilde istif (stack) ediniz 
yatay=np.hstack((dizi3,dizi3))
print(yatay)
dikey=np.vstack((dizi3,dizi3))
print(dikey)
