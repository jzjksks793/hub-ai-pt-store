# HUB AI PT STORE

[![Lisensi: MIT](https://img.shields.io/badge/lisensi-MIT-3ddc97.svg)](LICENSE)
[![CI](https://github.com/jzjksks793/hub-ai-pt-store/actions/workflows/ci.yml/badge.svg)](https://github.com/jzjksks793/hub-ai-pt-store/actions/workflows/ci.yml)
[![API: OpenAI-compatible](https://img.shields.io/badge/API-OpenAI--compatible-5bc0eb.svg)](docs/api.md)
[![Website](https://img.shields.io/badge/website-hub--ai.ptstore.my.id-3ddc97.svg)](https://hub-ai.ptstore.my.id)

Satu API untuk banyak model AI, **kompatibel dengan OpenAI**. Ganti base URL dan API key, kode lamamu langsung jalan. Model FREE bisa dipakai tanpa kartu kredit; model PREMIUM memakai saldo AI Credit.

Repo ini berisi **contoh kode dan dokumentasi** untuk memakai HUB AI. Layanannya sendiri berjalan di [https://hub-ai.ptstore.my.id](https://hub-ai.ptstore.my.id).

## Mulai cepat

1. Buka [Dashboard](https://hub-ai.ptstore.my.id/dashboard), masuk dengan akun Google, lalu buat API key (berawalan `pt-store-`).
2. Pakai base URL `https://api.ptstore.my.id/v1`.

```bash
export HUB_AI_KEY="pt-store-..."

curl -N https://api.ptstore.my.id/v1/chat/completions \
  -H "Authorization: Bearer $HUB_AI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"hubai/laguna-s-2.1","stream":true,"messages":[{"role":"user","content":"Halo!"}]}'
```

Cari ID model di [halaman model](https://hub-ai.ptstore.my.id/model) atau panggil `GET /v1/models`. ID model berformat `hubai/nama-model`.

## Isi repo

| Folder | Isi |
| --- | --- |
| [`examples/curl`](examples/curl) | Contoh curl: chat, daftar model, cek saldo |
| [`examples/python`](examples/python) | OpenAI SDK dan LangChain |
| [`examples/node`](examples/node) | OpenAI SDK untuk Node.js |
| [`docs/api.md`](docs/api.md) | Ringkasan endpoint, streaming, fallback |
| [`docs/integrations.md`](docs/integrations.md) | Cline, Cursor, Continue, Open WebUI, n8n |
| [`docs/limits-and-errors.md`](docs/limits-and-errors.md) | Kuota, batas request, kode error |

## Batasan yang perlu diketahui

- Jawaban selalu dikirim bertahap (streaming), jadi kirim `"stream": true`.
- `tools` dan function calling **belum diteruskan**. Mode Agent di Cursor atau agent dengan tools di n8n belum jalan.
- Batas **18 request per menit** untuk tiap API key.
- Model FREE memakai kuota 500.000 token per key; kalau habis, tunggu 1 menit sampai reset otomatis.

Detail lengkap: [docs/limits-and-errors.md](docs/limits-and-errors.md).

## HUB AI CLI

Ada juga aplikasi terminal resmi untuk chat dan mode agent. Butuh Node.js 18 atau lebih baru. Panduan install ada di [halaman integrasi](https://hub-ai.ptstore.my.id/integrasi).

## Keamanan

- Jangan menyimpan API key di repository publik atau kode front-end. Pakai variabel lingkungan (lihat [`.env.example`](.env.example)).
- Menemukan celah keamanan? Baca [SECURITY.md](SECURITY.md).

## Kontak

Email: [hub-ai@ptstore.my.id](mailto:hub-ai@ptstore.my.id) · [Halaman kontak](https://hub-ai.ptstore.my.id/kontak)

## Kontribusi

Perbaikan dokumentasi dan contoh kode sangat diterima. Baca [CONTRIBUTING.md](CONTRIBUTING.md).

## Tautan

[Website](https://hub-ai.ptstore.my.id) · [Dokumentasi](https://hub-ai.ptstore.my.id/docs) · [Harga](https://hub-ai.ptstore.my.id/pricing) · [Status model](https://hub-ai.ptstore.my.id/status) · [FAQ](https://hub-ai.ptstore.my.id/faq) · [TikTok](https://www.tiktok.com/@hubai_ptstore)

## Lisensi

[MIT](LICENSE). Lisensi ini berlaku untuk isi repo ini (contoh kode dan dokumentasi), bukan untuk layanan HUB AI.
