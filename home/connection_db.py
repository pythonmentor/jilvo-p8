import psycopg2

db = DB(dbname='oc_8_nutella', host='localhost', port=50779, user='admin', passwd='root')

result = db.query("SELECT * FROM User")

print(result)

db.close()