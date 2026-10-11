#!/bin/sh
# Copy the built site into docs/ and keep docs/CNAME if GitHub Pages added one
# (custom domain www.puheklinikka.net, set by Nana in Settings > Pages).
set -e
cd "$(dirname "$0")/.."
git pull -q origin main
CNAME=""
[ -f docs/CNAME ] && CNAME="$(cat docs/CNAME)"
rm -rf docs
cp -r /mnt/project-files/site-build/site docs
if [ -n "$CNAME" ]; then
  printf '%s\n' "$CNAME" > docs/CNAME
  echo "kept docs/CNAME: $CNAME"
fi
