#!/bin/bash
# while true; do
echo "converting WEBP files to PNGs"
  for file in /Users/human/src/*.webp; do
    if [ -f "$file" ]; then
    echo ""
      webp_file="$file"
      echo "$webp_file"
      png_file="${webp_file%.*}.png"
      echo "$png_file"
      dwebp "$webp_file" -o "$png_file"
      cp "$png_file" "./pngs_out/"
      echo "done"
      echo ""
    fi
  done;
echo "process complete"