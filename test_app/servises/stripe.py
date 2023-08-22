import http.client, urllib.parse
import json


class Stripe():
    __publishable_key = "pk_test_51NUur8KJHznOCE3kXzn1PhAiGttVjLB0EfBz1GxplgErBKk18ltE4kT9mQO3NeCHFCB23QKlS5Gn7Yy2mhfoKo1Q00ojjH10ue"
    __secret_key = "sk_test_51NUur8KJHznOCE3kBFZAC69x8gACpTV744xaIMGnanKRUg00RZiO7MO2HupPAPHs97GrS5bRv1HReculhpQzVeow00ZWrBMb0W"

    def add_card(self , number , month , year , cvc):
        conn = http.client.HTTPSConnection('api.stripe.com')
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {self.__secret_key}'
        }
        params = urllib.parse.urlencode(
            {
               'card[number]': number,
               'card[exp_month]': month, 
               'card[exp_year]': year,
               'card[cvc]': cvc
            }
        )
        conn.request('POST', '/v1/tokens', params, headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        token = json.loads(data)

        conn.close()
   #     print(response , token)

    def create_payment(self , cost):
        amount = int(cost) * 100 
        conn = http.client.HTTPSConnection('api.stripe.com')
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {self.__secret_key}'
        }
        params = urllib.parse.urlencode(
            {
               'amount': amount ,
               'currency': "usd", 
               'payment_method': "pm_card_visa" 
            }
        )
        conn.request('POST', '/v1/payment_intents', params, headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        token = json.loads(data)
        return token['id']
    
    def confirm_payment(self , id ):
        conn = http.client.HTTPSConnection('api.stripe.com')
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {self.__secret_key}' 
        }
        params = urllib.parse.urlencode(
            {
               'payment_method': "pm_card_visa" 
            }
        )
        conn.request('POST', f'/v1/payment_intents/{id}/confirm', params, headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        token = json.loads(data)
     #   print(token)