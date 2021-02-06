# conndb
Connect to a database. Depends on `psycopg2`. 

## Example Usage
Ensure that you have a JSON file with your database configuration information located somewhere on the deployment server.
```
dbhost=127.0.0.1
dbport=5432
dbname=postgres
dbuser=postgres
dbpass=password
dbenv=TEST
```

The `from_json` class method will look for this file at `/app/cfg/config.json` by default, but will also accept a path argument.
```python
import conndb

cfg = conndb.DBConfig.from_json("/home/adam/cfg/postgres-test")
conn = cfg.create_psycopg2_connection()
with conn.cursor() as curs:
    curs.execute("SELECT * FROM test;")
conn.commit()
conn.close()
```

## Quickstart: Docker
Add the following to your app's `requirements.txt`:
```
git+https://github.com/edenlib/conndb.git#egg=conndb
```

Build container image, then mount a local directory with secrets at runtime.
```shell
$ podman build --tag myproject:mytag .
$ podman run --rm -v ~/cfg:/app/cfg myproject:mytag
```
