# VMware Fusion nat config



## Add forwarding rules 
Edit */Library/Preferences/VMware\ Fusion/vmnet6/nat.conf* and add your rule under ***[incomingtcp]***

```
[incomingtcp]
10022 = 192.168.200.131:22
```

## Restart vmware
```
sudo /Applications/VMware\ Fusion.app/Contents/Library/vmnet-cli --stop
sudo /Applications/VMware\ Fusion.app/Contents/Library/vmnet-cli --start
```

## Access SSH behind NAT
```
ssh peyman@127.0.0.1 -p 10022
```