from influxdb_client import InfluxDBClient

my_token = 't'
my_org = 'www.yo'
bucket = 'elo'


client = InfluxDBClient(url=my_org, token=my_token, bucket=bucket)

print(client)

