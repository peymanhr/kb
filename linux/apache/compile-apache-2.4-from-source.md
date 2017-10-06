

# Compile apache 2.4 from source

## Installing build tools

```bash
sudo apt install build-essential 
```
## Download source files
```bash
wget http://www-us.apache.org/dist//apr/apr-1.6.2.tar.bz2
wget http://www-us.apache.org/dist//apr/apr-util-1.6.0.tar.bz2
wget https://ftp.pcre.org/pub/pcre/pcre-8.41.tar.bz2
wget https://fossies.org/linux/www/expat-2.2.3.tar.bz2
wget https://www.openssl.org/source/openssl-1.1.0f.tar.gz
wget http://www-us.apache.org/dist//httpd/httpd-2.4.27.tar.bz2
```

## Building and Installing *pcre*

```bash
$ tar -xjf pcre-8.41.tar.bz2
$ cd pcre-8.41/
$ ./configure --prefix=/usr/local/pcre
$ make
$ sudo make install
```

## Building and Installing *expat*

```bash
$ tar -xjf expat-2.2.3.tar.bz2
$ cd expat-2.2.3/
$ ./configure CPPFLAGS=-DXML_LARGE_SIZE --prefix=/usr/local/expat
$ make
$ sudo make install
```

## Building and Installing *openssl*

```bash
$ tar -xzf openssl-1.1.0f.tar.gz 
$ cd openssl-1.1.0f/
$ ./config --prefix=/usr/local/openssl -Wl,--enable-new-dtags,-rpath,'$(LIBRPATH)'
$ make
$ sudo make install
$ sudo sh -c 'echo "/usr/local/openssl/lib" > /etc/ld.so.conf.d/openssl.conf'
$ sudo ldconfig
```

## Extracting *Apache*

```bash
$ tar -xjf httpd-2.4.27.tar.bz2
```

## Including *apr* and *apr-util* in httpd source tree

```bash
$ tar -xjf apr-1.6.2.tar.bz2 
$ tar -xjf apr-util-1.6.0.tar.bz2
$ mv apr-1.6.2 httpd-2.4.27/srclib/apr
$ mv apr-util-1.6.0 httpd-2.4.27/srclib/apr-util
```

## Building and Installing *Apache*

```bash
$ cd httpd-2.4.27/
$ ./configure \
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
$ make
$ sudo make install
```

## Running *Apache*

```bash
$ sudo systemctl stop apache2.service
$ sudo systemctl disable apache2.service
$ cd /usr/local/httpd
$ sudo bin/apachectl start
```

## Verifying Installation

```bash
$ sudo netstat -lnpt | grep httpd
tcp6	0	0 :::80	:::*	LISTEN		12471/httpd

$ curl -s http://127.0.0.1/
<html><body><h1>It works!</h1></body></html>

$ bin/apachectl -M
Loaded Modules:
...
 ssl_module (static)
...
```



## Installing needed libraries during build as package

```bash
$ sudo apt install libapr1 libapr1-dev libaprutil1 libaprutil1-dev libexpat1-dev libssl-dev

$ ./configure \
--prefix=/usr/local/httpd \
--with-pcre=/usr/local/pcre \
--enable-ssl \
```