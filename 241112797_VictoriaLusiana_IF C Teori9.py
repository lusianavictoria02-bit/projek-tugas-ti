Data = [1, 2, -4, -5, 0, 10, 5]

# 1. Fungsi untuk menentukan Bilangan Ganjil
def cari_ganjil(data):
    hasil_ganjil = []
    for bilangan in data:
        if bilangan % 2 != 0:
            hasil_ganjil.append(bilangan)
    return hasil_ganjil

# 2. Fungsi untuk menentukan Bilangan Genap
def cari_genap(data):
    hasil_genap = []
    for bilangan in data:
        if bilangan % 2 == 0:
            hasil_genap.append(bilangan)
    return hasil_genap

# 3. Fungsi untuk menentukan Bilangan Positif
def cari_positif(data):
    hasil_positif = []
    for bilangan in data:
        if bilangan > 0:
            hasil_positif.append(bilangan)
    return hasil_positif

# 4. Fungsi untuk menentukan Bilangan Negatif
def cari_negatif(data):
    hasil_negatif = []
    for bilangan in data:
        if bilangan < 0:
            hasil_negatif.append(bilangan)
    return hasil_negatif

bilangan_ganjil = cari_ganjil(Data)
bilangan_genap = cari_genap(Data)
bilangan_positif = cari_positif(Data)
bilangan_negatif = cari_negatif(Data)

bilangan_nol = [b for b in Data if b == 0]

print(f"Data awal: {Data}")
print("-" * 35)

print(f"1. Bilangan Ganjil: {bilangan_ganjil}")
print(f"2. Bilangan Genap: {bilangan_genap}")
print("-" * 35)
print(f"3. Bilangan Positif: {bilangan_positif}")
print(f"4. Bilangan Negatif: {bilangan_negatif}")
print(f"   Bilangan Nol: {bilangan_nol}")