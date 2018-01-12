import psycopg2
import csv

conn=psycopg2.connect("dbname=postgres user=reporting password=Crpn2014 host=localhost")



#---------------------------------------------------------------------------Feed de la table num_categorie_1--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/num_categorie_1.csv'), delimiter=';')
cur=conn.cursor()

for row in data:
    cur.execute("""INSERT INTO num_categorie_1 (id_categorie_1, categorie_1) VALUES (%s, %s);""", row)
#    print("nothing")



#---------------------------------------------------------------------------Feed de la table num_categorie_2--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/num_categorie_2.csv'), delimiter=';')
cur=conn.cursor()

for row in data:
    cur.execute("""INSERT INTO num_categorie_2 (id_categorie_2, categorie_2) VALUES (%s, %s);""", row)
#    print("nothing")



#---------------------------------------------------------------------------Feed de la table num_categorie_3--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/num_categorie_3.csv'), delimiter=';')
cur=conn.cursor()

for row in data:
    cur.execute("""INSERT INTO num_categorie_3 (id_categorie_3, categorie_3) VALUES (%s, %s);""", row)
#    print("nothing")


#---------------------------------------------------------------------------Feed de la table num_categ_issuer--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/num_categ_issuer.csv'), delimiter=';')
cur=conn.cursor()

for row in data:
    cur.execute("""INSERT INTO num_categ_issuer (id_categ_issuer, categ_issuer) VALUES (%s, %s);""", row)
#    print("nothing")


#---------------------------------------------------------------------------Feed de la table num_sector--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/num_sector.csv'), delimiter=';')
cur=conn.cursor()

for row in data:
    cur.execute("""INSERT INTO num_sector (id_sector, sector) VALUES (%s, %s);""", row)
#    print("nothing")


#---------------------------------------------------------------------------Feed de la table num_niv_seniorite--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/num_niv_seniorite.csv'), delimiter=';')
cur=conn.cursor()

for row in data:
    cur.execute("""INSERT INTO num_niv_seniorite (id_niv_seniorite, niv_seniorite ) VALUES (%s, %s);""", row)
#    print("nothing")







conn.commit()
