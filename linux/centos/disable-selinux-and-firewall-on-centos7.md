# Disable SELinux and Firewall on CentOS 7

## Disable SELinux

**Reboot** is needed to disable SELinux.

### Check the status of SELinux
```bash
sestatus
```

### Disable SELinux Temporarily
```bash
echo 0 > /selinux/enforce
```
or

```bash
setenforce 0
```

### Disable SELinux Permanently
*/etc/sysconfig/selinux*

```
SELINUX=disabled
```

## Disable Firewall

### Check the status of firewall
```bash
systemctl status firewalls
```

### Stop and disable firewall
```bash
systemctl stop firewalld
systemctl disable firewalld
```

### Remove netfilter rules
```bash
iptables -t filter -F
iptables -t nat -F
iptables -t mangle -F
```
