# Ringkasan API

API kompatibel dengan OpenAI. Dokumentasi resmi dan terbaru ada di https://hub-ai.ptstore.my.id/docs; halaman ini ringkasannya.

- **Base URL:** `https://api.ptstore.my.id/v1`
- **Autentikasi:** header `Authorization: Bearer API_KEY` (key dibuat di [Dashboard](https://hub-ai.ptstore.my.id/dashboard))
- **Format ID model:** `hubai/nama-model`

## Endpoint

| Method | Path | Fungsi |
| --- | --- | --- |
| POST | `/v1/chat/completions` | Chat, model FREE |
| POST | `/v1/premium/chat/completions` | Chat, khusus model PREMIUM |
| POST | `/v1/cf/chat/completions` | Chat, model FREE jalur tambahan |
| POST | `/v1/cf/vision` | Baca dan jelaskan gambar |
| POST | `/v1/cf/images/generations` | Buat gambar |
| POST | `/v1/audio/speech` | Teks ke suara |
| POST | `/v1/cf/audio/speech` | Teks ke suara, jalur tambahan |
| GET | `/v1/models` | Daftar model FREE |
| GET | `/v1/premium/models` | Daftar model PREMIUM |
| GET | `/v1/me` | Info key dan sisa saldo |
| GET | `/v1/me/stats` | Statistik pemakaian key |
| GET | `/v1/model-status` | Model yang sedang gangguan |

## Streaming

Jawaban selalu dikirim bertahap sebagai server-sent events, sama seperti OpenAI. Sertakan `"stream": true` di body.

## Fallback model (opsional)

Dua field boolean di body chat, keduanya `false` secara default, jadi request tidak pernah dialihkan ke model lain tanpa izinmu.

| Field | Fungsi |
| --- | --- |
| `allow_fallback` | Boleh mengalihkan ke model lain kalau model pilihanmu gagal. Prompt dikirim ke model pengganti yang mungkin berbeda provider. |
| `allow_fallback_cross_provider` | Boleh mengalihkan lintas provider. Hanya berlaku kalau `allow_fallback` juga `true`. |

Kalau pengalihan terjadi, respons membawa header `X-Fallback-From`, `X-Fallback-Provider`, dan `X-Model-Used`.
