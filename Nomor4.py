"""Nomor 4 - Mencetak bilangan ganjil dari 1 sampai n (for loop).

Pengguna memasukkan nilai n, lalu program mencetak semua bilangan ganjil
di antara 1 dan n secara berurutan.
"""


def bilangan_ganjil(n):
    """Mengembalikan list bilangan ganjil dari 1 sampai n."""
    return [angka for angka in range(1, n + 1) if angka % 2 != 0]


def main():
    n = int(input("Masukkan nilai n: "))
    print(*bilangan_ganjil(n))


if __name__ == "__main__":
    main()