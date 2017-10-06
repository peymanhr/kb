# Network Namespaces in Linux

## Introduction

Linux shares a single set of network interfaces and routing table entries. You can use policy routing to make certain packets use a separate routing table, but that doesn’t fundamentally change the fact that the set of network interfaces and routing tables are shared across the entire system. Network namespaces change that fundamental assumption. With network namespaces, you can have different and separate instances of network interfaces and routing tables that operate independent of each other.

I’m using Ubuntu Server 14.04 LTS. Please note that support for network namespaces varies between Linux distributions.

## Creating and verifying a network namespace

```bash
ip netns add <namespace>
ip netns list
```

## Assigning interfaces to network namespaces

```bash
ip link set dev <device> netns <namespace>
```

## Configuring interfaces in network namespaces

### Listing interfaces in a namespace
After assigning an interface to a namespace, when listing interfaces you should see a loopback interface and the interface you assigned.

```bash
ip netns exec <namespace> ip link list
```

If you run the `ip link list` command, you’ll see that the interface has disappeared from the list. It now belongs to the namespace you assigned it.   

The `ip netns exec` is how you execute commands in a different network namespace.

### Activating and adding IP address to an interface in a namespace.

```bash
ip netns exec <namespace> ip link set up dev <interface>
ip netns exec <namespace> ip addr add <ip/prefix> dev <interface>
```

### Other usual commands to run in a namespace
You actually can run all ip,ifconfig,arp,route,... in a namespace with `ip netns exec <namespace>` preceding it. some examples are shown here.

- List ip addresses and interfaces: `ip netns exec <namespace> ip addr list`
- Print routing table: `ip netns exec <namespace> ip route list`
- Ping a host from namespace: `ip netns exec <namespace> ping 8.8.8.8`
- Print ARP table: `ip netns exec <namespace> ip neigh list`

## Virtual Ethernet (veth) interfaces

Virtual Ethernet interfaces are interesting; they always come in pairs, and they are connected like a pipe. Whatever comes in one veth interface will come out the other peer veth interface.

As a result, you can use veth interfaces to connect a network namespace to another. Or even to the outside world via the “default” or “global” namespace where physical interfaces exist.

### Creating veth pair and verifying it

```bash
ip link add <veth> type veth peer name <veth pear>
ip link list
```

For example you may choose veth0 and veth1 for the names.

By default all created veth interfaces belong to “default” or “global” namespace. You can assign them to other namespaces using `ip link set <veth> netns <namespace>`.

### Connecting network namespaces to the physical network using *veth* and *bridging*.

Why doing it the long way !? This way you can **share a physical interface** between namespaces.

#### Using linux bridge
```bash
# setup namespace
ip netns add ns1
ip netns exec ns1 ip link set up lo

# create veth
ip link add veth0 type veth peer name veth0_peer
ip link set up dev veth0

# add peer side to namespace
ip link set veth0_peer netns ns1
ip netns exec ns1 ip link set up dev veth0_peer

# setup bridge
ip link add br0 type bridge
ip link set eth0 master br0
ip link set veth0 master br0
ip link set up dev br0
ip link set up dev eth0

# add ip to br0 and veth0_peer
ip addr add 10.1.1.2/24 dev br0
ip netns exec ns1 ip addr add 10.1.1.3/24 dev veth0_peer
```

#### Using openvswitch

##### Install openvswitch
```bash
apt-get install openvswitch-switch openvswitch-datapath-dkms
echo "BRCOMPAT=yes >> /etc/default/openvswitch-switch"
service openvswitch-switch restart

```

##### Setup bridge
```bash
...
# setup bridge
ovs-vsctl add-br br0
ovs-vsctl add-port br0 eth0
ovs-vsctl add-port br0 veth0
...
```

## Useful links
- http://baturin.org/docs/iproute2/
- http://blog.oddbit.com/2014/08/11/four-ways-to-connect-a-docker/
- http://www.opencloudblog.com/?p=66
- http://blog.scottlowe.org/2013/05/29/a-quick-introduction-to-linux-policy-routing/

