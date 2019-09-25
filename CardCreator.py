import pprint
from flask import send_file
import tinys3

def CardCreator(company, phoneNumber, street, city, region, code, country, website, note):
    file = tempfile.TemporaryFile("w+b")

    file.write("BEGIN:VCARD\nVERSION:3.0\nPRODID:-//Apple Inc.//iPhone OS 13.0//EN\nN:;;;;\n".encode("utf-8"))
    file.write(("FN:" + str(company) + "\n").encode("utf-8"))
    file.write(("ORG:" + str(company) + "\n").encode("utf-8"))
    if note:
        file.write("NOTE:".encode("utf-8"))
        for i in range(0, len(note)):
            if i is len(note)-1:
                file.write(str(note[i]).encode("utf-8"))
                continue
            file.write((str(note[i]) + "\\n").encode("utf-8"))

    file.write(("\nTEL;type=WORK;type=VOICE;type=pref:" + str(phoneNumber) + "\n").encode("utf-8"))
    file.write(("item1.ADR;type=WORK;type=pref:;;" + str(street) + ";" + str(city) + ";" + str(region) + ";" + str(code) + ";" + str(country) + "\n").encode("utf-8"))
    file.write("item1.X-ABADR:de\n".encode("utf-8"))
    file.write(("item2.URL;type=pref:" + str(website) + "\n").encode("utf-8"))
    file.write("item2.X-ABLabel:_$!<HomePage>!$_\nX-ABShowAs:COMPANY\nEND:VCARD\n".encode("utf-8"))
    
    S3 = tinys3.Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,tls=True)
    S3.upload(str(company) + '.vcf',file,S3_BUCKET)
