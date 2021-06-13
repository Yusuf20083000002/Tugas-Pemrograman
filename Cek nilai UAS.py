# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 19:35:41 2021

@author: muham
"""

jawab="y"
while jawab=="y" or jawab=="Y":

    print("---------------------------------")
    print("      Cek nilai UAS          ")
    print("Author: Muhammad Yusuf Aldiansyah")

    n=0
    while int(n)>=0 and int(n)<=100:
        n=input("Masukkan nilai anda: ")

        if int(n)>0 and int(n)<=100:
            if int(n)>80:
                sts="Baik Sekali"
            elif int(n)>=65:
                    sts="Baik"
            elif int(n)>=55:
                    sts="Cukup"
            elif int(n)>=40:
                    sts="Kurang"
            else:
                    sts="Kurang sekali"
            print("Nilai anda tergolong: " + sts)
            jawab= input("Ingin Mengulangi? y/t: ")
            if jawab=="t" or jawab=="T":
                break
        else:
            pesan=("Masukkan angka 0-100 saja!")
            print(pesan)
            break
print("Terima kasih..")
