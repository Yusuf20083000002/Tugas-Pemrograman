# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 12:35:49 2021

@author: muham
"""
jawab="y"
while jawab=="y" or jawab=="Y":
    print("---------------------------------")
    print("      Cek golongan usia          ")
    print("Author: Muhammad Yusuf Aldiansyah")

    U=1
    while int(U)>0 and int(U)<=100:
        U = input("Masukkan Usia Anda : ")
        
        if int(U)>0 and int(U)<=100:
            
            if int(U)>=60:
                sts="Lansia"
            elif int(U)>=35:
                sts="Dewasa"
            elif int(U)>=18:
                sts="Pemuda"
            elif int(U)>=15:
                sts="Remaja"
            else:
                sts="Anak"
            print("Usia anda tergolong dalam: " + sts)
            jawab= input("Ingin mengecek kembali? y/t : ")
            if jawab=="t" or jawab=="T":
                break
        else:
             Pesan=("Masukkan Usia 0-100 saja")
             print(Pesan)
             break
print("Terima kasih")