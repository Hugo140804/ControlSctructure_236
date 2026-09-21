"""Nomor 2 - Mencari angka terbesar dari tiga angka (if / elif / else).

Write a PYTHON program to find largest of three numbers.

Pengguna memasukkan tiga bilangan bulat, lalu program mencetak angka terbesar.
Jika ada angka yang nilainya sama, nilai tersebut tetap dianggap terbesar.
"""


def angka_terbesar(a, b, c):
    """Mengembalikan angka terbesar di antara a, b, dan c.

    Args:
        a (int): Bilangan pertama.
        b (int): Bilangan kedua.
        c (int): Bilangan ketiga.

    Returns:
        int: Nilai terbesar dari ketiga bilangan.
    """
    if a >= b and a >= c:
        return a
    if b >= c:
        return b
    return c


def main():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    c = int(input("Masukkan angka ketiga: "))

    print("Angka terbesar:", angka_terbesar(a, b, c))


if __name__ == "__main__":
    main()