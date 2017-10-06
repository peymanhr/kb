# FTP in Python3

```python
from ftplib import FTP 

>>> s = ftplib.FTP('hostname','user','pass')
>>> s.dir()
drwxrwxr-x    6 1010     1010         4096 Aug 02 11:14 images
drwxrwxr-x    12 1010     1010         4096 Nov 29 10:41 logs
>>> s.cwd('images')
'250 Directory successfully changed.'
>>> s.pwd()
'/images'
>>> f = open('image.png', 'rb')
>>> s.storbinary('STOR image.png', f)
'226 Transfer complete.'
>>> f.close()
>>> s.quit()
```


