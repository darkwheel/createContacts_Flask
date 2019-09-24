def AddressExtractor(address):

    streetNumber = address['result']['address_components'][0]['short_name']
    streetName = address['result']['address_components'][1]['short_name']
    street = streetName + " " + streetNumber
    city = address['result']['address_components'][3]['short_name']
    region = address['result']['address_components'][5]['long_name']
    country = address['result']['address_components'][6]['long_name']
    code = address['result']['address_components'][7]['short_name']

    return [street, city, region, code, country]

def DetailExtractor(detailedInformation):
    phone = detailedInformation['result']['international_phone_number']
    noteList = detailedInformation['result']['opening_hours']['weekday_text']
    website = detailedInformation['result']['website']

    return [phone, website, noteList]

