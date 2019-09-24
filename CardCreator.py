import pprint


def CardCreator(company, phoneNumber, street, city, region, code, country, website, note):
    file = open(str(company) + ".vcf", "w")

    file.write("BEGIN:VCARD\nVERSION:3.0\nPRODID:-//Apple Inc.//iPhone OS 13.0//EN\nN:;;;;\n")
    file.write("FN:" + company + "\n")
    file.write("ORG:" + company + "\n")
    if note:
        file.write("NOTE:")
        for i in range(0, len(note)):
            if i is len(note)-1:
                file.write(note[i])
                continue
            file.write(note[i] + "\\n")

    file.write("\nTEL;type=WORK;type=VOICE;type=pref:" + phoneNumber + "\n")
    file.write("item1.ADR;type=WORK;type=pref:;;" + street + ";" + city + ";" + region + ";" + code + ";" + country + "\n")
    file.write("item1.X-ABADR:de\n")
    file.write("item2.URL;type=pref:" + website + "\n")
    file.write("item2.X-ABLabel:_$!<HomePage>!$_\nX-ABShowAs:COMPANY\nEND:VCARD\n")

    file.close()

