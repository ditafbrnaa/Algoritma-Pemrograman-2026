r = float(input("Masukkan jari-jari lingkaran (r): "))

if r < 0:
    print("Peringatan: Jari-jari tidak boleh bernilai negatif!")
else:
    PHI = 3.14159
    luas = PHI * r * r
    keliling = 2 * PHI * r

    print("Luas Lingkaran     :", round(luas, 2))
    print("Keliling Lingkaran :", round(keliling, 2))
