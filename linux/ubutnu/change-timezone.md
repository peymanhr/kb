# Change timezone on ubuntu 16.04

```bash
sudo timedatectl set-timezone Asia/Tehran
```

or 

```bash
sudo dpkg-reconfigure tzdata
```

or

```bash
ln -sf /usr/share/zoneinfo/Asia/Tehran /etc/localtime
```