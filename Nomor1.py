"""Nomor 1 - Student performance (if / elif / else).

Write a PYTHON program to evaluate the student performance.

Pengguna memasukkan sebuah nilai (%), lalu program mencetak predikatnya:
    >= 90 -> Excellent performance
    >= 80 -> Very Good performance
    >= 70 -> Good performance
    >= 60 -> Average performance
    <  60 -> Poor performance
"""


def tentukan_predikat(nilai):
    """Mengembalikan predikat (str) berdasarkan nilai persen.

    Args:
        nilai (float): Nilai siswa dalam persen.

    Returns:
        str: Salah satu dari "Excellent performance", "Very Good performance",
            "Good performance", "Average performance", atau "Poor performance".
    """
    if nilai >= 90:
        return "Excellent performance"
    if nilai >= 80:
        return "Very Good performance"
    if nilai >= 70:
        return "Good performance"
    if nilai >= 60:
        return "Average performance"
    return "Poor performance"


def main():
    nilai = int(input("Masukkan nilai: "))
    print(tentukan_predikat(nilai))


if __name__ == "__main__":
    main()
