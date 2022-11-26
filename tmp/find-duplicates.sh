find / -type f -exec md5sum {} \; > md5sums
gawk '{print $1}' md5sums | sort | uniq -d > dupes
while read d; do echo "---"; grep $d md5sums | cut -d ' ' -f 2-; done < dupes 