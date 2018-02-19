import apSTOCKS


query = "SELECT * FROM daily_stock;"
BC_InfluxDBClient = apSTOCKS.BC_InfluxDBClient()

resultSet = BC_InfluxDBClient.Query("SELECT * FROM daily_stock;")

print(resultSet.raw)
