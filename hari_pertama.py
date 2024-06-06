# Define the initial set
hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = ("keju", {"garam", "gula", "coklat", "kecap"})

# If you want to discard "tepung" from hari_pertama
hari_pertama.discard("tepung")

# Print the modified set
print(hari_pertama)

# If you want to access elements from hari_kedua tuple
print(hari_kedua[0])  # This will print "keju"
print(hari_kedua[1])  # This will print the set {"garam", "gula", "coklat", "kecap"}
