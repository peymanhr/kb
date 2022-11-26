# Symlink to same file with different extension


```bash
find foo -name "*.mp4" -exec bash -c 'ln -s "$(basename "{}")"  "$(sed "s/\(.*\)\.mp4$/\1.m4v/" <<< "{}")"' \;
```
