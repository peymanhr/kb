# KEv2 VPN Server with StrongSwan on Ubuntu 18.04 

## Installing StrongSwan 

```bash
sudo apt install strongswan strongswan-pki libcharon-standard-plugins libcharon-extra-plugins iptables-persistent
```

## Generate entropy
```bash
cat /proc/sys/kernel/random/entropy_avail
ls -lR /

```

## Creating a Certificate Authority
```bash
mkdir -p ~/pki/{cacerts,certs,private}
chmod 700 ~/pki
ipsec pki --gen --type rsa --size 4096 --outform pem > server-root-key.pem
ipsec pki --self --ca --lifetime 3650 --in ~/pki/private/ca-key.pem --type rsa --dn "CN=Rabbit Root CA" --outform pem > ~/pki/cacerts/ca-cert.pem
```

## Generating a Certificate for the VPN Server
```bash
ipsec pki --gen --type rsa --size 4096 --outform pem > ~/pki/private/server-key.pem

ipsec pki --pub --in ~/pki/private/server-key.pem --type rsa \
    | ipsec pki --issue --lifetime 1825 \
        --cacert ~/pki/cacerts/ca-cert.pem \
        --cakey ~/pki/private/ca-key.pem \
        --dn "CN=hostname" --san "hostname" \
        --flag serverAuth --flag ikeIntermediate --outform pem \
    >  ~/pki/certs/server-cert.pem

```

## Install all certificates

```bash
sudo cp -r ~/pki/* /etc/ipsec.d/
```

## Configuring StrongSwan

```bash
sudo mv /etc/ipsec.conf{,.original}

cat <<EOF > /etc/ipsec.conf
config setup
    charondebug="ike 1, knl 1, cfg 0"
    uniqueids=yes

conn ikev2-vpn
    auto=add
    compress=yes
    type=tunnel
    keyexchange=ikev2
    fragmentation=yes
    forceencaps=yes
    dpdaction=clear
    dpddelay=300s
    rekey=no
    left=%any
    leftid=@rabbit.arjang.ac.ir
    leftcert=server-cert.pem
    leftsendcert=always
    leftsubnet=0.0.0.0/0
    right=%any
    rightid=%any
    rightauth=eap-mschapv2
    rightsourceip=10.10.10.0/24
    rightdns=8.8.8.8,1.1.1.1
    rightsendcert=never
    eap_identity=%identity
EOF
```

## Configuring VPN Authentication

```bash
cat <<EOF > /etc/ipsec.secrets
: RSA "server-key.pem"
peyman : EAP "suticarma"
EOF
```

## Restart StrongSwan

```bash
sudo systemctl restart strongswan
```

## Enable ip_forwarding

```bash
cat <<EOF >> /etc/sysctl.conf
net.ipv4.ip_forward = 1
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.ip_no_pmtu_disc = 1
EOF
```

## Configuring firewall

```bash
sudo ufw disable
sudo iptables -t nat -A POSTROUTING -o eth0 -s 10.10.10.0/24 -j MASQUERADE
sudo iptables-persistent save
sudo iptables-persistent reload
```

## Monitoring

```bash
ipsec status
ipsec leases
ipsec statusall
```