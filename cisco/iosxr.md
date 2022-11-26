# IOS XR

## IP Configuration

```
conf t
interface mgmtEth 0/0/CPU0/0
ipv4 address 10.1.1.10 255.255.255.0
no sh
commit
```

## Enabling gRPC
```
configure 
grpc
port 10000
no tls
```

## LAB
`pass: ost`

```
ssh root@82.99.216.247
source foo/bin/activate
cd files
```

## Examples

### Get default toute

```python
import json
from iosxr_grpc.cisco_grpc_client import CiscoGRPCClient

client = CiscoGRPCClient('172.16.6.200', 10000, 10, 'admin', 'admin')
path = '{"Cisco-IOS-XR-ip-static-cfg:router-static": [null]}'

err, result = client.getconfig(path)
if err:
    print(err)
print(json.loads(result))
```

### Add BGP Configuration

```python
path = open('bgp_start.json').read()
response = client.replaceconfig(path)

if response.errors:
    err = json.loads(response.errors)
    print(err)
```

### Get BGP Configuration

```python
path = '{"Cisco-IOS-XR-ipv4-bgp-cfg:bgp": [null]}'
err, result = client.getconfig(path)
if err:
    print(err)
print(json.dumps(json.loads(result)))
```

### Delete BGP Config

```python
path = open('bgp_start.json').read()

response = client.deleteconfig(path)
if response.errors:
    err = json.loads(response.errors)
    print(err)
```

## Find YANG Models in Cisco IOS XR

```
run
cd /pkg/yang
ls -l
```

## CDP Configuration    
```json
{
 "Cisco-IOS-XR-cdp-cfg:cdp": {
  "timer": 50,
  "enable": true,
  "log-adjacency": [
   null
  ],
  "hold-time": 180,
  "advertise-v1-only": [
   null
  ]
 }
}
```

## ios-xr-grpc-python

https://github.com/cisco-ie/ios-xr-grpc-python/blob/master/examples/grpc_cfg.py

## RFC 7951
https://tools.ietf.org/html/rfc7951

## Make JSON from YANG modules
https://napalm-automation.net/yang-for-dummies/