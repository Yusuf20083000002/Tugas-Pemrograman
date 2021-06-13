# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("       CEK KELULUSAN NILAI")
print("Author: Muhammad Yusuf Aldiansyah")
jawab = "y"
while jawab== "y":
    
    n = input("Masukkan Nilaimu: ")
    if int(n)>60:
        sts= "LULUS"
    else:
        sts= "ULANG"
    
    print ("Nilaimu dalam kategori " + sts)
    
    jawab = input("Pengecekan Nilai kembali? : ")
    if jawab== "t":
        break