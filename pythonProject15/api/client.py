import requests

class OrderBaseClient:
    url = "https://restful-booker.herokuapp.com"

    def create_token(self):
        return requests.post(self.url + '/auth')

    def booking_all(self):
        return requests.get(self.url + f'/booking/')

    def booking_id(self):
        return requests.get(self.url + f'/:id/{id}')

    def booking_create(self, traveller):
        return requests.post(self.url + '/booking', json=traveller)

    def booking_update(self, traveller):
        return requests.put(self.url + '/booking', json=traveller)

    def booking_part_update(self, traveller):
        return requests.patch(self.url + '/:id', json=traveller)

    def booking_delete(self, traveller):
        return requests.delete(self.url + '/:id', json=traveller)

    def booking_ping(self):
        return requests.get(self.url + '/ping')

    def create_order(self, order):
        return requests.post(self.url + '/orders', json=order)

    def get(self, order_id):
        return requests.get(self.url + f'/orders/{order_id}')


order_base_client = OrderBaseClient()
