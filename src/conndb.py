import json
import psycopg2


class DBConfig(object):

    def __init__(self, host, port, name, user, password):
        self.host = host
        self.port = port 
        self.name = name
        self.user = user 
        self.password = password

    @classmethod
    def from_json(cls, json_path="/app/cfg/config.json"):
        with open(json_path, "r") as f:
            cfg = json.load(f)
        return cls(host=cfg["dbhost"], port=cfg["dbport"], name=cfg["dbname"], user=cfg["dbuser"], password=cfg["dbpass"])

    def create_psycopg2_connection(self):
        return psycopg2.connect(host=self.host, port=self.port, database=self.name, user=self.user, password=self.password)
