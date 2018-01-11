import psycopg2

conn=psycopg2.connect("dbname=postgres user=reporting password=Crpn2014 host=localhost")

cur=conn.cursor()

#cur.execute("""SELECT * FROM PX_APOLLO WHERE DATE_VL='26/10/2016';""")
#cur.execute("""SELECT PX_APOLLO.DATE_VL, TABLE_RISQUE.NAME FROM PX_APOLLO, TABLE_RISQUE TABLE_RISQUE WHERE TABLE_RISQUE.ISIN = PX_APOLLO.ISIN AND ((PX_APOLLO.DATE_VL={d '2017-10-26'})))""")

#cur.execute("""drop table ref_oblig;""")
#cur.execute("""drop table ref_global;""")



#Create Table ref_global -----------------------------------------------------------------------------------------------------------------------------------------
cur.execute("""CREATE TABLE ref_global (id_sec INT PRIMARY KEY NOT NULL AUTOINCREMENT, isin VARCHAR(12) NOT NULL, name VARCHAR(70) NOT NULL, id_issuer INT NOT NULL, categorie_1 INT NOT NULL, categorie_2 INT NOT NULL, categorie_3 INT NOT NULL);""")
#Create correspondance table num_categorie_1
cur.execute("""CREATE TABLE num_categorie_1 (id_categorie_1 INT, categorie_1 VARCHAR(50));""")
#Create correspondance table num_categorie_2
cur.execute("""CREATE TABLE num_categorie_2 (id_categorie_2 INT, categorie_2 VARCHAR(50));""")
#Create correspondance table num_categorie_3
cur.execute("""CREATE TABLE num_categorie_3 (id_categorie_3 INT, categorie_3 VARCHAR(50));""")

#Create table ref_issuer -----------------------------------------------------------------------------------------------------------------------------------------
cur.execute("""CREATE TABLE ref_issuer (id_issuer INT NON NULL, issuer VARCHAR(50), id_categ_issuer INT NON NULL, id_pays_risque INT NON NULL, id_group INT NON NULL);""")
#Create correspondance table num_categ_issuer
cur.execute("""CREATE TABLE num_categ_issuer(id_categ_issuer INT NON NULL, categ_isser VARCHAR(20));""")
#Create correspondance table num_pays_risque
cur.execute("""CREATE TABLE num_pays_risque(id_pays_risque INT NON NULL, pays_risque VARCHAR(20));""")
#Create correspondance table num_group
cur.execute("""CREATE TABLE num_group(id_group INT NON NULL, group VARCHAR(50));""")

#Create table ref_oblig -----------------------------------------------------------------------------------------------------------------------------------------
cur.execute("""CREATE TABLE ref_oblig (id_sec INT PRIMARY KEY NOT NULL, id_niv_seniorite INT NOT NULL, maturity DATE, issuer_date DATE, id_indice INT NOT NULL);""")
cur.execute("""CREATE TABLE num_niv_seniorite (id_niv_seniorite INT NOT NULL, niv_seniorite VARCHAR(20));""")
cur.execute("""CREATE TABLE num_indice (id_indice INT NOT NULL, indice VARCHAR(40));""")

#Create table Coupon -------------------------------------------------------------------------------------------------------------------------------------------------
cur.execute("""CREATE TABLE coupon_daily (id_cpn INT PRIMARY KEY NOT NULL, id_sec INT NOT NULL, date_vl DATE, cpn_nom DOUBLE NOT NULL, cpn_freq DOUBLE NOT NULL, cpn_couru DOUBLE NOT NULL);""")

#Create table rtg -------------------------------------------------------------------------------------------------------------------------------------------------
cur.execute("""CREATE TABLE rtg (id_rtg INT PRIMARY KEY NOT NULL, id_sec INT NOT NULL, id_rtg_CRPN INT, date_last_changed DATE);""")
cur.execute("""CREATE TABLE num_rtg (id_rtg_CRPN INT NOT NULL, rtg );""")

#Modify definitively the db
conn.commit()
'''


rows=cur.fetchall()

print("\nShow me the results:\n")
for row in rows:
    print("  ",row[0])
'''
