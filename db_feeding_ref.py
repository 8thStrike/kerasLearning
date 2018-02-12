import psycopg2
import csv

conn=psycopg2.connect("dbname=postgres user=reporting password=Finance2018 host=172.16.0.81")



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


#---------------------------------------------------------------------------Feed de la table ref_coupon--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/ref_coupon.csv'), delimiter=';')
cur=conn.cursor()

for row in data:
    cur.execute("""INSERT INTO ref_coupon (id_sec, cpn_nom , cpn_freq) VALUES (%s, %s, %s);""", row)
#    print("nothing")


#---------------------------------------------------------------------------Feed de la table ref_oblig--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/ref_oblig.csv'), delimiter=';')
cur=conn.cursor()
for row in data:
    cur.execute("""INSERT INTO ref_oblig (id_sec, id_niv_seniorite , maturity , issuer_date , id_indice ) VALUES (%s, %s, %s, %s, %s);""", row)
#    print("nothing")

#---------------------------------------------------------------------------Feed de la table rtg--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/rtg.csv'), delimiter=';')
cur=conn.cursor()
for row in data:
    cur.execute("""INSERT INTO rtg (id_sec, id_rtg_CRPN, date_last_changed ) VALUES (%s, %s, %s);""", row)
#    print("nothing")

#---------------------------------------------------------------------------Feed de la table call_dates--------------------------------------------------------------------
data = csv.reader(open('/home/edouard/Documents/projet/kera/data/Documents/Edouard/Travail/database/call_dates.csv'), delimiter=';')
cur=conn.cursor()
for row in data:
    cur.execute("""INSERT INTO call_dates (id_sec, next_call_date, date_last_changed ) VALUES (%s, %s, %s);""", row)
#    print("nothing")





conn.commit()
