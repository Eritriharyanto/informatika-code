#b
kereta = ["william","kate","anderson","jame","mady"]

#c
kereta.append("jones")
kereta[2] = "grace"

#d
check_thomson = "thomson" in kereta

sorted_result = sorted(kereta)

for index, data in enumerate(kereta):
	print("penumpang nomor {} dengan nama: {}".format(index, data))