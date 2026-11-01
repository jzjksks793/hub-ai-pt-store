"""Streaming dengan LangChain.

Install: pip install langchain-openai
Jalankan: HUB_AI_KEY=pt-store-... python langchain_stream.py
"""
import os

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model=os.environ.get("HUB_AI_MODEL", "hubai/laguna-s-2.1"),
    api_key=os.environ["HUB_AI_KEY"],
    base_url=os.environ.get("HUB_AI_BASE_URL", "https://api.ptstore.my.id/v1"),
    streaming=True,
)

for part in llm.stream("Halo!"):
    print(part.content, end="", flush=True)
print()
