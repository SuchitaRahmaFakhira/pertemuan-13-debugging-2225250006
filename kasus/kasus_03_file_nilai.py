def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


nilai_mahasiswa = [80, 60, 90, 70]

print("Data Nilai Mahasiswa:", nilai_mahasiswa)
print("Rata-rata:", hitung_rata_rata(nilai_mahasiswa))

for nilai in nilai_mahasiswa:
    print("Nilai:", nilai, "-", status_lulus(nilai))