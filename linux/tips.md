# Tips

## Backup config files in  place  

```
cp /etc/squid3/squid.conf{,.bak}
```

## List all available kernel modules  

```
find /lib/modules/`uname -r` -type f -iname '*.o' -or -iname '*.ko'
```

## Redirect packets to local process

```
sysctl -w net.ipv4.conf.eth0.route_localnet=1
iptables -t nat -A PREROUTING -i eth0 -d 192.168.4.38 -p tcp --dport 80 -j DNAT --to 127.0.0.1:80
```

## Downloading entire web site

```
wget \
     --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --restrict-file-names=windows \
     --domains website.org \
     --no-parent \
         www.website.org/tutorials/html/
```

This command downloads the web site www.website.org/tutorials/html/.

The options are:

`--recursive`: download the entire Web site.

`--domains` website.org: don't follow links outside website.org.

`--no-parent`: don't follow links outside the directory tutorials/html/.

`--page-requisites`: get all the elements that compose the page (images, CSS and so on).

`--html-extension`: save files with the .html extension.

`--convert-links`: convert links so that they work locally, off-line.

`--restrict-file-names=windows`: modify filenames so that they will work in Windows as well.

`--no-clobber`: don't overwrite any existing files (used in case the download is interrupted and
resumed).

## Multiuser screen session

Install screen

```
apt-get install screen
```  

Multiuser session needs SUID be set on screen binary
```
chmod u+s /usr/bin/screen
chmod 755 /var/run/screen
```

Create an account
```
useradd -m -s /bin/bash student
passwd student
```

### ~/.screenrc
```
startup_message off
multiuser on
aclchg READERS -w "#"
aclgrp student READERS
aclumask "*"-rwx peyman+rwx READERS+r-wx
```

Start session

```
screen -S class
```

Clients use ssh to connect
```
ssh student@teacherhost 
screen -x peyman/class
```

