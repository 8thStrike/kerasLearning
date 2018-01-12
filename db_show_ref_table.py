import psycopg2

conn=psycopg2.connect("dbname=postgres user=reporting password=Crpn2014 host=localhost")
cur=conn.cursor()


cur.execute("SELECT * FROM ref_oblig;")
rows=cur.fetchall()
print("\nShow me the results:\n")
for row in rows:
    print("  ",row[0],"  ", row[1])



cur.execute("SELECT * FROM ref_global;")
rows=cur.fetchall()
print("\nShow me the results:\n")
for row in rows:
    print("  ",row[0],"  ", row[1],"  ", row[2],"  ", row[3])


cur.execute("SELECT * FROM ref_issuer;")
rows=cur.fetchall()
print("\nShow me the results:\n")
for row in rows:
    print("  ",row[0],"  ", row[1])
