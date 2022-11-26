# Getting started with Ansible

## Disable `Cryptography` warnings
```bash
export PYTHONWARNINGS="ignore::UserWarning"
```


## Running a simple command using raw module

```bash 
ansible all -i 192.168.4.110, -u peyman -bkK -m raw -a 'uptime'
```

## Inventory file

```
127.0.0.1

[ios]
10.1.1.5
10.1.1.6

[servers]
192.168.4.110

[servers:vars]
ansible_python_interpreter=/usr/bin/python3

#---- Needs sshpass
#ansible_password=ost

[ios:vars]
ansible_become=yes
ansible_become_method=enable
ansible_network_os=ios
ansible_user=cisco
ansible_ssh_pass=cisco
ansible_become_pass=cisco

```

## Playbook

### Adding SSH key exclusively
```yaml
---
- hosts: servers
  user: peyman
  become: yes
  tasks:
    - name: Add SSH key exclusivly
      authorized_key:
        user: peyman
        state: present
        key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
        exclusive: yes
```

### Installing apache2 on ubuntu

```yaml
---
- hosts: servers
  user: peyman
  become: true
  tasks:
    - name: Install Apache2
      apt: pkg=apache2 update_cache=true
      notify: stop_httpd
  handlers:
    - name: stop_httpd
      service: name=apache2 state=stopped

```

### Removing apache2 on ubuntu
```yaml
---
- hosts: servers
  user: peyman
  become: true

  tasks:
    - name: Uninstall Apache
      apt: pkg=apache2 state=absent update_cache=false purge=yes
```

### Changing IOS hostname
```yaml
---
- name: GENERATE A REPORT
  hosts: ios
  gather_facts: yes
  connection: network_cli
  become: yes

  tasks:
  - name: Change Hostname
    ios_command:
      commands:
        - conf t
        - hostname FOO
```

### Show interfaces
```yaml
---
- name: GENERATE A REPORT
  hosts: cisco
  gather_facts: no
  connection: network_cli

  roles:
    - ansible-network.network-engine

  tasks:
  - name: CAPTURE SHOW IP INTERFACE
    ios_command:
      commands:
        - show ip interface brief
    register: output
    
  - name: DISPLAY THE OUTPUT
    debug: var=output.stdout
```