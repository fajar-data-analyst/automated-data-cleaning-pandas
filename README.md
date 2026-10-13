# Automasi Pembersihan dan Analisis Data Penjualan Toko Online (Pandas)

## 📌 Deskripsi Proyek
Proyek ini dibuat untuk mensimulasikan tantangan nyata yang sering dihadapi oleh pemilik bisnis atau toko online, yaitu memiliki data transaksi mentah yang berantakan, memiliki nilai kosong (*missing values*), serta pencatatan ganda (*data duplikat*). 

Menggunakan kekuatan library **Python Pandas**, saya membangun sebuah skrip automasi untuk mendeteksi kerusakan data, melakukan proses pembersihan data (*data cleaning*), hingga mengekstrak ringkasan performa penjualan produk secara akurat dalam hitungan detik.

## 🛠️ Fitur & Fungsi Pandas yang Digunakan
- **Eksplorasi Data Berantakan:** `.info()`, `.isnull().sum()`, dan `.describe()` untuk memetakan kolom yang mengalami kerusakan atau kekosongan data awal.
- **Pembersihan Data:** `.fillna()` untuk mengatasi harga satuan yang kosong secara logis, `.dropna()` untuk menghapus baris tanpa tanggal transaksi, dan `.drop_duplicates()` untuk memastikan akurasi data keuangan.
- **Feature Engineering:** Membuat kolom kalkulasi omset baru bernama `Total_Pendapatan` hasil perkalian harga satuan dan jumlah beli.
- **Agregasi Bisnis:** `.groupby()`, `.sum()`, dan `.sort_values()` untuk menyusun laporan produk dengan pendapatan terbesar.

## 📊 Hasil Analisis (Sebelum vs Sesudah)

### 1. Kondisi Data Mentah (Awal)
- Terdapat baris kosong (`NaN`) pada kolom tanggal transaksi.
- Kolom harga satuan memiliki data yang hilang pada produk Headphone.
- Terjadi pencatatan ganda (Duplikat) pada transaksi Smartphone di baris ke-2 dan ke-3 yang dapat merusak kalkulasi profit toko.

### 2. Kondisi Data Bersih (Hasil Akhir)
Seluruh hasil automasi data yang sudah bersih diekspor secara otomatis ke dalam file `data_penjualan_bersih.csv` dengan struktur kolom yang rapi:
`Tanggal`, `Produk`, `Harga_Satuan`, `Jumlah`, `Total_Pendapatan`

## 📈 Laporan Performa Produk (Insight Toko)
Berdasarkan berkas ringkasan `laporan_performa_produk.csv` yang dihasilkan secara otomatis lewat fungsi agregasi, berikut adalah urutan performa produk berdasarkan total pendapatan tertingginya:
1. **Laptop** — Memberikan kontribusi omset terbesar bagi toko senilai **Rp15.000.000**.
2. **Smartphone** — Menyumbang omset stabil sebesar **Rp10.000.000** (setelah baris duplikat berhasil dibersihkan).
3. **Headphone** — Menyumbang omset sebesar **Rp4.000.000** (setelah harga kosong berhasil ditangani secara logis menggunakan teknik imputasi data).

---
## 📬 Butuh Bantuan Mengotomatisasi dan Merapikan Data Bisnis Anda?
Jika Anda memiliki data Excel, Google Sheets, atau CSV yang berantakan dan ingin dibersihkan secara otomatis menggunakan skrip Python Pandas yang cepat, mari berkolaborasi! Anda dapat menghubungi saya melalui:
- **Email:** [ahmadfajaralizaini@gmail.com]
