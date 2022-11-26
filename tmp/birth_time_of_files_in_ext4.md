# دستور stat و زمان ایجاد فایل (Birth) در ext4

فایل سیستم ext توی metadata هر فایل چهار تا زمان مختلف ذخیره می‌کنه.

‏crtime زمان پیدایش فایل
‏mtime زمان آخرین ویرایش محتوی
‏ctime زمان آخرین تغییر در محتوی یا متادیتا (inode)
‏atime زمان آخرین خوانده شدن (access) - با در نظر گرفتن mount option پیشفرض relatime

زمانی که با دستور stat وضعیت یک فایل را بررسی می‌کنید شاید متوجه شده باشید که زمان ایجاد فایل یا Birth خالیه.

```
‏peyman@ubutnu:~$ stat /etc/passwd
‏  File: '/etc/passwd'
‏  Size: 2653      	Blocks: 8          IO Block: 4096   regular file
‏Device: 801h/2049d	Inode: 277706      Links: 1
‏Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
‏Access: 2017-12-01 23:19:19.680000000 +0330
‏Modify: 2017-07-20 19:23:40.013463855 +0430
‏Change: 2017-07-20 19:23:40.017463781 +0430
‏ Birth: -
```

اینطور به نظر می‌آید که فایل سیستم، btime (همان crtime در ext) را ذخیره نمی‌کنه. اما مشکل از فایل سیستم نیست و birth‪-‬time به درستی در inode ذخیره می‌شه. در واقع این نسخه گنویی ابزار stat است که آن را نمی‌خواند. 

```
‏peyman@ubutnu:~$ stat --format=%w /etc/passwd
-
```

با اینکه gnulib در حال حاظر از خواندن btime پشتیبانی می‌کند، در ابزار stat هیج کس تا حالا کدی برای استفاده از این قابلیت ماژول stat-times ننوشته است.

تنها راه برای بدست آوردن زمان ایجاد یک فایل در ext، استخراج مستقیم آن از بلاک دیوایس با کمک ابزار debugfs است.

```
‏peyman@ubutnu:~$ sudo debugfs -R 'stat /etc/passwd' /dev/sda1

‏Inode: 277706   Type: regular    Mode:  0644   Flags: 0x80000
‏Generation: 3949810765    Version: 0x00000000:00000001
‏User:     0   Group:     0   Size: 2653
‏File ACL: 0    Directory ACL: 0
‏Links: 1   Blockcount: 8
‏Fragment:  Address: 0    Number: 0    Size: 0
‏ ctime: 0x5970c3f4:0429e794 -- Thu Jul 20 19:23:40 2017
‏ atime: 0x5a21b23f:a21fe800 -- Fri Dec  1 23:19:19 2017
‏ mtime: 0x5970c3f4:0335c4bc -- Thu Jul 20 19:23:40 2017
‏crtime: 0x5970c3f4:0335c4bc -- Thu Jul 20 19:23:40 2017
‏Size of extra inode fields: 32
‏EXTENTS:
(0):1649974
‏(END)
```

برای راحت تر شدن کار می تونیم یک تابع توی `~/.bashrc` بنویسیم که اسم فایلها را از آرگومان بگیره و btime اونها را برگردونه.

```
‏btime() {
‏  for file in "${@}"; do
‏    inode=$(ls -di "${file}" | cut -d ' ' -f 1)
‏    fs=$(df "${file}"  | tail -1 | awk '{print $1}')
‏    crtime=$(sudo debugfs -R 'stat <'"${inode}"'>' "${fs}" 2>/dev/null | 
‏    grep -oP 'crtime.*--\s*\K.*')
‏    printf "%s\t%s\n" "${crtime}" "${file}"
‏  done
}
```

و اینجوری اجراش می‌کنیم.

```
‏peyman@ubutnu:~$ btime /etc/python*
‏Thu Jul 20 17:30:10 2017	/etc/python
‏Thu Jul 20 17:30:10 2017	/etc/python2.7
‏Thu Jul 20 17:30:10 2017	/etc/python3
‏Thu Jul 20 17:30:10 2017	/etc/python3.5
```

فقط یک نکته ای وجود داره. birth time برای فایل سیستمی که اندازه‌ی inode آن ۱۲۸ بایت باشه به دلیل محدودیت فضای آینود ذخیره نمیشه.

با ابزار tune2fs میتوانیم inode size یک پارتیشن را ببینیم.

```
‏peyman@ubutnu:~$ sudo tune2fs -l /dev/sdb1 | grep "Inode size"
‏Inode size:	          256
```

سایز آینود پیشفزض نسخه فعلی mkfs.ext2/3/4 برابر ۲۵۶ بایت هست ولی مشکل وقتی پیش میاد که یک فایل سیستم ext روی partition کوچکتر از ۵۱۲ مگابایت بسازیم. اونوقت inode size پیشفرض ۱۲۸ بایت خواهد بود و جای کافی برای ذخیره crtime وجود ندارد.

آینود سایز ۱۲۸ بایتی البته مشکلات دیگری هم ایجاد میکنه‪.‬ مثلا جا برای extended attributes و ACL توی آینود نداره.

البته بعضی وقت ها هم چاره‌ای نداریم و مجبوریم اندازه‌ی inode را هنگام فرمت ۱۲۸ بایت بگیریم. مثل زمانی که از Linux 2‪.‬4 و پایینتر استفاده می‌کنیم که از اندازه بزرگتر پشتیبانی نمی‌کنه.


‏keywords

‏btime
‏birth
‏ext4
‏ext
 











