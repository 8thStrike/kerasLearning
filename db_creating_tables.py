import psycopg2

conn=psycopg2.connect("dbname=postgres user=reporting password=Finance2018 host=172.16.0.81")

cur=conn.cursor()

#cur.execute("""SELECT * FROM PX_APOLLO WHERE DATE_VL='26/10/2016';""")
#cur.execute("""SELECT PX_APOLLO.DATE_VL, TABLE_RISQUE.NAME FROM PX_APOLLO, TABLE_RISQUE TABLE_RISQUE WHERE TABLE_RISQUE.ISIN = PX_APOLLO.ISIN AND ((PX_APOLLO.DATE_VL={d '2017-10-26'})))""")

#cur.execute("""drop table ref_oblig;""")
#cur.execute("""drop table ref_global;""")



#Create Table ref_global -----------------------------------------------------------------------------------------------------------------------------------------          0 table
cur.execute("""CREATE TABLE ref_global (id_sec SERIAL PRIMARY KEY, isin VARCHAR(12) NOT NULL, name VARCHAR(70) NOT NULL, id_issuer INT NOT NULL, id_categorie_1 INT NOT NULL, id_categorie_2 INT NOT NULL, id_categorie_3 INT NOT NULL) TABLESPACE financier;""")
#Create correspondance table num_categorie_1
cur.execute("""CREATE TABLE num_categorie_1 (id_categorie_1 INT, categorie_1 VARCHAR(50)) TABLESPACE financier;""")
#Create correspondance table num_categorie_2
cur.execute("""CREATE TABLE num_categorie_2 (id_categorie_2 INT, categorie_2 VARCHAR(50)) TABLESPACE financier;""")
#Create correspondance table num_categorie_3
cur.execute("""CREATE TABLE num_categorie_3 (id_categorie_3 INT, categorie_3 VARCHAR(50)) TABLESPACE financier;""")

#Create table ref_issuer -----------------------------------------------------------------------------------------------------------------------------------------          4 tables Created
cur.execute("""CREATE TABLE ref_issuer (id_issuer SERIAL PRIMARY KEY, issuer VARCHAR(50), id_categ_issuer INT NOT NULL, id_pays_risque INT NOT NULL, id_group INT NOT NULL, id_sector INT NOT NULL) TABLESPACE financier;""")
#Create correspondance table num_categ_issuer
cur.execute("""CREATE TABLE num_categ_issuer(id_categ_issuer INT NOT NULL, categ_issuer VARCHAR(20)) TABLESPACE financier;""")
#Create correspondancetable num_sector_issuer
cur.execute("""CREATE TABLE num_sector(id_sector INT NOT NULL, sector VARCHAR(30)) TABLESPACE financier;""")
#Create correspondance table num_pays_risque
cur.execute("""CREATE TABLE num_pays_risque(id_pays_risque INT NOT NULL, pays_risque VARCHAR(20)) TABLESPACE financier;""")
#Create correspondance table num_group
cur.execute("""CREATE TABLE num_group(id_group INT NOT NULL, group_name VARCHAR(50)) TABLESPACE financier;""")

#Create table ref_oblig -----------------------------------------------------------------------------------------------------------------------------------------              9 tables Created
cur.execute("""CREATE TABLE ref_oblig (id_sec INT PRIMARY KEY NOT NULL, id_niv_seniorite INT NOT NULL, maturity DATE, issuer_date DATE, id_indice INT NOT NULL) TABLESPACE financier;""")
cur.execute("""CREATE TABLE num_niv_seniorite (id_niv_seniorite SERIAL PRIMARY KEY, niv_seniorite VARCHAR(20)) TABLESPACE financier;""")
cur.execute("""CREATE TABLE num_indice (id_indice INT NOT NULL, indice VARCHAR(40)) TABLESPACE financier;""")

#Create table ref_coupon -----------------------------------------------------------------------------------------------------------------------------------------              9 tables Created
cur.execute("""CREATE TABLE ref_coupon (id_sec INT PRIMARY KEY NOT NULL, cpn_nom DOUBLE PRECISION, cpn_freq DOUBLE PRECISION NOT NULL) TABLESPACE financier;""")

#Create table Coupon -------------------------------------------------------------------------------------------------------------------------------------------------          13 tables created
cur.execute("""CREATE TABLE coupon_daily (id_sec INT NOT NULL, date_vl DATE,  cpn_couru DOUBLE PRECISION NOT NULL, PRIMARY KEY (id_sec, date_vl)) TABLESPACE financier;""")

#Create table rtg -------------------------------------------------------------------------------------------------------------------------------------------------             14 tables Created
cur.execute("""CREATE TABLE rtg (id_sec INT NOT NULL, id_rtg_CRPN INT, date_last_changed DATE, PRIMARY KEY (id_sec, date_last_changed)) TABLESPACE financier;""")
cur.execute("""CREATE TABLE num_rtg (id_rtg_CRPN INT NOT NULL, rtg VARCHAR(20)) TABLESPACE financier;""")

#Create table mouvements -------------------------------------------------------------------------------------------------------------------------------------------------      15 tables created
cur.execute("""CREATE TABLE mouvements (id_mvt SERIAL PRIMARY KEY, id_sec INT NOT NULL, direction INT NOT NULL, quantity INT NOT NULL, price DOUBLE PRECISION, yield DOUBLE PRECISION, date_vl DATE) TABLESPACE financier;""")

#Create table date de prochain call---------------------------------------------------------------------------------------------------------------------------------            16 tables created
cur.execute("""CREATE TABLE call_dates (id_sec INT NOT NULL, next_call_date DATE, date_last_changed DATE, PRIMARY KEY (id_sec, date_last_changed)) TABLESPACE financier;""")

#Create table date remboursement anticipé---------------------------------------------------------------------------------------------------------------------------------            17 tables created
cur.execute("""CREATE TABLE remboursement_dates (id_rmbst SERIAL PRIMARY KEY, id_sec INT NOT NULL, remboursement_date DATE, date_last_changed DATE) TABLESPACE financier;""")

#Create table base d'indice---------------------------------------------------------------------------------------------------------------------------------                       18 tables created
cur.execute("""CREATE TABLE index_base (id_base_indice SERIAL PRIMARY KEY, id_sec INT NOT NULL, base_indice DOUBLE PRECISION) TABLESPACE financier;""")

#Create table floating---------------------------------------------------------------------------------------------------------------------------------            19 tables created
cur.execute("""CREATE TABLE floating (id_floating SERIAL PRIMARY KEY, id_sec INT NOT NULL, floater INT, date_vl DATE) TABLESPACE financier;""")

#Create table monetaire---------------------------------------------------------------------------------------------------------------------------------            20 tables created
cur.execute("""CREATE TABLE monetaire (id_monetaire SERIAL PRIMARY KEY, id_sec INT NOT NULL, monetaire INT NOT NULL) TABLESPACE financier;""")

#------------------------------------------------------------------------------------------------------------------------------------------------            21 tables created


#Modify definitively the db
conn.commit()
'''


rows=cur.fetchall()

print("\nShow me the results:\n")
for row in rows:
    print("  ",row[0])
'''
