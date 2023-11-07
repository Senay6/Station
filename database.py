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
            email = line[7]
            beoordeling_datum_tijd = line[4]

            cur.execute("INSERT INTO reiziger (naam_r) VALUES (%s)", (naam_r,))
            cur.execute("INSERT INTO moderator (naam_m, email) VALUES (%s, %s)", (naam_m, email,))
            cur.execute(("SELECT reiziger_id from reiziger"))
            cur.execute("SELECT moderator_id from moderator")
            # get id of reiziger
            #get id of reiziger
            cur.execute(
                "INSERT INTO bericht (inhoud, bericht_datum_tijd, station, beoordeling_datum_tijd, status) VALUES (%s, %s, %s, %s, %s)",
                (inhoud, bericht_datum_tijd, station, beoordeling_datum_tijd, status,))

            continue

    with open('station_scherm.csv', mode='w', newline='') as file:
        pass

connection.commit()
cur.close()
connection.close()