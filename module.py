import csv
from datetime import datetime
import random

# MODULE 1
personen = ['1', '2', '3']
#keuzes = ["Ja", "Nee"] # bence buna gerek yok.

while True:
    print(" ")
    keuze = input("Als u een reiziger bent, type [1].\nAls u een moderator bent, type [2].\nAls u het menu wilt verlaten, typt [3]: ")
    # if durumu ekledim. keuze icin farkli birsey girince hata vermesin diye
    if keuze not in personen:
        print("U kunt alleen maar 1,2 of 3 kiezen! Nog een keer proberen.")
        continue
    if keuze == '1':
        while True:
            naam = input("Schrijf alstublieft uw naam. Wilt u liever anoniem blijven, vul dan niets in : ").upper()
            #kayitlar hep ayni formatta kayit olsun diye buyuk harf yaptim. upper() metodu ile
            bericht = input("Geef uw mening over het NS-Station (max. 140 character): ")

            if len(bericht) >= 140:
                print("Sorry, u mag maximaal 140 characters invoeren. Probeer opnieuw.")
                break
            else:
                print("Je mening is succesvol doorgestuurd naar de moderators.")

            if naam == "":
                naam = 'ANONIEM'
            stations = ['Haarlem', 'Arnhem', 'Almere', 'Amersfoort', 'Helmond', 'Venlo', 'Oss', 'Amsterdam', 'Zaandam']
            station_keuze = random.choice(stations)

            tijd = str(datetime.now())

            lijst = []
            lijst.append(naam)
            lijst.append(bericht)
            lijst.append(tijd)
            lijst.append(station_keuze)

            with open('reiziger.csv', mode='a', newline='') as file:
                printer = csv.writer(file, delimiter=',')
                printer.writerow(lijst)

            reiziger_choice = input("Wilt u nog een mening doorgeven? [J]a / [N]ee ").upper()
            # alinan inputu upper ile buyuk harfe donusturdumki if sartina tam uysun.
            # ericht_2 yerine choice olabilir
            if reiziger_choice == 'NEE' or reiziger_choice == 'N':
                keuze = '3' # break ile donguden sonra tum programdan cikar
                break
            if reiziger_choice == 'JA' or reiziger_choice == 'J':
                continue
            # rakam yada baska birsey girer ise diye ELSE durumu ekledim
            else:
                print("Sorry. Er is iets fout gegaan.")
                break
        #continue # buna gerek yok zaten while true loop icindeyiz

# MODULE 2

    if keuze == '2':
        wachtwoord_m = '123'
        wachtwoord = input("Vul de moderator wachtwoord: ")
        if wachtwoord_m != wachtwoord:
            print("Onjuiste wachtwoord.")

        else:
            mod_naam = input("Vul uw naam in als moderator: ").upper()
            mod_email = input("Vul uw E-mail adres: ")
            # r+ modda dosya yoksa yeniden olusturulmaz. Amacim reiziger dosyasindaki bericht sayisini bilmek.
            with open('reiziger.csv', mode='r+') as file_r:
                read_reiziger = csv.reader(file_r)
                list_van_berichten = list(read_reiziger)
                bericht_count = len(list_van_berichten)  # reiziger dosyasindaki bericht sayisi
                if bericht_count == 0:
                    print("Er is geen bericht.")
                    continue # eger burada break kullanirsak tamamen cikar programdan. simdi menu geliyor tekrar
                else:
                    while True:
                        for line1 in list_van_berichten:
                            ## moderator basarili giris yapinca exit sorulmasin. en sonda sorulsun
                            #exit = input("Typ [E]xit om de moderatoroptie af te sluiten. ").upper()
                            #exit yerine sluiten olabilir. cunku exit gibi onceden tanimli bazi kelimeler sorun olur.
                            #if exit == 'E' or exit == 'EXIT':
                            #    break
                            #else:
                            print(line1)
                            status = input("Is het bericht [G]oedgekeurd of [A]fgekeurd?: ").upper()
                            #kelimeler cok uzun G veya A girmesi yeter bence
                            tijd_2 = str(datetime.now())

                            lijst_2 = []
                            lijst_2.append(tijd_2)
                            lijst_2.append(status)
                            lijst_2.append(mod_naam)
                            lijst_2.append(mod_email)

                            with open('moderator.csv', mode='a', newline='') as file_m: # file idi file_m
                                printer = csv.writer(file_m, delimiter=',')
                                printer.writerow(lijst_2)

                            with open('station_scherm.csv', mode='a', newline='') as file_ss: # file idi file_s
                                scherm = line1 + lijst_2
                                printer = csv.writer(file_ss, delimiter=',')
                                printer.writerow(scherm)

                            with open('reiziger.csv', mode='r+') as file_r: # file idi file_r
                                reader = csv.reader(file_r)
                                lines = list(reader)
                                print('Deleting...', lines[0])
                                lines.remove(lines[0])
                                #deleted_line = line1 # bu satirlara gerek yok
                                #for line in lines:
                                    #if deleted_line == line:
                                        #print('Deleting...', line, line1)
                                        #lines.remove(line)
                            with open('reiziger.csv', mode='w', newline='') as file_r: # file idi file_w
                                writer = csv.writer(file_r)
                                writer.writerows(lines)
                            bericht_count = bericht_count-1
                            if bericht_count == 0:
                                print("Gefeliciteerd! Berichten is op!")
                                keuze = '3'  # break ile donguden sonra tum programdan cikar
                                break
                            moderator_choice = input(f"Berichten Count: {bericht_count} [E]xit / [D]oorgaan ").upper()
                            # exit yerine sluiten olabilir. cunku exit gibi onceden tanimli bazi kelimeler sorun olur.
                            if moderator_choice == 'E' or moderator_choice == 'EXIT':
                                keuze = '3'  # break ile donguden sonra tum programdan cikar
                                break
                            else:
                                continue
                        break
    if keuze == '3':
        print("Tot ziens!")
        break
