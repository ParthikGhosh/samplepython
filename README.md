
## Install pre-requisite packages

``` 
$ sudo yum install git -y
$ sudo yum install python-pip
$ sudo pip install --upgrade pip
```

```
$ sudo pip install Flask
$ sudo pip install requests
$ sudo pip install Flask-Cors
```

## Start Apache HBASE rest api server

```
$ cd /usr/hdp/2.x.x.x/hbase
$ bin/hbase rest start -p 4200
```

## Start Apache HBASE rest api server as a daemon

```
$ cd /usr/hdp/2.x.x.x/hbase
$ sudo bin/hbase-daemon.sh start rest -p 4200
$ curl -vi -X GET -H "Accept: application/json" http://localhost:4200/version/cluster
```

## Sample rest call to get last 10 records from table


```
$ curl -vi -X GET -H "Accept: application/json" http://localhost:4200/table_name/*?limit=10&reversed=true
```

## Start development server

```
$ mkdir -p ~/ifabric.ws && cd ~/ifabric.ws
$ git clone https://bitbucket.fsc.atos-services.net/scm/ci/codex-ifabric-demoapp.git
$ cd codex-ifabric-demoapp && cd ifabric-api && cd src
$ python app.py
```

or

```
$ export FLASK_APP=app.py
$ python -m flask run
```

## Set Hbase server base url

Default Hbase URL is `http://localhost:4200` which can be specified byt setting `HBASE_BASE_URL`

```
$ export HBASE_BASE_URL=http://host:port
```

## Invoke sample ping service

```
$ curl -vi -X GET http://127.0.0.1:3004/ping
```

From outside

```
$ curl -vi -X GET http://dhdp-ambari.paas-enablement.net:13004/ping
```

