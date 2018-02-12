import psycopg2
import csv

conn=psycopg2.connect("dbname=postgres user=reporting password=Finance2018 host=172.16.0.81")



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


#---------------------------------------------------------------------------Feed de la table num_niv_indice--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/num_indice.csv'), delimiter=';')
cur=conn.cursor()

for row in data:
    cur.execute("""INSERT INTO num_indice (id_indice, indice) VALUES (%s, %s);""", row)
#    print("nothing")

#---------------------------------------------------------------------------Feed de la table num_group--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/num_group.csv', newline='', encoding='utf-8'), delimiter=';')
cur=conn.cursor()

for row in data:
    cur.execute("""INSERT INTO num_group (id_group, group_name) VALUES (%s, %s);""", row)

#---------------------------------------------------------------------------Feed de la table num_rtg--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/num_rtg.csv', newline='', encoding='utf-8'), delimiter=';')
cur=conn.cursor()

for row in data:

    cur.execute("""INSERT INTO num_rtg (id_rtg_CRPN, rtg) VALUES (%s, %s);""", row)




conn.commit()
