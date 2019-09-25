import googlemaps
from GoogleMapsAPIKey import getMyAPIKey
from CardCreator import CardCreator
from AddressExtractor import AddressExtractor
from AddressExtractor import DetailExtractor


# Define API KEy
# apiKey = getMyAPIKey()

def GoogleAccesser(apiKey, userInput):
    # Define our client
    gmaps = googlemaps.Client(key=apiKey)

    # Define our search
    placesResult = gmaps.find_place(input=userInput, input_type="textquery",
                                    fields=["place_id", "name", "formatted_address"])

    address = gmaps.place(placesResult['candidates'][0]['place_id'], fields=["address_component"])
    detailInformation = gmaps.place(placesResult['candidates'][0]['place_id'],
                                    fields=["international_phone_number", "opening_hours", "website"])
    name = placesResult['candidates'][0]['name']
    splitAddress = AddressExtractor(address)
    details = DetailExtractor(detailInformation)

    CardCreator(name, details[0], splitAddress[0], splitAddress[1], splitAddress[2], splitAddress[3],
                splitAddress[4], details[1], details[2])
    # return name of vCard
    return name
