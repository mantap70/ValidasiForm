# Program Validasi Formulir Pendaftaran
![CodePicture](pictures/code.png)  
Program ini memvalidasi input dari pengguna untuk memastikan data yang dimasukkan sesuai dengan aturan yang telah ditentukan. Program memeriksa tiga jenis input: nama lengkap, nomor telepon, dan email.

## Fitur Validasi

1. **Nama Lengkap**:  
   Memastikan bahwa nama lengkap hanya mengandung huruf. Jika tidak, akan menampilkan pesan kesalahan:  
   `"Nama lengkap harus hanya berisi huruf."`

2. **Nomor Telepon**:  
   Memastikan bahwa nomor telepon hanya terdiri dari angka. Jika tidak, akan menampilkan pesan kesalahan:  
   `"Nomor telepon harus hanya berisi angka."`

3. **Email**:  
   Memastikan bahwa email mengandung karakter `'@'` dan `'.'`. Jika tidak, akan menampilkan pesan kesalahan:  
   `"Email harus mengandung karakter '@' dan '.'."`

## Alur Program

1. Program menerima input dari pengguna:
   - Nama lengkap
   - Nomor telepon
   - Email

2. Fungsi `validate_form(name, phone, email)` memvalidasi data input berdasarkan aturan validasi.

3. Jika ada kesalahan, program akan menampilkan pesan kesalahan untuk setiap input yang tidak valid.

4. Jika semua input valid, program akan menampilkan pesan:  
   `"Data pendaftaran valid."`

## Contoh Penggunaan

Berikut adalah contoh input dan output program:

### Input
```
Masukkan nama lengkap: John123
Masukkan nomor telepon: 12345abc
Masukkan email: exampleemail.com
```

### Output
```
Data tidak valid:
- Nama lengkap harus hanya berisi huruf.
- Nomor telepon harus hanya berisi angka.
- Email harus mengandung karakter '@' dan '.'.
```

### Input Lain
```
Masukkan nama lengkap: John Doe
Masukkan nomor telepon: 1234567890
Masukkan email: john.doe@example.com
```

### Output
```
Data pendaftaran valid.
```

## Cara Menjalankan

1. Pastikan Python sudah terinstal di komputer Anda.
2. Simpan kode program ke dalam file Python, misalnya `validate_form.py`.
3. Jalankan file menggunakan perintah:
   ```
   python validate_form.py
   ```
4. Masukkan data sesuai dengan permintaan program.
