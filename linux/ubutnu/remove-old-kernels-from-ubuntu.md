# Remove old kernels from ubuntu 18.04

## Get current kernel version

```bash
uname -r
```

## List all installed kernels

```bash
dpkg -l | grep linux-image | awk '{print$2}'
```

## Remove old kernels

```bash
apt purge linux-image-4.15.0-29-generic
apt purge linux-modules-4.15.0-29-generic
apt purge linux-headers-4.15.0-29*
```