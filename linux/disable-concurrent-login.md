# Disable concurrent login


Open ***/etc/security/limits.conf*** and add:

```
root hard maxlogins 1
```
