from influxdb import InfluxDBClient

class BC_InfluxDBClient:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = '8086'
        self.user = 'ap'
        self.password = 'ddeerr44'
        self.dbname = 'stocksDAILY'
        self.query = 'select value from cpu_load_short;'

        self.measurement
        self.tags
        self.time
        self.fields
        self.json_body = [
            {
                "measurement": "cpu_load_short",
                "tags": {
                    "host": "server01",
                    "region": "us-west"
                },
                "time": "2009-11-10T23:00:00Z",
                "fields": {
                    "Float_value": 0.64,
                    "Int_value": 3,
                    "String_value": "Text",
                    "Bool_value": True
                }
            }
        ]
        self.InfluxDBClient = InfluxDBClient(host=self.host, port=self.port, username=self.user, password=self.password, database=self.database)

    def insert(self, ticker, date, high, low, open, close, volume):
        ret = ""
        json_body = [
            {
                "measurement": "daily_stock",
                "tags": {
                    "ticker": ticker,

                },
                "time": date,
                "fields": {
                    "high": high,
                    "low": low,
                    "open": open,
                    "close": close,
                    "volume": volume,
                    }
            }
        ]
        self.InfluxDBClient.write_points(json_body)

        return ret



