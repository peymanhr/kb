# Enabling TSIG for Zone Transfers  


## Entropy

### Check available entropy

```no-highlight
cat /proc/sys/kernel/random/entropy_avail
```

### Generate entropy

You can run random commands like `ls -R /` or `find /` or just start typing. Bu the best way is to use `rngd` command:

```no-highlight
apt-get install rng-tools
rngd -r /dev/urandom -o /dev/random -b
```

## Generating Keys

```no-highlight
dnssec-keygen -a HMAC-SHA512 -b 512 -n HOST -r /dev/urandom tsigkey
```

### ./Ktsigkey.+165+49047.private
```no-highlight
Private-key-format: v1.3
Algorithm: 165 (HMAC_SHA512)
Key: Ok1qR5IW1ajVka5cHPEJQIXfLyx5V3PSkFBROAzOn21JumDq6nIpoj6H8rfj5Uo+Ok55ZWQ0Wgrf302fDscHLw==
```

### /etc/bind/named.conf.tsigkeys  

```no-highlight
key "my-tsig" {
 algorithm HMAC-SHA512;
 secret "Ok1qR5IW1ajVka5cHPEJQIXfLyx5V3PSkFBROAzOn21JumDq6nIpoj6H8rfj5Uo+Ok55ZWQ0Wgrf302fDscHLw==";
};
```

### /etc/bind/named.conf
```no-highlight
include "/etc/bind/named.conf.options";
include "/etc/bind/named.conf.local";
include "/etc/bind/named.conf.default-zones";
// ADD THE LINE BELOW
include "/etc/bind/named.conf.tsigkeys";
```

### /etc/bind/named.conf.local
```no-highlight
zone "mysecuredzone.com" {
 type master;
 file "/etc/bind/zones/db.mysecuredzone.com";
 allow-transfer {
  key "my-tsig";
 };
};
```





