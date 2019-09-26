import tempfile
import boto3
import botocore
import webbrowser
from botocore.client import Config
import os

def CardCreator(company, phoneNumber, street, city, region, code, country, website, note):
    
    access_key = os.environ['S3_KEY']
    secret_key = os.environ['S3_SECRET']
    regionS3 = "eu-central-1"
    key = str(company) + '.vcf'
    bucket = os.environ['S3_BUCKET']
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

    file.seek(0)
    s3_client = boto3.client('s3', region_name=regionS3, aws_access_key_id=access_key, aws_secret_access_key=secret_key, config=Config(signature_version='s3v4'))
    s3 = boto3.resource('s3', region_name=regionS3, aws_access_key_id=access_key, aws_secret_access_key=secret_key, config=Config(signature_version='s3v4'))

    s3.Bucket(bucket).put_object(Key=key, Body=file)
    objectUrl = s3_client.generate_presigned_url(ClientMethod='get_object',Params={'Bucket': bucket,'Key': key})
    response = webbrowser.open(str(objectUrl),new=2,autoraise=1)
    print(response)
