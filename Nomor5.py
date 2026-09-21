"""Nomor 5 - Mencetak pola segitiga angka (nested loop).

Pengguna memasukkan nilai n, lalu program mencetak pola berikut:

    1
    2 2
    3 3 3
    ...

Baris ke-i berisi angka i yang dicetak sebanyak i kali, untuk i = 1..n.
"""


def pola_segitiga(n):
    """Mengembalikan list of list; baris ke-i berisi angka i sebanyak i kali."""
    return [[i] * i for i in range(1, n + 1)]


def main():
    n = int(input("Masukkan nilai n: "))

    for baris in pola_segitiga(n):
        print(*baris)


if __name__ == "__main__":
    main()