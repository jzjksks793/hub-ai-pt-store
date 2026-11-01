#!/usr/bin/env sh
# Daftar model FREE dan info key + sisa saldo.
set -eu
: "${HUB_AI_KEY:?Isi dulu: export HUB_AI_KEY=pt-store-...}"
BASE="https://api.ptstore.my.id/v1"

echo "== Model FREE =="
curl -s "$BASE/models" -H "Authorization: Bearer ${HUB_AI_KEY}"
echo
echo "== Model PREMIUM =="
curl -s "$BASE/premium/models" -H "Authorization: Bearer ${HUB_AI_KEY}"
echo
echo "== Info key dan saldo =="
curl -s "$BASE/me" -H "Authorization: Bearer ${HUB_AI_KEY}"
echo
