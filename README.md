# Aplikasi Manajemen Kursus Online
Aplikasi web sederhana untuk mengelola kursus online, dibuat dengan Django. Aplikasi ini memungkinkan admin untuk menambah, mengubah, dan menghapus kursus serta mengatur keanggotaan peserta kursus.

## Apa yang Bisa Dilakukan Aplikasi Ini?
1. **Halaman Utama**
   - Melihat daftar semua kursus yang tersedia
   - Melihat detail setiap kursus (nama, pengajar, harga)
2. **Halaman Admin**
   - Login sebagai admin
   - Menambah kursus baru
   - Mengubah detail kursus
   - Menghapus kursus
   - Mengatur peserta kursus

## Cara Menjalankan Aplikasi
### 1. Persiapan Awal
Pastikan Python sudah terinstall dipc, lalu:
1. Buka terminal atau command prompt
2. Install semua yang dibutuhkan dengan perintah:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Menyiapkan Database
Ketik perintah berikut di terminal:
```bash
python manage.py migrate
```

### 3. Membuat Akun Admin
```bash
python manage.py createsuperuser
```
- Masukkan usernamenya
- Masukkan email (boleh dikosongkan)
- Masukkan password
- Konfirmasi password

### 4. Menjalankan Aplikasi
```bash
python manage.py runserver
```

### 5. Mengakses Aplikasi
Buka browser dan kunjungi:
- Halaman Utama: http://localhost:8000
- Halaman Admin: http://localhost:8000/admin
- Halaman Kursus: http://localhost:8000/courses

## Cara Menguji Aplikasi

### Menguji Fitur-fitur (Unit Testing)
Ketik perintah ini di terminal:
```bash
python manage.py test courses
```
Ini akan mengecek apakah semua fitur berjalan dengan benar.

### Menguji Kinerja Aplikasi (Load Testing)
Load testing utk proses menguji kemampuan website dalam menangani banyak pengunjung sekaligus.

#### Cara Melakukan Load Testing:
1. Buka terminal baru (jangan tutup terminal sebelumnya)
2. Jalankan Locust:
   ```bash
   locust -f locustfile.py --host=http://localhost:8000
   ```
3. Buka http://localhost:8089 di browser
4. Masukkan:
   - Number of users: 5 (berapa banyak pengunjung virtual yang akan mengakses website)
   - Spawn rate: 1 (berapa cepat pengunjung virtual ditambahkan, 1 = tambah 1 pengunjung per detik)
   - Klik "Start swarming"

#### Apa yang Diuji:
- Halaman Utama (/)
- Halaman Kursus (/courses/)
- Halaman Admin (/admin/)
- Proses Login
- Kecepatan respon website
- Kemampuan menangani banyak pengunjung

#### Hasil Pengujian:
Dari hasil testing terakhir, website menunjukkan performa yang sangat baik:
- RPS (Request Per Second): 3.2 (bisa melayani 3.2 permintaan per detik)
- Failures: 0% (tidak ada error)
- Response Time:
  * Halaman Utama: 1.69ms (sangat cepat)
  * Halaman Admin: 7.03ms (cepat)
  * Halaman Kursus: 3.7ms (cepat)

## Struktur File

```
testing_project/
├── courses/                # Folder untuk fitur course
│   ├── models.py          # Data course & peserta
│   ├── views.py           # tampilan
│   ├── tests.py           # File pengujian
│   └── templates/         # Tampilan HTML
├── testing_project/       # Pengaturan utama
├── locustfile.py         # File untuk uji kinerja
└── requirements.txt      # Daftar yang dibutuhkan
```

## Hasil Pengujian

Aplikasi sudah diuji dan menunjukkan hasil yang baik:
- Semua fitur berjalan lancar (0% error)
- Waktu respon cepat (rata-rata < 0.5 detik)
- Bisa digunakan oleh banyak pengguna sekaligus

## Rencana Pengembangan

Fitur yang bisa ditambahkan nanti:
1. Pendaftaran pengguna baru
2. Sistem pembayaran
3. Forum diskusi
4. Unggah materi kursus
5. Sistem penilaian

---
Dibuat dengan tangan, mata, otak, hati, jiwa, raga, waktu, tenaga, suasana, situasi, kondisi, apapun itu ya ges yak @sumanto