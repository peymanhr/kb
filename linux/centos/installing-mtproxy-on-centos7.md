# Installing MTProxy on CentOS 7

### Adding `getpagespeed` repo and install mtproxy package
```bash
yum -y install https://extras.getpagespeed.com/release-el7-latest.rpm 
yum -y install mtproxy
```

### Change secret in `/etc/mtproxy/secret`. it is a 128bit hexodecinmal like md5.

```
MTPROXY_SECRET=08f059c6515c7a163953dcd8df295c97 

```

### Change port and number of workers in `/etc/mtproxy/mtproxy.params`

```
MTPROXY_CLIENT_PORT=23235
MTPROXY_WORKERS=10
```

### Enable and start mtproxy service
```bash
systemctl enable mtproxy
systemctl start mtproxy
systemctl status mtproxy
```