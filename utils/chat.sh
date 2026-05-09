#!/usr/bin/env bash
set -euo pipefail
PROMPT="${1:?Usage: chat.sh <prompt> [model]}"
MODEL="${2:-sonar-pro}"

curl -s -X POST https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer ${PERPLEXITY_API_KEY}" \
  -H "content-type: application/json" \
  -d "{\"model\":\"${MODEL}\",\"max_tokens\":1024,\"messages\":[{\"role\":\"user\",\"content\":\"${PROMPT}\"}]}" \
  | python3 -c "import sys,json;print(json.load(sys.stdin)['choices'][0]['message']['content'])"
