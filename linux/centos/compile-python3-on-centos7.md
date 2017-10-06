# Compile Python3 on CentOS 7

### Install required libraries
```bash
yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel
```

### Compile and install python from source
```bash
mkdir -p /usr/local/python/python-3.6.0/lib
./configure --prefix=/usr/local/python/python-3.6.0 --enable-shared LDFLAGS="-Wl,-rpath /usr/local/python/python-3.6.0/lib"
make
make install
echo "PATH=\$PATH:/usr/local/python/python-3.6.0/bin" >> /etc/bashrc

```

## Add EPEL repo

```bash
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -i epel-release-latest-7.noarch.rpm
```

