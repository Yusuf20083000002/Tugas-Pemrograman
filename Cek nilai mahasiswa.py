# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 21:01:31 2021

@author: muham
"""

jawab="y"
while jawab=="y" or jawab=="Y":

    print("---------------------------------")
    print("      Cek nilai Mahasiswa         ")
    print("Author: Muhammad Yusuf Aldiansyah")

    n=0
    while int(n)>=0 and int(n)<=100:
        n=input("Masukkan nilai anda: ")

        if int(n)>=0 and int(n)<=100:
            if int(n)>=91:
                sts="A"
            elif int(n)>=81:
                sts="B"
            elif int(n)>=71:
                sts="C"
            else:
                sts="D"
            print("Nilai anda dalam kategori: " +sts)
            jawab=input("Ingin mengulangi? y/t: ")
            if jawab=="t" or jawab=="T":
                break

        else:
            pesan=("Masukkan angka 0-100 saja")
            print(pesan)
    break
print("Terima kasih...")