# My Docker notes

## Setting up a LAMP on Mac OSX
Ref: http://ineed.coffee/projects/osx-docker-lamp/

```
docker pull dgraziotin/lamp
docker run -i -t -p "80:80" -p "3306:3306" -e CREATE_MYSQL_BASIC_USER_AND_DB="true" -v ${PWD}/mysql:/var/lib/mysql -v ${PWD}/app:/app --name lamp dgraziotin/lamp
```
This doesn't seem to work with mysql after the first time. Even if you take away the CREATE_MYSQL_BASIC_USER_AND_DB env it won't import the existing mysql data.

In the mean time I've been destroying and creating lamp and using the phpmyadmin to import/export the db.

```bash
docker run -d -p "80:80" -e CREATE_MYSQL_BASIC_USER_AND_DB="true" -v ${PWD}:/app --name lamp dgraziotin/lamp
```

# problems with mac
Mac volumes don't work properly. It only will read volumes from OSX env if the docker user accessing it has the same UID as the docker-machine UID (1000).

# My SQL donesn't seem to work

