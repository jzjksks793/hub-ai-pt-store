"""Cek info key dan sisa saldo lewat GET /v1/me (hanya library standar)."""
import json
import os
import urllib.request

base = os.environ.get("HUB_AI_BASE_URL", "https://api.ptstore.my.id/v1")
req = urllib.request.Request(
    f"{base}/me",
    headers={"Authorization": f"Bearer {os.environ['HUB_AI_KEY']}"},
)
with urllib.request.urlopen(req, timeout=30) as res:
    print(json.dumps(json.load(res), indent=2, ensure_ascii=False))
