# Cisco SSHv2 Configuration and OpenSSH Client

## General Router Configuration

```
en
conf t
hostname r1
enable secret cisco
no cdp run
int fa0/0
ip address 192.168.1.2 255.255.255.0
no shut
exit
```
## SSHv2 Configuration

```
line vty 0 4
login local
exit
username cisco password cisco
ip domain-name r1.foo.net
crypto key generate rsa
1024
ip ssh version 2
exit
wr
```

## Client configuration

### Option #1

Use ssh client command line options.

```bash
ssh -c aes256-cbc -o KexAlgorithms=diffie-hellman-group1-sha1 cisco@10.1.1.1
```

### Option #2

Add these lines to the beginning of OpenSSH user-specific configuration file ***.ssh/config*** or global configuration file ***/etc/ssh/ssh_config***

```
HostkeyAlgorithms +ssh-dss
KexAlgorithms +diffie-hellman-group1-sha1
Ciphers +3des-cbc
```

Do normal ssh

```
ssh cisco@10.1.1.1
```
## Managing SSH Sessions

```
show users
clear line vty 1
```

## Sever Configuration on IOS Device

There is a very good article on 
[Securing Cisco IOS SSH server](https://networkjutsu.com/securing-cisco-ios-ssh-server/) which describes proper SSH configuration on IOS Devices.
