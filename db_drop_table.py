import psycopg2

conn=psycopg2.connect("dbname=postgres user=reporting password=Finance2018 host=172.16.0.81")

cur=conn.cursor()

#22 tables to drop if we need to go back to square zero
cur.execute("""drop table ref_oblig;""")    #1
cur.execute("""drop table ref_global;""")  #2
cur.execute("""drop table call_dates;""")  #3
cur.execute("""drop table coupon_daily;""")  #4
cur.execute("""drop table floating;""")  #5
cur.execute("""drop table index_base;""")  #6
cur.execute("""drop table monetaire;""")  #7
cur.execute("""drop table mouvements;""")  #8
cur.execute("""drop table num_categ_issuer;""")  #9
cur.execute("""drop table num_categorie_1;""")  #10
cur.execute("""drop table num_categorie_2;""")  #11
cur.execute("""drop table num_categorie_3;""")  #12
cur.execute("""drop table remboursement_dates;""")  #13
cur.execute("""drop table num_group;""")  #14
cur.execute("""drop table num_indice;""")  #15
cur.execute("""drop table num_niv_seniorite;""")  #16
cur.execute("""drop table num_pays_risque;""")  #17
cur.execute("""drop table rtg;""")  #18
cur.execute("""drop table num_rtg;""")  #19
cur.execute("""drop table num_sector;""")  #20
cur.execute("""drop table ref_issuer;""")  #21
cur.execute("""drop table ref_coupon;""")  #22



conn.commit()
