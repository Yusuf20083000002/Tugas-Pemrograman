
#Author: Muhammad Yusuf Aldiansyah
#NIM : 20083000002l

jawab="y"
while jawab=="y" or jawab=="Y":

    print("----------------------------------------")
    print("...Cek jumlah harga pembelian printer...")
    
    n=1
    while int(n)>0:
        printer = 660000
        n=int(input("Jumlah printer yang dibeli: "))
        jumlah= n * printer
        
        print("Uang yang dibayarkan: "+format(jumlah,',.2f'))

        jawab=input("Ingin mengecek kembali? y/t: ")
        if jawab=="t" or jawab=="T":
                break
print("Terima kasih sudah berkunjung...")
