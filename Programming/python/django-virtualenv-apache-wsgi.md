# Django with apache and mod_wsgi


## Installing required packages

```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install apache2
$ sudo apt install python3-pip
$ sudo apt install python3-venv
$ sudo apt install libapache2-mod-wsgi-py3
```

## Installing Django

### Setting up virtual environment

```bash
$ cd
$ mkdir venvs && cd venvs
$ python3 -m venv foo.net
$ source foo.net/bin/activate
```

### Upgrading pip and installing Django

```bash
(foo.net)$ pip install --upgrade pip
(foo.net)$ pip install django
(foo.net)$ cd ..
```

### Creating a project

```bash
(foo.net)$ django-admin startproject foo
```

### Allowing remote hosts access project

Edit ***foo/foo/settings.py*** and replace:

```python
ALLOWED_HOSTS = []
```
with

```python
ALLOWED_HOSTS = ['*']
```

### Test Installation

```bash
(foo.net)$ python foo/manage.py runserver 0:8000
```
Open a browser and go to ***http://\<host\>:8000/***

### Stopping server

```bash
^C
```

### Freezing requirements

```bash
(foo.net)$ pip freeze > foo/requirements.txt
```

### Deactivating virtual env

```bash
(foo.net)$ deactivate
$
```

## Configuring apache

### Fix apache *fqdn* warning

Edit ***/etc/apache2/apache2.conf*** and add:

```
ServerName 127.0.0.1
```

```bash
$ sudo service apache2 restart
```

### Verify mod_wsgi is enabled

```bash
$ apachectl -M | grep wsgi
wsgi_module (shared)
```
if it is not enabled:

```bash
$ sudo a2enmod wsgi
$ sudo service apache2 restart
```

### Add virtualhost

Create ***/etc/apache2/sites-enabled/foo.net.conf***:

```
<VirtualHost *:80>

    Define ENV "/home/peyman/venvs/foo.net"
    Define APP "/home/peyman/foo"

    ServerName foo.net

    <Directory "${APP}/foo">
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess foo python-path=${APP} python-home=${ENV}
    WSGIProcessGroup foo
    WSGIScriptAlias / ${APP}/foo/wsgi.py

</VirtualHost>
```

### Verify Django app is working with wsgi

```
$ sudo service apache2 restart
$ sudo sh -c 'echo "127.0.0.1 foo.net" >> /etc/hosts'
```
Open a browser and go to ***http://foo.net/***

If you are using another machine as http client other than the same machine as your server, use your server ip address instead of *127.0.0.1*.

### Adding static contents

It is best to use another web server possibly **Nginx** or even another minimal **Apache** to serve static contents and let the main server serve the **wsgi** app only.

But if you insist on hosting static files on the same server, do the followings.

Edit ***/etc/apache2/sites-enabled/foo.net.conf*** and add the following lines inside the ***VirtualHost*** container.

```
Alias /static ${APP}/static
<Directory ${APP}/static>
    Require all granted
</Directory>
```
Create the ***static*** folder and some files inside it.

```bash
$ mkdir foo/static
$ echo "<h1>Sample Static File</h1>" > foo/static/test.html
```
Open a browser and go to ***http://foo.net/static/test.html***

Your Final ***/etc/apache2/sites-enabled/foo.net.conf*** must look like this:

```
<VirtualHost *:80>

    Define ENV "/home/peyman/venvs/foo.net"
    Define APP "/home/peyman/foo"

    ServerName foo.net

    <Directory "${APP}/foo">
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess foo python-path=${APP} python-home=${ENV}
    WSGIProcessGroup foo
    WSGIScriptAlias / ${APP}/foo/wsgi.py

    Alias /static ${APP}/static
    <Directory ${APP}/static>
        Require all granted
    </Directory>

</VirtualHost>
```

## Replicating virtual env for the project

```bash
$ cp -r foo bar
$ cd bar
$ python3 -m venv .
$ source bin/activate
(bar)$ 
(bar)$ pip install -r requirements.txt
(bar)$ python manage.py runserver 0:8000
```




