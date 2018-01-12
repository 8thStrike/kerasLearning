import psycopg2

conn=psycopg2.connect("dbname=postgres user=reporting password=Crpn2014 host=localhost")
cur=conn.cursor()


cur.execute("SELECT * FROM num_categorie_1;")
rows=cur.fetchall()
print("\nShow me the results:\n")
for row in rows:
    print("  ",row[0],"  ", row[1])



cur.execute("SELECT * FROM num_categorie_2;")
rows=cur.fetchall()
print("\nShow me the results:\n")
for row in rows:
    print("  ",row[0],"  ", row[1])



cur.execute("SELECT * FROM num_categorie_3;")
rows=cur.fetchall()
print("\nShow me the results:\n")
for row in rows:
    print("  ",row[0],"  ", row[1])



cur.execute("SELECT * FROM num_categ_issuer;")
rows=cur.fetchall()
print("\nShow me the results:\n")
for row in rows:
    print("  ",row[0],"  ", row[1])

#conn.commit()





cur.execute("SELECT * FROM num_niv_seniorite;")
rows=cur.fetchall()
print("\nShow me the results:\n")
for row in rows:
    print("  ",row[0],"  ", row[1])
