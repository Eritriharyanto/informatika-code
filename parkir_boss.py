nama_list = []

while True :
    nama = input("jenis kendaraan: ")
    nama_list.append(nama)

    if nama.lower() == "selesai" :
    	break

    elif nama.lower() == "sepeda" :
        print("total parkir rp 500,00")

    elif nama.lower() == "motor" :
        print("total parkir rp 2.000,00")

    elif nama.lower() == "mobil" :  
        print("total parkir rp 5.000,00")

    else:
        print("Jenis kendaraan tidak dikenali, masukkan jenis yang valid (sepeda, motor, mobil).")

    print("terimakasih")
    print("goodbye")                	