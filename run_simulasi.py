# Simulasi Model Ising 2D
# Anggota Kelompok:
# 1. Eki Permata Cahya Hati (NIM: 01231007)
# 2. Melky Juli Kurniawan Silalahi (NIM: 01231010)
# 3. Yustiara Sampe Manggoali (NIM: 01231019)

import numpy as np
import matplotlib.pyplot as plt

# Parameter dasar untuk simulasi
ukuran_kisi = 20
suhu = 1.0
jumlah_langkah = 200000

# Mulai dengan membuat papan spin acak (Hot Start)
papan_spin = np.random.choice([-1, 1], size=(ukuran_kisi, ukuran_kisi))

# Wadah untuk mencatat perubahan magnetisasi
catatan_magnetisasi = []

# --- Simulasi Ising ---

# 1. Menghitung perubahan energi
def hitung_energi_tetangga(kisi, i, j):
    spin = kisi[i, j]
    # Mencari tetangga atas, bawah, kiri, kanan
    # Menggunakan % ukuran_kisi agar tidak error di pinggir kisi
    atas = kisi[(i-1) % ukuran_kisi, j]
    bawah = kisi[(i+1) % ukuran_kisi, j]
    kiri = kisi[i, (j-1) % ukuran_kisi]
    kanan = kisi[i, (j+1) % ukuran_kisi]
    
    total_tetangga = atas + bawah + kiri + kanan
    delta_e = 2 * spin * total_tetangga
    return delta_e

# 2. Proses simulasi
print("Menjalankan simulasi Model Ising 2D...")
for langkah in range(jumlah_langkah):
    # Pilih koordinat acak
    i = np.random.randint(0, ukuran_kisi)
    j = np.random.randint(0, ukuran_kisi)
    
    perubahan = hitung_energi_tetangga(papan_spin, i, j)
    
    # Kriteria Metropolis
    if perubahan < 0:
        # Jika energi turun, terima perubahan
        papan_spin[i, j] = papan_spin[i, j] * -1
    else:
        # Jika energi naik, cek peluang
        peluang = np.exp(-perubahan / suhu)
        if np.random.rand() < peluang:
            papan_spin[i, j] = papan_spin[i, j] * -1
            
    # Catat data
    if langkah % 100 == 0:
        rata_rata = np.mean(papan_spin)
        catatan_magnetisasi.append(rata_rata)

print("Simulasi selesai. Menampilkan grafik...")
plt.figure(figsize=(12, 5))

# Plot kondisi akhir kisi
plt.subplot(1, 2, 1)
plt.imshow(papan_spin, cmap='binary', vmin=-1, vmax=1)
plt.title(f"Konfigurasi Spin Akhir (T={suhu})")
plt.colorbar(label="Arah Spin")

# Plot grafik magnetisasi
plt.subplot(1, 2, 2)
plt.plot(catatan_magnetisasi, color='blue')
plt.title("Riwayat Magnetisasi")
plt.xlabel("Iterasi (x100)")
plt.ylabel("Magnetisasi Rata-rata")
plt.grid(True)

plt.tight_layout()
plt.show()
