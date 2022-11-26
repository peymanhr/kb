# Mongodb

* [MongoDB Tutorial for Beginners](https://beginnersbook.com/2017/09/mongodb-tutorial/)
* [How to Install MongoDB on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-18-04)
* [Getting Started with Python and MongoDB](https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb)
* [W3schools Python MongoDB](https://www.w3schools.com/python/python_mongodb_getstarted.asp)
* [Enable Access Control](https://docs.mongodb.com/manual/tutorial/enable-authentication/)
* [Dump MongoDB Data](https://www.tutorialspoint.com/mongodb/mongodb_create_backup.htm)
* [db.collection.update()¶](https://docs.mongodb.com/manual/reference/method/db.collection.update/)

```
db.createUser(
  {
    user: "admin",
    pwd: "ost",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)
```

```

   {
        "_id" : "admin.admin",
        "user" : "admin",
        "db" : "admin",
        "roles" : [
            {
                "role" : "userAdminAnyDatabase",
                "db" : "admin"
            },
            {
                "role" : "readWriteAnyDatabase",
                "db" : "admin"
            },
            {
                "role" : "dbAdminAnyDatabase",
                "db" : "admin"
            },
            {
                "role" : "clusterAdmin",
                "db" : "admin"
            },
            {
                "role" : "clusterMonitor",
                "db" : "admin"
            }
        ]
    }
```

