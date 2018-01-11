import psycopg2
import csv

conn=psycopg2.connect("dbname=postgres user=reporting password=Crpn2014 host=localhost")

data = csv.reader(open(''))
cur=conn.cursor()

cur.execute("""INSERT INTO TABLE num_categorie_1 ();""")


#conn.commit()
