import psycopg2 as db
con = None
connected = None
cursor = None
def connect():
    global connected
    global con
    global cursor

    try :
        con = db.connect(
        host = "localhost",
        database = "kampusku",
        port = 5432,
        user = "mutii",
        password = "12345"
        )
        cursor = con.cursor()
        connected = True
    except :
        connected = False
    return cursor

def disconnect():
    global connected
    global con
    global cursor
    if (connected==True):
        cursor.close()
        con.close()
    else:
        con = None
    connected = False

def Tampil(sql):
    a = connect()
    a.execute(sql)
    record = a.fetchall()
    return record

def Entry():
    global connected
    global con
    global cursor
    xnim = input("Masukkan NIM: ")
    xnama = input("Masukkan Nama Lengkap: ")
    xidfk = input("Masukkan ID Fakultas (1 .. 5): ")
    xidpr = input("Masukkan ID Prodi (1 .. 10): ")
    a = connect()
    sql = "insert into mahasiswa (nim, nama, idfakultas, idprodi) values ('"+xnim+"','"+xnama+"','"+xidfk+"','"+xidpr+"')"
    a.execute(sql)
    con.commit()
    print("Entry is done.")

def Cari():
    global connected
    global con
    global cursor
    xnim = input("Masukkan NIM yg dicari: ")
    a = connect()
    sql = "select * from mahasiswa where nim ='" + xnim +"'"
    a.execute(sql)
    record = a.fetchall()
    print(record)
    print("search is done.")

def Ubah():
    global connected
    global con
    global cursor
    xnim = input("Masukkan NIM yg dicari: ")
    a = connect()
    sql = "select * from mahasiswa where nim ='" + xnim + "'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini :")
    print(record)
    row = a.rowcount
    if(row==1):
        print("Silahkan untuk mengubah data..")
        xnama = input("Masukkan Nama Lengkap: ")
        xidfk = input("Masukkan ID Fakultas (1 .. 5): ")
        xidpr = input("Masukkan ID Prodi (1 .. 10): ")
        a = connect()
        sql = "update mahasiswa set nama='" + xnama +"', idfakultas='" + xidfk + "', idprodi='" + xidpr + "' where nim='" + xnim + "'"
        a.execute(sql)
        con.commit()
        print("Update is done.")
        sql="select * from mahasiswa where nim='" + xnim + "'"
        a.execute(sql)
        rec = a.fetchall()
        print("Data setelah diubah :")
        print(rec)

    else:
        print("Data tidak ditemukan")

Ubah()