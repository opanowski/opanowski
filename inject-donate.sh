#!/bin/bash

SNIPPET='<script src="/opanowski/donate-widget.js"></script>'

for file in $(find . -name "*.html"); do
  if grep -q "donate-widget.js" "$file"; then
    echo "SKIP (sudah ada): $file"
  elif grep -q "</body>" "$file"; then
    sed -i '' "s|</body>|$SNIPPET\n</body>|" "$file"
    echo "OK inject: $file"
  else
    echo "SKIP (no </body>): $file"
  fi
done

echo ""
echo "Selesai! Semua file sudah diinject."
