import psycopg2 as db

try:
    con =db.connect(
    host = "localhost",
    database ="kampusku",
    port= 5432,
    user = "mutii",
    password="12345"
    )
    cursor=con.cursor()

    sql="select * from mahasiswa"
    cursor.execute(sql)
    record=cursor.fetchall()
    print(record)

except:
    print("koneksi gagal")