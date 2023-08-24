class Networks:
    url = "https://restful-booker.herokuapp.com"
    CreateToken = url + "/auth"
    Booking = url + "/booking"
    HealthCheck = url + "/ping"

#Получение ID
def getIDsFromResponse(resp):
    id_array = []

    for key in resp:
        id_array.append(key.get("bookingid"))

    return id_array