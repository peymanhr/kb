# Scapy

## Install scapy

```bash
pip3 install scapy-python3
```

## Disable scapy warnings
```python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
```

## Importing scapy
```python
from scapy.all import *
```

## Analysing pcap files
```bash
sudo tcpdump -i enp0s3 -w out.pcap
```

```python
>>> c = rdpcap("/home/peyman/out.pcap")
>>> c
<out.pcap: TCP:0 UDP:2 ICMP:8 Other:0>
>>> c.summary()
Ether / IP / UDP 10.0.2.15:mdns > 224.0.0.251:mdns / Raw
Ether / IPv6 / UDP fe80::cacc:a7c:e663:424b:mdns > ff02::fb:mdns / Raw
Ether / IP / ICMP 10.0.2.15 > 8.8.8.8 echo-request 0 / Raw
Ether / IP / ICMP 8.8.8.8 > 10.0.2.15 echo-reply 0 / Raw
Ether / IP / ICMP 10.0.2.15 > 8.8.8.8 echo-request 0 / Raw
Ether / IP / ICMP 8.8.8.8 > 10.0.2.15 echo-reply 0 / Raw
Ether / IP / ICMP 10.0.2.15 > 8.8.8.8 echo-request 0 / Raw
Ether / IP / ICMP 8.8.8.8 > 10.0.2.15 echo-reply 0 / Raw
Ether / IP / ICMP 10.0.2.15 > 8.8.8.8 echo-request 0 / Raw
Ether / IP / ICMP 8.8.8.8 > 10.0.2.15 echo-reply 0 / Raw

```

### Creating pdf from a packet

```bash
sudo apt-get install python3-pyx
sudo pip3 install pyx
```

```python
import pyx

c[2].pdfdump('/home/peyman/Desktop/packet.pdf', layer_shift=1)
```

## Sniff packets

```python
packets = sniff(filter="icmp and host 8.8.8.8", count=2)
packets.summary()
packets[0].show()
```

### Save packets to pcap file
```python
wrpcap("temp.cap", packets)
```

## ARPing

```python
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")ARP(pdst="10.0.2.0/24"),timeout=2)
```

## Send 1 echo request and receive one answer

```python
p = IP(dst='8.8.8.8',ttl=128)/ICMP(type='echo-request')/'HelloWorld!'
r = sr1(p)
r.show()
```

## 
```python
p = sr1(IP(dst='8.8.8.8')/UDP()/DNS(rd=1,qd=DNSQR(qname='ubuntu.com')))
p.show()
print(p.an.getstrval('type'))

p = sr1(IP(dst='8.8.8.8')/UDP()DNS(rd=1,qd=DNSQR(qname='google.com',qtype='NS')))
p.an.show()
for i in range(p[DNS].ancount):
    print(p.an[i].getstrval('rdata'))
```

## Sending TCP syn
```python
sr1(IP(dst="82.99.216.245")/TCP(dport=[80,81],flags="S"), timeout=3, retry=0)
```

* sr1
* srp1
* sr
* srp
* send
* sendp


```python
#!/usr/bin/env python3

# Disable scapy warnings
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

# Send 1 echo request and receive one answer
#p = sr1(IP(dst='192.168.4.1',src='192.168.4.109',ttl=128)/ICMP(type='echo-request')/'HelloWorld!')
#p.show()

# Send tcp syn and receive one answer
#p=sr1(IP(dst='192.168.4.1')/TCP(dport=80,flags='S'))
#p.show()

#p=sr(IP(dst='192.168.4.1')/TCP(dport=[80],flags='S'))
#ans,unans = p
#ans.summary()
#ans.nsummary()
#ans.hexdump()

# DNS
#p = sr1(IP(dst='8.8.8.8')/UDP()/DNS(rd=1,qd=DNSQR(qname='ubuntu.com')))
#p.show()
#print(p.an.getstrval('type'))

#p = sr1(IP(dst='8.8.8.8')/UDP()/DNS(rd=1,qd=DNSQR(qname='google.com',qtype='NS')))
#p.an.show()
#for i in range(p[DNS].ancount):
#    print(p.an[i].getstrval('rdata'))

#conf.verb = 1
#ans, unans = sr(IP(dst='192.168.4.1')/TCP(flags='S', dport=[80,23,22]), timeout=10)
#for p in ans:
#    print(p[0].dport)

#p = sr(IP(dst='127.0.0.1')/TCP(flags='S', dport=80), timeout=10, retry=0)
#a,u = p
#u.summary()
```
