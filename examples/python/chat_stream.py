"""Chat streaming dengan OpenAI SDK.

Install: pip install openai
Jalankan: HUB_AI_KEY=pt-store-... python chat_stream.py
"""
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["HUB_AI_KEY"],
    base_url=os.environ.get("HUB_AI_BASE_URL", "https://api.ptstore.my.id/v1"),
)

stream = client.chat.completions.create(
    model=os.environ.get("HUB_AI_MODEL", "hubai/laguna-s-2.1"),
    messages=[{"role": "user", "content": "Halo!"}],
    stream=True,
)

for chunk in stream:
    # Potongan terakhir berisi data pemakaian token dan choices-nya kosong.
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
