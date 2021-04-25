menu = ["1. Lihat Daftar Contact", "2. Input Contact Baru","3. Keluar"]
print("-Selamat Datang Pelanggan yang Terhormat.-")
print("Pilihan Menu:")
print("-------------")
for item in menu:
    print(item)
pilihan= int(input("Silakan pilih nomor pada menu di atas: "))
nama =[]
nomor_tlp =[]

while pilihan <=0 or pilihan > 3:
    pilihan= int(input("Nomor yang anda masukkan SALAH. Jika ingin mengulang, silakan pilih nomor pada menu di atas: "))   
while pilihan == 1 or pilihan==2 or pilihan==3: 
    if pilihan == 1:
        for a1,a2 in zip(nama,nomor_tlp):
            print("--------------------")
            print("Nama: ", a1)
            print("Nomor Telepon: ", a2)
        print("--------------------")
        for i in menu:
            print(i)
        pilihan= int(input("Silakan pilih nomor pada menu di atas: "))
        while pilihan <=0 or pilihan > 3:
            pilihan= int(input("Nomor yang anda masukkan SALAH. Jika ingin mengulang, silakan pilih nomor pada menu di atas: "))   
    elif pilihan == 2:
        print("Silakan input nama dan Nomor Telepon")
        nama.append(input("Nama : "))
        nomor_tlp.append(input("Nomor Telepon: "))
        print("Nomor anda telah tercatat. Perlu tambahan lagi?")
        print("------------------------------------------------")
        for i in menu:
            print(i)
        pilihan= int(input("Silakan pilih nomor pada menu di atas: "))
        while pilihan <=0 or pilihan > 3:
            pilihan= int(input("Nomor yang anda masukkan SALAH. Jika ingin mengulang, silakan pilih nomor pada menu di atas: "))   
    elif pilihan == 3:
        print("Program telah selesai. Terima kasih.") 
        pilihan=int(input("Jika ingin mengulang, silakan pilih nomor pada menu di atas: ")) 
        while pilihan <=0 or pilihan > 3:
            pilihan= int(input("Nomor yang anda masukkan SALAH. Jika ingin mengulang, silakan pilih nomor pada menu di atas: "))   
        
 
