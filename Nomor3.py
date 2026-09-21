"""Nomor 3 - Mencetak deret Fibonacci sampai batas n (while loop).

Pengguna memasukkan batas n, lalu program mencetak seluruh bilangan
Fibonacci yang nilainya tidak lebih besar dari n.
"""


def deret_fibonacci(batas):
    """Mengembalikan list bilangan Fibonacci yang <= batas."""
    hasil = []
    a, b = 0, 1
    while a <= batas:
        hasil.append(a)
        a, b = b, a + b
    return hasil


def main():
    n = int(input("Masukkan batas nilai n: "))
    print(*deret_fibonacci(n))


if __name__ == "__main__":
    main()