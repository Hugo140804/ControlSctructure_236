# Control Structure 236

Kumpulan latihan **struktur kontrol** (percabangan dan perulangan) pada bahasa
**Python** untuk mata kuliah Pemrograman Multiplatform — Pertemuan 2.

## Daftar Program

| File | Materi | Deskripsi |
| --- | --- | --- |
| [`Nomor1.py`](Nomor1.py) | `if` / `elif` / `else` | *Evaluate the student performance* — `>=90` Excellent, `>=80` Very Good, `>=70` Good, `>=60` Average. |
| [`Nomor2.py`](Nomor2.py) | `if` / `elif` / `else` | *Find largest of three numbers* — mencari bilangan bulat terbesar dari tiga input. |
| [`Nomor3.py`](Nomor3.py) | `while` | *Print Fibonacci series up to n* — mencetak deret Fibonacci sampai batas `n`. |
| [`Nomor4.py`](Nomor4.py) | `for` | *Print odd numbers up to n* — mencetak bilangan ganjil dari 1 sampai `n`. |
| [`Nomor5.py`](Nomor5.py) | nested `for` | *Produce following design* — pola segitiga angka (baris ke-`i` berisi angka `i` sebanyak `i` kali). |

## Prasyarat

- Python 3.8 atau lebih baru (diuji pada Python 3.14).

Cek versi Python yang terpasang:

```bash
python --version
```

## Cara Menjalankan

Jalankan salah satu file, lalu masukkan nilai saat program meminta input:

```bash
python Nomor1.py
```

Contoh sesi `Nomor1.py`:

```text
Masukkan nilai: 85
Very Good performance
```

Contoh sesi `Nomor2.py`:

```text
Masukkan angka pertama: 10
Masukkan angka kedua: 7
Masukkan angka ketiga: 25
Angka terbesar: 25
```

Contoh sesi `Nomor3.py`:

```text
Masukkan batas nilai n: 20
0 1 1 2 3 5 8 13
```

Contoh sesi `Nomor5.py`:

```text
Masukkan nilai n: 4
1
2 2
3 3 3
4 4 4 4
```

## Catatan Desain

Setiap file mengikuti struktur yang sama agar mudah dibaca dan diuji:

1. **Docstring modul** — menjelaskan tujuan dan aturan program.
2. **Fungsi logika murni** (mis. `tentukan_predikat`, `deret_fibonacci`) —
   menerima parameter dan mengembalikan nilai, sehingga bisa diuji tanpa input.
3. **`main()`** — hanya menangani input/output (I/O).
4. **Guard `if __name__ == "__main__":`** — file bisa dijalankan langsung
   maupun diimpor sebagai modul tanpa efek samping.

## Struktur Repositori

```text
.
├── .gitignore
├── README.md
├── Nomor1.py
├── Nomor2.py
├── Nomor3.py
├── Nomor4.py
└── Nomor5.py
```
