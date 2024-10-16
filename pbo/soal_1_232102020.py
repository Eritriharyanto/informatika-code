mata_kuliah = {
    "INF004": "Matematika Teknik",
    "INF005": "Fotografi",
    "INF007": "Instalasi Hardware",
    "INF008": "Sistem Operasi",
    "INF013": "Pendidikan Pancasila",
    "INF015": "Algoritma Komputer & Struktur Data"
}

for i in range(5):
    kode = input(f"Masukkan kode mata kuliah ke-{i+1}: ")
    nama = input(f"Masukkan nama mata kuliah ke-{i+1}: ")
    mata_kuliah[kode] = nama

mata_kuliah["INF011"] = "Pemrograman Python"
mata_kuliah["INF023"] = "Bahasa Indonesia"

print("\nDaftar Mata Kuliah:")
for kode, nama in mata_kuliah.items():
    print(f"{kode} ===> {nama}")
