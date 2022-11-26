# PostgreSQL

## Install postgresql

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

## Bind to all interfaces

Edit ***/etc/postgresql/12/main/postgresql.conf***

```
listen_addresses = '*'
```
```
systemctl restart postgresql
netstat -lnpt
```


## Create database and user
```bash
sudo -i -u postgres
psql
postgres=# CREATE DATABASE foo
postgres=# CREATE USER app WITH PASSWORD 'ost';
postgres=# GRANT ALL PRIVILEGES ON DATABASE foo to app;
postgres=# \q
```

## Preparing python venv
```
sudo apt install python3-venv python3-pip build-essential libpq-dev
python3 -m venv ~/.venv/postgres
source ~/.venv/postgres/bin/activate
pip install wheel
pip install psycopg2
```

## psql Commands

### Show databases

```
\l
```

### Switch to database

```
\c dbname
```

### Show tables

```
\dt
```

### Show connection
```
\conninfo
```

## SQL

```sql
CREATE TABLE playground (
    equip_id serial PRIMARY KEY,
    type varchar (50) NOT NULL,
    color varchar (25) NOT NULL,
    location varchar(25) check (location in ('north', 'south', 'west', 'east', 'northeast', 'southeast', 'southwest', 'northwest')),
    install_date date
);

INSERT INTO playground (type, color, location, install_date) VALUES ('slide', 'blue', 'south', '2017-04-28');

SELECT * FROM playground;

DELETE FROM playground WHERE type = 'slide';

ALTER TABLE playground ADD last_maint date;

ALTER TABLE playground DROP last_maint;

UPDATE playground SET color = 'red' WHERE type = 'swing';
```

## Cheetsheet

[https://sp.postgresqltutorial.com/wp-content/uploads/2018/03/PostgreSQL-Cheat-Sheet.pdf](https://sp.postgresqltutorial.com/wp-content/uploads/2018/03/PostgreSQL-Cheat-Sheet.pdf)

## Python Example

```python 
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(database = "books",
                        user = "app",
                        password = "ost",
                        host = "127.0.0.1",
                        port = "5432")

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute('DROP TABLE IF EXISTS COMPANY')

cur.execute('''CREATE TABLE COMPANY
               (
                    ID INT PRIMARY KEY NOT NULL,
                    NAME TEXT NOT NULL,
                    AGE INT NOT NULL,
                    ADDRESS CHAR(50),
                    SALARY REAL
               );''')

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.commit()

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
    print(row['name'])

conn.close()

```

* [https://www.tutorialspoint.com/postgresql/postgresql_python.htm](https://www.tutorialspoint.com/postgresql/postgresql_python.htm)

* [http://zetcode.com/python/psycopg2/](http://zetcode.com/python/psycopg2/)

## JSON

[https://info.enterprisedb.com/rs/enterprisedb/images/EDB_White_Paper_Using_the_NoSQL_Features_in_Postgres.pdf](https://info.enterprisedb.com/rs/enterprisedb/images/EDB_White_Paper_Using_the_NoSQL_Features_in_Postgres.pdf)