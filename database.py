import csv
import psycopg2

hostname = '20.0.35.176'
database = 'station'
username = 'postgres'
pword = 'Senay!2023'
port_id = 5432

connection = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pword,
    port=port_id)

cur = connection.cursor()
geschreven_mail = None
reiziger_reiziger_id = None
with open('station_scherm.csv', mode='r') as file_ss:
    reader1 = csv.reader(file_ss)
    lines = list(reader1)

    for line in lines:
        status = line[5]
        if status == 'Afgekeurd' or status == 'A':
            continue

        if status == 'Goedgekeurd' or status == 'G':
            naam_r = line[0]
            inhoud = line[1]
            bericht_datum_tijd = line[2]
            station = line[3]
            naam_m = line[6]
            email_1 = line[7]
            beoordeling_datum_tijd = line[4]

            reiziger_reiziger_id = cur.execute("SELECT reiziger_id FROM reiziger")
            if reiziger_reiziger_id == None:
                cur.execute("INSERT INTO reiziger (naam_r) VALUES (%s)", (naam_r,))
                cur.execute("SELECT reiziger_id FROM reiziger")
                reiziger_reiziger_id =

            else:
                cur.execute("SELECT reiziger_id FROM reiziger")
                reiziger_id_values = cur.fetchall()

                for reiziger_id_value in reiziger_id_values:
                    cur.execute("UPDATE bericht SET reiziger_id = %s WHERE reiziger_id IS NULL", (reiziger_id_value[0],))
                    break



            if email_1 == geschreven_mail:
                pass
            else:
                cur.execute("INSERT INTO moderator (naam_m, email) VALUES (%s, %s)", (naam_m, email_1,))
                geschreven_mail = email_1

            moderator_moderator_id = cur.execute("SELECT moderator_id FROM moderator")
            if moderator_moderator_id == None:
                pass
            else:
                cur.execute("SELECT moderator_id FROM moderator")
                moderator_id_values = cur.fetchall()

                for moderator_id_value in moderator_id_values:
                    cur.execute("UPDATE bericht SET moderator_id = %s WHERE moderator_id IS NULL", (moderator_id_value[0],))
                    break
            #cur.execute("SELECT reiziger_id FROM reiziger")
            #reiziger_id_values = cur.fetchall()

            #for reiziger_id_value in reiziger_id_values:
            #    cur.execute("UPDATE bericht SET reiziger_id = %s WHERE reiziger_id IS NULL", (reiziger_id_value[0],))
            #    break

            #cur.execute("SELECT moderator_id FROM moderator")
            #moderator_id_values = cur.fetchall()

            #for moderator_id_value in moderator_id_values:
            #    cur.execute("UPDATE bericht SET moderator_id = %s WHERE moderator_id IS NULL", (moderator_id_value[0],))
            #    break
            cur.execute(
                "INSERT INTO bericht (inhoud, bericht_datum_tijd, station, beoordeling_datum_tijd, status) VALUES (%s, %s, %s, %s, %s)",
                (inhoud, bericht_datum_tijd, station, beoordeling_datum_tijd, status,))


            continue
        continue

    with open('station_scherm.csv', mode='w', newline='') as file:
        pass
geschreven_mail = None

connection.commit()
cur.close()
connection.close()