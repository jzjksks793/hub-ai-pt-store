# Integrasi dengan tools populer

Untuk semua tools, pakai:

- **Base URL:** `https://api.ptstore.my.id/v1` (model PREMIUM: `https://api.ptstore.my.id/v1/premium`)
- **API key:** dari [Dashboard](https://hub-ai.ptstore.my.id/dashboard)
- **Model ID:** misalnya `hubai/laguna-s-2.1`

Pengaturan yang terisi otomatis ada di [halaman integrasi](https://hub-ai.ptstore.my.id/integrasi).

## Cline (VS Code)

1. Buka panel Cline, klik ikon roda gigi.
2. Pada **API Provider**, pilih **OpenAI Compatible**.
3. Isi Base URL, API Key, dan Model ID, lalu simpan.

Cline mengirim instruksi panjang di setiap request, jadi satu permintaan bisa memakai ribuan token. Untuk pemakaian rutin, model PREMIUM lebih tenang.

## Cursor

1. Buka **Cursor Settings** lalu menu **Models**.
2. Isi kolom key OpenAI dengan API key-mu.
3. Aktifkan **Override OpenAI Base URL** dan isi Base URL.
4. Klik **Add model**, tulis Model ID, lalu pilih di chat.

Mode Agent (butuh function calling) belum didukung. Nama menu Cursor bisa berubah; cari "Override OpenAI Base URL".

## Continue (VS Code / JetBrains)

Tambahkan di `config.yaml` (ganti `ISI_API_KEY` dengan key-mu, jangan di-commit):

```yaml
name: HUB AI
version: 1.0.0
schema: v1
models:
  - name: HUB AI
    provider: openai
    model: hubai/laguna-s-2.1
    apiBase: https://api.ptstore.my.id/v1
    apiKey: ISI_API_KEY
    roles:
      - chat
      - edit
```

## Open WebUI

Lewat menu: **Admin Panel > Settings > Connections > OpenAI API > +**, isi URL dan API key.

Lewat Docker:

```bash
docker run -d -p 3000:8080 \
  -e OPENAI_API_BASE_URL=https://api.ptstore.my.id/v1 \
  -e OPENAI_API_KEY=$HUB_AI_KEY \
  -v open-webui:/app/backend/data \
  --name open-webui ghcr.io/open-webui/open-webui:main
```

Judul chat otomatis ikut memakai kuota dan batas 18 request per menit; matikan kalau sering kena batas.

## n8n

Pakai node **Basic LLM Chain** dengan **OpenAI Chat Model**. Buat credential baru dengan API key dan Base URL, lalu pada Model pilih mode **By ID**. Node **AI Agent** dengan tools belum jalan karena function calling belum diteruskan.
