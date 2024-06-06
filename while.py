nama_list = []

while True :
	nama = input("masukan jenis kendaraan :")
	nama_list.append(nama)

	if nama.lower() == "python" :   #untul menghentikan code yg berjalan
		break

	elif nama.lower() == "montor" :
		print("parkir anda adalah : 2000")

	elif nama.lower() == "sepeda" :
		print("parkir anda adalah : 1000")

	elif nama.lower() == "mobil" :
		print("parkir anda adalah : 5000")
print("goodbye python")		