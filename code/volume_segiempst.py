def luas_segiempat (panjnag, lebar):
	luas = panjang * lebar
	return luas

def volume_prisma_segiempat(panjang, lebar, tinggi):
	volume = luas_segiempat(panjang, lebar) * tinggi
	return volume

panjang = int(input("masukan panjang : "))
lebar = int(input("masukan lebar : "))
tinggi = int(input("masukan tinggi : "))

luas_alas = luas_segiempat(panjang, lebar)
volume = volume_prisma_segiempat(panjang, lebar, tinggi)

print(f"volume prisma segiempat adalah : {volume}")