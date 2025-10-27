# a. List berisi tiga pasangan titik
titik_list = [(0, 0), (50, 50), (100, 0)]

print("Daftar titik dalam list:")
for titik in titik_list:
    print(titik)

# b. Tuple berisi satu titik pusat
pusat = (0, 0)
print("\nTitik pusat:", pusat)

# c. Dictionary berisi atribut titik
titik_dict = {"x": 10, "y": 20, "warna": "biru"}
print(f"\nTitik ({titik_dict['x']}, {titik_dict['y']}) berwarna {titik_dict['warna']}.")
