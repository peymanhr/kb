# Remove old kernels from ubuntu

## Get current kernel version

```bash
uname -r
```

## List all installed kernels

```bash
dpkg -l | grep linux-image
```

## Remove old kernels

```bash
apt purge linux-image-<version>-generic
apt purge linux-image-extra-<version>-generic
```