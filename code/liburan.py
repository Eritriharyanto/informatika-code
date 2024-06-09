liburan = ["william", "kate", "anderson", "jame", "mady"]
rute = ["jakarta", "ciamis", "kebumen", "jogja"]
liburan += ["jones"]
liburan[2] = "grece"
print(liburan)

member = "thompson" in liburan
print(member)

liburan.sort()

# for nama in liburan:
# 	print(nama)

# i = 0
# while i < len(liburan):
# 	print(liburan)
# 	break

for i in liburan:
	print(i, end="")
liburan.clear()
print(liburan)