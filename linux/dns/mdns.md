# mDNS (Multicast DNS )  


## Definition

It is a zero-configuration service, using essentially the same programming interfaces, packet formats and operating semantics as the unicast Domain Name System (DNS).  

* The mDNS Ethernet frame is a multicast UDP packet
* mDNS protocol is published as RFC 6762

* It is implemented by the Apple Bonjour and Linux nss-mdns services.  

* By default, mDNS only and exclusively resolves host names ending with the `.local` top-level domain (TLD).

* MAC address 01:00:5E:00:00:FB (for IPv4) or 33:33:00:00:00:FB (for IPv6)

* IPv4 address 224.0.0.251 or IPv6 address FF02::FB

* UDP port 5353


## Installing Avahi

```
apt-get install avahi-daemon avahi-utils  
```

## Enable mdns lookup

### /etc/snswitch.conf
```
...
hosts: hosts mdns4_minimal dns
... 
```

## Testing mDNS

### ping a machine
```
ping hostname.local
```

### Use dig
```
dig hostname.local @224.0.0.251 -p 5353
dig -x 192.168.1.1 @224.0.0.251 -p 5353
```

### Use avahi-resolve
```
avahi-resolve -n4 hostname.local
avahi-resolve -a 192.168.1.1
```

### Browse a network
```
avahi-browse -alr
```



