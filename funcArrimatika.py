def luas_persegi_panjang(panjang,lebar):
	luas = panjang*lebar
	return luas

def volume_balok(panjang,lebar,tinggi):
	volume = luas_persegi_panjang(panjang,lebar)*tinggi
	return volume

if __name__ == "__main__":
	panjang = int(input("masukan panjang balok : "))
	lebar = int(input("masukan lebar balok : "))
	tinggi = int(input("masukan tinngi balok : "))
	print("volume balok adalah {}".format(volume_balok(panjang,lebar,tinggi)))