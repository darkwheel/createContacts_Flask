# createContactsWithGoogle

This reason I created this repository was that I wanted to easily create a contact in my iPhone with the information 
provided by a Google search. Every information is already in that contact card of google maps, but to copy paste every information is
annoying.

So to use my repository you have to clone the repo and create a file for __your Google API Key__ (I am not providing mine :) )
This file should be named __GoogleMapsAPIKey__ and you should create an function __getMyAPIKey()__ within this file with following body:

```python
def getMyAPIKey():
    apiKey = FillInYourAPIKeyHere
    return apiKey
```

This provides the right API key for the GoogleAccesser function.

If you run the GoogleAccesser.py file you have to type in what you want to search (which company) and it will perform a google maps search 
with the entered term and it will pick the first result to create a contact card. The vCard file is saved in your repository folder.
This will only work for company vCards not for privat ones, because the private ones are not in Google Maps :)

If there are any bugs, please let me now and i will try to help you!


