#!/usr/bin/env sh
# Chat dengan streaming. Butuh: export HUB_AI_KEY="pt-store-..."
set -eu
: "${HUB_AI_KEY:?Isi dulu: export HUB_AI_KEY=pt-store-...}"
MODEL="${HUB_AI_MODEL:-hubai/laguna-s-2.1}"

curl -N https://api.ptstore.my.id/v1/chat/completions \
  -H "Authorization: Bearer ${HUB_AI_KEY}" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"${MODEL}\",\"stream\":true,\"messages\":[{\"role\":\"user\",\"content\":\"Halo!\"}]}"
