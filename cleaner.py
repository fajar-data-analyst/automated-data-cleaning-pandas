import pandas as pd

data_berantakan = {
    'Tanggal': ['2026-01-01', '2026-01-02', '2026-01-02', None, '2026-01-04'],
    'Produk': ['Laptop', 'Smartphone', 'Smartphone', 'Tablet', 'Headphone'],
    'Harga_Satuan': [15000000, 5000000, 5000000, 3000000, None],
    'Jumlah': [1, 2, 2, 1, 5]
}

df_dirty = pd.DataFrame(data_berantakan)

# Menampilkan Data Kotor awal
print('=== Dataset Kotor === ')
print(df_dirty)

# Berapa ukuran dari dataset
print(df_dirty.shape)

# Ada kolom apa saja di dataset
print(df_dirty.columns)

# Ada tipe data apa saja dan menampilkan kolom mana yg data nya kosong(none)
df_dirty.info()

# Hasil statistik dari dataset
print(df_dirty.describe())

# Mengecek apakah di dasaset ini ada missing value(data kosong)
print(df_dirty.isnull()) # Akan menampilkan nilai boolean, yang hasilnya "True" berarti data tersebut kosong.

# Menghitung total data missing value(data kosong) ada berapa?
print(df_dirty.isnull().sum()) # Akan menampilkan ada berapa data yang kosong di setiap kolom

# Melihat baris mana yang memiliki missing value(data_kosong)
print(df_dirty[df_dirty.isnull().any(axis = 1)])

# Mengisi data yang harga satuan yang kosong dari menjadi 1.000.000
df_dirty['Harga_Satuan'] = df_dirty['Harga_Satuan'].fillna(800000)

# Menghapus data pembelian tapi tanggal pembelian nya tidak ada(kosong)
df_clean = df_dirty.dropna()
print(df_clean) 



# Dari dataset ini apakah ada yg duplikat
print(df_clean.duplicated()) # Dari hasil ini ditemukan bahwa indeks ke 2 datanya duplikat dengan indeks ke 1

# Bisa juga melihat data mana yg duplikat
print(df_clean[df_clean.duplicated()])

# Setelah melihat data mana yang duplikat, data duplikat tersebut akan di hapus
df_clean = df_clean.drop_duplicates()
print(df_clean)


# Ingin mengetahui berapa total pendapatan per transaksi
df_clean['Total_Pendapatan'] = df_clean['Harga_Satuan'] * df_clean['Jumlah']
print(df_clean)

# Ingin mengetahui produk mana yang laporan penjualannya terbesar
laporan_penjualan = df_clean.groupby('Produk')['Total_Pendapatan'].sum().sort_values(ascending = False).reset_index()
print(laporan_penjualan)

df_clean.to_csv('data_penjualan_bersih.csv', index = False)
laporan_penjualan.to_csv('laporan_performa_produk.csv', index = False)

print("Proses selesai! Semua file bersih berhasil disimpan")