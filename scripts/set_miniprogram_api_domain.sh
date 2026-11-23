#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: scripts/set_miniprogram_api_domain.sh https://api.example.com"
  exit 1
fi

DOMAIN="$1"
DOMAIN="${DOMAIN%/}"

case "$DOMAIN" in
  https://*)
    ;;
  *)
    echo "ERROR: domain must start with https://"
    exit 1
    ;;
esac

if [[ "$DOMAIN" == *"127.0.0.1"* || "$DOMAIN" == *"localhost"* ]]; then
  echo "ERROR: trial/release domain cannot be localhost or 127.0.0.1"
  exit 1
fi

API_BASE="${DOMAIN}/python7i67w282/"

FILES=(
  "python7i67w282/api/templates/front/front/api/base.js"
  "mp-weixin/common/vendor.js"
  "mp-weixin/pages/ai-assistant/ai-assistant.js"
  "docs/miniprogram-release-api-checklist.md"
  ".ai-memory/current_status.md"
  ".ai-memory/handoff.md"
)

for file in "${FILES[@]}"; do
  if [ -f "$file" ]; then
    perl -0pi -e "s#https://YOUR_HTTPS_DOMAIN/python7i67w282/#${API_BASE}#g" "$file"
    perl -0pi -e "s#https://api\\.example\\.com/python7i67w282/#${API_BASE}#g" "$file"
  fi
done

echo "Mini-program release API base set to: ${API_BASE}"
echo "Remember to configure WeChat Platform server domains with: ${DOMAIN}"
