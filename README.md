Pertemuan 13 - Debugging dan Testing

Nama: Suchita Rahma Fakhira
NIM: 2225250006
Kelas: 3B

Kasus

Praktik ini membahas debugging, tracing, dan testing pada program Python. Tiga contoh kasus pendukung membahas kesalahan batas kelulusan, kesalahan perhitungan rata-rata, dan penanganan file nilai yang tidak ditemukan.

Pada Praktik 4, program awal memiliki tiga bug, yaitu kesalahan pada perhitungan rata-rata, penentuan status kelulusan, dan pencarian nilai tertinggi.

Test Case

<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Input</th>
      <th>Expected</th>
      <th>Actual Awal</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>T1</td>
      <td>Rata-rata [80, 60, 90, 70]</td>
      <td>75.0</td>
      <td>60.0</td>
      <td>FAIL</td>
    </tr>
    <tr>
      <td>T2</td>
      <td>Rata-rata [100, 80]</td>
      <td>90.0</td>
      <td>36.0</td>
      <td>FAIL</td>
    </tr>
    <tr>
      <td>T3</td>
      <td>Status nilai 60</td>
      <td>Lulus</td>
      <td>Tidak lulus</td>
      <td>FAIL</td>
    </tr>
    <tr>
      <td>T4</td>
      <td>Status nilai 59</td>
      <td>Tidak lulus</td>
      <td>Tidak lulus</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>T5</td>
      <td>Nilai tertinggi [80, 60, 90, 70]</td>
      <td>90</td>
      <td>0</td>
      <td>FAIL</td>
    </tr>
  </tbody>
</table>

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

<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Input</th>
      <th>Expected</th>
      <th>Actual Setelah Perbaikan</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>T1</td>
      <td>Rata-rata [80, 60, 90, 70]</td>
      <td>75.0</td>
      <td>75.0</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>T2</td>
      <td>Rata-rata [100, 80]</td>
      <td>90.0</td>
      <td>90.0</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>T3</td>
      <td>Status nilai 60</td>
      <td>Lulus</td>
      <td>Lulus</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>T4</td>
      <td>Status nilai 59</td>
      <td>Tidak lulus</td>
      <td>Tidak lulus</td>
      <td>PASS</td>
    </tr>
    <tr>
      <td>T5</td>
      <td>Nilai tertinggi [80, 60, 90, 70]</td>
      <td>90</td>
      <td>90</td>
      <td>PASS</td>
    </tr>
  </tbody>
</table>

Setelah perbaikan dilakukan, seluruh test case dijalankan kembali. Hasil aktual sesuai dengan hasil yang diharapkan dan seluruh pengujian berstatus PASS.

Cara Menjalankan

python3 praktik/praktik_4_debugging.py

Refleksi

Debugging membantu menemukan dan memperbaiki kesalahan pada program. Tracing membantu memahami alur eksekusi serta perubahan nilai variabel. Testing digunakan untuk membandingkan hasil aktual dengan hasil yang diharapkan. Dengan menggunakan beberapa test case, program dapat diuji melalui berbagai masukan untuk memastikan perbaikan berjalan dengan benar.
