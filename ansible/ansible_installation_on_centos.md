# Installing Ansible on Centos 7

## Add epel-release repo
```
$ sudo yum install epel-release
```

## Install python3
```
$ sudo yum install python3
```

## Create a virtual environment
```
$ mkdir ~/.venv
$ python3 -m venv ~/.venv/ansible
$ source ~/.venv/ansible/bin/activate
(ansible)$ pip install --upgrade pip
(ansible)$ pip install wheel
(ansible)$ pip install ansible
(ansible)$ pip install paramiko
(ansible)$ pip install passlib
```


## Verify Installation
```
(ansible)$ ansible --version
ansible 2.8.5
  config file = None
  configured module search path = ['/home/peyman/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/peyman/.venv/ansible/lib64/python3.6/site-packages/ansible
  executable location = /home/peyman/.venv/ansible/bin/ansible
  python version = 3.6.8 (default, Aug  7 2019, 17:28:10) [GCC 4.8.5 20150623 (Red Hat 4.8.5-39)]```


