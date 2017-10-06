# Configure SSH Certificate Authentication

```bash
ssh-keygen -t rsa
ssh root@<host> mkdir -p .ssh
cat ~/.ssh/id_rsa.pub | ssh root@<host> 'cat >> .ssh/authorized_keys'
```

## Recomended permissions

```bash
ssh root@<host> chmod 700 .ssh && chmod 640 .ssh/authorized_keys
```


