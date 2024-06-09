pastel_pertama = ["merah", "kuning", "hijau", "biru"]           #mencari wara berbeda
pastel_kedua = ["kuning", "coklat", "ungu,"]

# pastel_kedua += ["merah"]                   menambah warna
# pastel_pertama += ["jingga"]

warna_berbeda = set(pastel_pertama) - set(pastel_kedua)
print("warna yang berbeda adalah : {}".format(warna_berbeda))

		# mancari warna sama

# pastel_pertama = ["merah", "kuning", "hijau", "biru", "jingga"]
# pastel_kedua = ["kuning", "coklat", "ungu", "merah"]

# warna_sama = set(pastel_pertama).intersection(set(pastel_kedua))
# print("warna yang sama adalah: {}".format(warna_sama))

		# mencari yang sama

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x & y

# print(z)