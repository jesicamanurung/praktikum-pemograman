print()
print('praktikum-b5')
print('Nama Lengkap: Jesica Septiani Manurung')
print('NIM         : 231031045')
print('prodi       : Sistem Informasi')
print()

nim = [2,3,1,0,3,1,0,4,5]
print(nim)
# akses item
print('item index 0:,',nim[0])
print('item index 3:,',nim[3])
print('item index terakhir:,',nim[len(nim)-1])
#akses indeks negatif
print('item index terakhir:,',nim[-1])
print('item index pertama:,',nim[-len(nim)])
print('item index 3: [-6]',nim [-6])
print('item index 5: [-4]',nim [-4])
print('item index -7: [2]',nim [2])
print('item index 2: [-7]',nim [-7])
# akses index batas
print(f'item index 1,2,.....: {nim [1:]}')
print(f'item index 3,3,.....: {nim [3:]}')
print(f'item index 0,1,2,3: {nim [:4]}')
print(f'item index 0 : {nim [:1]}')
print(f'item index semua: {nim [:]}')
print(f'item index [:8]: {nim [:-1]}')
print(f'item index [:4]: {nim [:-5]}')
# pengirisan 
print(f'item index 1,2: {nim [1:3]}')
print(f'item index []: {nim [3:3]}')
print(f'item index 2,3,4: {nim [2:5]}')
print(f'item index [1:8]: {nim [1:-1]}')
print(f'item index [2:7]: {nim [2:-2]}')
print('\n')
# nested list
kelas = [('kalkulus',2),
         ('pemrograman',3)]
print(kelas)
kelas.append(('pancasila',2))
# tambahkan matkul 4 dan 5 dan sksnya
kelas.append(('Sainster',2))
kelas.append(("PTI",2))
print(kelas)

# Mata kuliah 1: Matkul1 dengan 2 sks
print(f"Mata Kuliah 1: {kelas[0][0]} dengan {kelas[0][1]} sks")

# Mata kuliah 2: Matkul2 dengan 3 sks
print(f"Mata Kuliah 2: {kelas[1][0]} dengan {kelas[1][1]} sks")

# Mata kuliah 3: Matkul3 dengan 2 sks
print(f"Mata Kuliah 3: {kelas[2][0]} dengan {kelas[2][1]} sks")

# Mata kuliah 4: Matkul4 dengan .. sks
print(f"Mata Kuliah 4: {kelas[3][0]} dengan {kelas[3][1]} sks")

# Mata kuliah 5: Matkul5 dengan .. sks
print(f"Mata Kuliah 5: {kelas[4][0]} dengan {kelas[4][1]} sks")

print('\n')
data = [('Jesica',2023,'Aktif'),
        (76,98,89,87,99),
        [2,3,2,2,2],
        ('S1-Reguler','Sistem Informasi B','Ganjil')]

# Nama mahasiswa: jesica
print(f"Nama mahasiswa : {data[0][0]}")

# Inisial jesica: j
print(f"Inisial mahasiswa : {data[0][0][0]}")

# NIM jesica: 231031045
nim_int = int("".join(map(str, nim))) 
print(f"NIM {data[0][0]} : {nim_int}")

# Program jesica: S1-Reguler Sistem Informasi B
print(f"Program {data[0][0]} : {data[3][0]} {data[3][1]}")

# Angkatan jesica: Ganjil-2023
print(f"Angkatan {data[0][0]}: {data[3][2]}-{data[0][1]}")

# Total sks jesica adalah: 11
print(f"Total sks {data[0][0]} adalah: {sum(data[2])}")

# Jumlah Nilai jesica: 5
print(f"Jumlah Nilai {data[0][0]}: {len(data[2])}")

# Nilai tertinggi jesica: 99
print(f"NIlai tertinggi {data[0][0]}: {max(data[1])}")

# Nilai terendah jesica: 76
print(f"NIlai terendah {data[0][0]}: {min(data[1])}")

# Rata-rata nilai jesica: 89.8
x_bar = sum(data[1])/len(data[1])
print(f'Rata-rata nilai {data[0][0]} adalah: {x_bar}')














