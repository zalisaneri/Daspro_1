 #Irena Silmi Azizah
#2500869
#1b
print("=== Sistem Analisis Performa Jualan ===")
pertanyaan = int(input("berapa banyak produk yang terjual hari ini: "))
data = []
for i in range (1, pertanyaan +1):
    if pertanyaan < 0 :
        print("x input tidak valid harga harus berupa angka")
    else :
        harga = int(input(f"masukkan harga produk ke {i}: "))
        data.append((harga))
def total(data):
    menghitung_total = sum(data)
    return menghitung_total
def rata(data):
    rata_rata = sum(data)/len(data)
    return rata_rata
print("=== Hasil Analisis ===")
print(f"jumlah produk yang dijual : {len(data)} ")
print(f"Total pendapatan Rp. {total(data)}")
print(f"Rata-rata pendapatan per produk Rp. {rata(data)}")



