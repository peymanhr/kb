# Gitlab 

## git - is the one, period.

## Public and Private git servers

* github
* gitlab
* private git server

## Gitlab features

* Perfect UI/UX to manage repo
* Commit directly from gitlab
* manage members and their level
* Branch Graphs
* Issue board
* Wiki
* Collaboration through merge request
* Analytics
* Time Tracking
* CI/CD

## Installing Gitlab

### Environment prerequisite 

* Linux Server IP Configuration

    ```
    Subnet: 82.99.216.240/28
    IP Address: 82.99.216.248
    Gateway: 82.99.216.241
    ```  

    */etc/netplan/main.yaml*

    ```
    network:
    ethernets:
        ens160:
            addresses:
            - 82.99.216.248/28
            gateway4: 82.99.216.241
            nameservers:
                addresses:
                - 9.9.9.9
                - 8.8.4.4
    version: 2
    ```
    
    ```bash
    netplan apply
    ```
    

* FQDN and DNS records

    ```
    Zone: gnusol.com
    Host: gitlab.gnusol.com
    ```

* Timezone
* SSH Public key authentication
    * .ssh/authorized_keys
    
    ```bash
    ssh-keygen -t rsa
    ssh root@82.99.216.248 mkdir -p .ssh
    cat ~/.ssh/id_rsa.pub | ssh root@82.99.216.248 'cat >> .ssh/authorized_keys'
    ssh root@82.99.216.248 chmod 700 .ssh && chmod 640 .ssh/authorized_keys
    ```
    
    * .ssh/config
    
    ```
    # GitLab.com server
    Host gitlab.gnusol.com
    PubkeyAuthentication yes
    IdentityFile ~/.ssh/gitlab_rsa

    ```

### [Installing GitLab with Omnibus package](https://about.gitlab.com/install/#ubuntu)

## Working with Gitlab
* Merge requests

