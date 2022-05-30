import psycopg2

conn = psycopg2.connect("dbname=python_intermedio_db user= postgres password=root")
cur  = conn.cursor()

cur.execute("select * from usuarios")
print(cur.fetchone())