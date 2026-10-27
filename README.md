Pertemuan 13 - Debugging dan Testing

Nama: Suchita Rahma Fakhira
NIM: 2225250006
Kelas: 3B

Kasus

Praktik ini membahas debugging, tracing, dan testing pada program Python. Tiga contoh kasus pendukung membahas kesalahan batas kelulusan, kesalahan perhitungan rata-rata, dan penanganan file nilai yang tidak ditemukan.

Pada Praktik 4, program awal memiliki tiga bug, yaitu kesalahan pada perhitungan rata-rata, penentuan status kelulusan, dan pencarian nilai tertinggi.

Test Case

ID| Input| Expected| Actual Awal| Status
T1| Rata-rata "[80, 60, 90, 70]"| 75.0| 60.0| FAIL
T2| Rata-rata "[100, 80]"| 90.0| 36.0| FAIL
T3| Status nilai 60| Lulus| Tidak lulus| FAIL
T4| Status nilai 59| Tidak lulus| Tidak lulus| PASS
T5| Nilai tertinggi "[80, 60, 90, 70]"| 90| 0| FAIL

Bug Report

Bug 1 — Perhitungan rata-rata

- Lokasi: fungsi "hitung_rata_rata()".
- Gejala: hasil rata-rata tidak sesuai.
- Penyebab: pembagi ditetapkan 5 meskipun jumlah data berbeda.
- Perbaikan: membagi jumlah nilai dengan banyaknya data menggunakan "len(nilai)".

Bug 2 — Status kelulusan

- Lokasi: fungsi "status()".
- Gejala: nilai 60 dinyatakan tidak lulus.
- Penyebab: kondisi menggunakan "nilai > 60".
- Perbaikan: mengubah kondisi menjadi "nilai >= 60".

Bug 3 — Nilai tertinggi

- Lokasi: fungsi "nilai_tertinggi()".
- Gejala: nilai tertinggi yang dihasilkan adalah 0.
- Penyebab: nilai awal dan perbandingan dalam perulangan tidak tepat.
- Perbaikan: menggunakan elemen pertama sebagai nilai awal dan membandingkan nilai berikutnya dengan ">".

Retest

ID| Input| Expected| Actual Setelah Perbaikan| Status
T1| Rata-rata "[80, 60, 90, 70]"| 75.0| 75.0| PASS
T2| Rata-rata "[100, 80]"| 90.0| 90.0| PASS
T3| Status nilai 60| Lulus| Lulus| PASS
T4| Status nilai 59| Tidak lulus| Tidak lulus| PASS
T5| Nilai tertinggi "[80, 60, 90, 70]"| 90| 90| PASS

Setelah perbaikan dilakukan, seluruh test case dijalankan kembali. Hasil aktual sesuai dengan hasil yang diharapkan dan seluruh pengujian berstatus PASS.

Cara Menjalankan

python3 praktik/praktik_4_debugging.py

Refleksi

Debugging membantu menemukan dan memperbaiki kesalahan pada program. Tracing membantu memahami alur eksekusi serta perubahan nilai variabel. Testing digunakan untuk membandingkan hasil aktual dengan hasil yang diharapkan. Dengan menggunakan beberapa test case, program dapat diuji melalui berbagai masukan untuk memastikan perbaikan berjalan dengan benar.
