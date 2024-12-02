# Lacak Lokasi Target Ome TV

Script ini digunakan untuk mendeteksi dan mengambil informasi lokasi geografis dari sebuah alamat IP, termasuk benua, negara, provinsi, kota, ISP, serta koordinat geografis. Data tersebut diambil dari API eksternal dan ditampilkan dalam format yang mudah dibaca.

## Fitur
- Mendeteksi alamat IP dari input string.
- Mengambil informasi geolokasi dari alamat IP menggunakan API.
- Menampilkan informasi lokasi geografis dan ISP dari alamat IP yang diberikan.

## Prasyarat

Sebelum menjalankan script, pastikan Anda telah menginstal dependensi berikut:

- Python 3.x
- Modul `requests`
- Modul `re`
- Modul `json`
- Modul `os`
- Modul `http.client`
- Modul `urllib`

Untuk menginstal dependensi, jalankan perintah berikut:
```bash
pip install requests
```

## Cara Penggunaan
- Jalankan script menggunakan Python:
```bash
python located.py
```
- Masukkan input yang berisi alamat IP atau string yang mengandung alamat IP yang ada di inspect
- Script akan mencari alamat IP di dalam input dan menampilkan informasi terkait lokasi dari alamat IP tersebut.

## Output
Informasi yang ditampilkan meliputi:

- Alamat IP
- Benua
- Negara
- Provinsi
- Kota
- ISP
- Latitude dan Longitude
- Kecepatan respons (ms)

## NOTE
- Pastikan koneksi internet stabil untuk menghindari error saat mengambil data dari API.
- Script akan membersihkan layar setelah setiap iterasi untuk menjaga tampilan yang bersih.
