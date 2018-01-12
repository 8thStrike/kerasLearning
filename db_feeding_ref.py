import psycopg2
import csv

conn=psycopg2.connect("dbname=postgres user=reporting password=Crpn2014 host=localhost")



#---------------------------------------------------------------------------Feed de la table ref_global--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/ref_global.csv'), delimiter=';')
cur=conn.cursor()

for row in data:
    cur.execute("""INSERT INTO ref_global (id_sec, isin, name, id_issuer, id_categorie_1, id_categorie_2, id_categorie_3) VALUES (%s, %s, %s, %s, %s, %s, %s);""", row)
#    print("nothing")


#---------------------------------------------------------------------------Feed de la table ref_issuer--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/ref_issuer.csv'), delimiter=';')
cur=conn.cursor()

for row in data:
    cur.execute("""INSERT INTO ref_issuer (id_issuer, issuer, id_categ_issuer, id_pays_risque, id_group, id_sector) VALUES (%s, %s, %s, %s, %s, %s);""", row)
#    print("nothing")



conn.commit()
