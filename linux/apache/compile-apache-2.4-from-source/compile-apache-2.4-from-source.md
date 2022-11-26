`

# Compile apache 2.4 from source on ubuntu 16.04

## Installing build tools

```bash
sudo apt install build-essential 
```

or

```bash
sudo yum groupinstall 'Development Tools'
```
## Download source tarballs 
```bash
wget https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz
wget http://www-us.apache.org/dist/apr/apr-1.7.0.tar.gz
wget http://www-us.apache.org/dist/apr/apr-util-1.6.1.tar.gz
wget https://fossies.org/linux/www/expat-2.2.9.tar.xz
wget https://www.openssl.org/source/openssl-1.1.1g.tar.gz
wget https://www-us.apache.org/dist//httpd/httpd-2.4.41.tar.bz2
```

## Building and Installing *pcre*

```bash
tar -xzf pcre-8.44.tar.gz
cd pcre-8.44/
./configure --prefix=/usr/local/pcre
make
sudo make install
```

## Building and Installing *expat*

```bash
tar -xJf expat-2.2.9.tar.xz
cd expat-2.2.9/
./configure CPPFLAGS=-DXML_LARGE_SIZE --prefix=/usr/local/expat
make
sudo make install
```

## Building and Installing *openssl*

```bash
tar -xzf openssl-1.1.1g.tar.gz 
cd openssl-1.1.1g/
./config --prefix=/usr/local/openssl -Wl,--enable-new-dtags,-rpath,'$(LIBRPATH)'
make
sudo make install
sudo sh -c 'echo "/usr/local/openssl/lib" > /etc/ld.so.conf.d/openssl.conf'
sudo ldconfig
```

## Extracting *Apache*

```bash
tar -xjf httpd-2.4.43.tar.gz
```

## Including *apr* and *apr-util* in httpd source tree

```bash
tar -xzf apr-1.7.0.tar.gz 
tar -xzf apr-util-1.6.1.tar.gz
mv apr-1.7.0 httpd-2.4.43/srclib/apr
mv apr-util-1.6.1 httpd-2.4.37/srclib/apr-util
```

## Building and Installing *Apache*

```bash
cd httpd-2.4.43/
./configure \
--prefix=/usr/local/httpd \
--with-included-apr \
--with-pcre=/usr/local/pcre \
--with-expat=/usr/local/expat \
--enable-ssl \
--with-ssl=/usr/local/openssl \
--enable-ssl-staticlib-deps \
--enable-mods-static=ssl \
--enable-rewrite \
--enable-cgi
make
sudo make install
```

## Running *Apache*

```bash
sudo systemctl stop apache2.service
sudo systemctl disable apache2.service
cd /usr/local/httpd
sudo bin/apachectl start
```

## Verifying Installation

```bash
sudo netstat -lnpt | grep httpd
tcp6	0	0 :::80	:::*	LISTEN		12471/httpd

curl -s http://127.0.0.1/
<html><body><h1>It works!</h1></body></html>

bin/apachectl -M
Loaded Modules:
...
 ssl_module (static)
...
```



## Installing needed libraries during build as package

```bash

sudo apt install libapr1-dev libaprutil1-dev libpcre3-dev libssl-dev libexpat1-dev

./configure \
--prefix=/usr/local/httpd \
--enable-ssl \
--enable-rewrite \
--enable-cgi
````