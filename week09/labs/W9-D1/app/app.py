import os, pymysql
conn = pymysql.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASS'],
    database=os.environ['DB_NAME'])
with conn.cursor() as cur:
    cur.execute("SELECT * FROM proof")
    print("READ FROM RDS:", cur.fetchall())
conn.close()
