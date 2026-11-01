# Kuota, batas, dan error

| Hal | Aturan |
| --- | --- |
| Kuota model FREE | 500.000 token per key. Kalau habis, tunggu 1 menit sampai reset otomatis; key tidak dihapus. |
| Model PREMIUM | Memotong saldo AI Credit sesuai token yang dipakai. |
| Batas request | 18 request per menit untuk tiap API key. |
| Streaming | Wajib. Kirim `"stream": true`. |
| Function calling / `tools` | Belum diteruskan. |

## Error umum

| Gejala | Penyebab dan solusi |
| --- | --- |
| `429` | Terlalu banyak request dalam waktu singkat. Tunggu beberapa detik lalu coba lagi. Tools yang banyak mengirim request (Cline, Open WebUI) bisa kena batas ini. |
| Model "overload" | Provider sedang sibuk atau gangguan. Pilih model lain atau cek [status model](https://hub-ai.ptstore.my.id/status). |
| Kuota FREE habis | Tunggu 1 menit, atau top up AI Credit lalu pakai model PREMIUM dengan key yang sama. |
| Top up belum masuk | Pastikan nominal sama persis dengan total di halaman Top Up (termasuk kode unik), lalu tekan "Saya sudah bayar". |

Lebih lengkap: [FAQ](https://hub-ai.ptstore.my.id/faq).
