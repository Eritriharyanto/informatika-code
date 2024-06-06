data_angka = [1,2,3,4,5,6,7,8,9]

bilangan_ganjil = []                        #kalau ingin menampilkan bilangan genap tingal ganti menjadi genap

for angka in data_angka:
	if angka % 3 == 0:                      #kalau ingin menmpilkan bilangan ganjil gunakan 2!(tanda seru)
		bilangan_ganjil.append(angka)

print(bilangan_ganjil)     