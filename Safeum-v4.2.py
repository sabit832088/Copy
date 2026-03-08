import requests
import random
import json
import time
import os
import webbrowser
from gzip import decompress
from random import choices
from concurrent.futures import ThreadPoolExecutor
from websocket import create_connection
from ssl import CERT_NONE


try:
    from licensing.models import *
    from licensing.methods import Key, Helpers
except ImportError:
    os.system('pip install licensing')
    from licensing.models import *
    from licensing.methods import Key, Helpers

RSAPubKey = "<RSAKeyValue><Modulus>txHjmm2sSOkPgl/5JJxEu6JEooQGKXS0bnEuUjV7eTbOFEHmwM5ZDw85udK9qSIIWVR9MKqBtiVpii/JV1YAqeay+XTxZNct1vOHtbfgmd7kI0FqGUl6i/HF3bzBfu+y9Vy+jn2b6ldtAyRVJfdqQOCtLO0Ob+8puJ3VHCzPig5/7J5vz9wn6LwUIPaUqYvHv7GYY1fZzHaieVOD5z5Nq03KBpSL7LlFveggwxvNXbCclvDP1i+ysVa+Kp9L8huFDTtOH2YSWwrTkFW/XJYgi+L4zI8rFqq/CyFPOjOb0NexFR3fxf11+C1iR0LJUhBf2fm1ZfWb+CBSBl6D81XytQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyIxMDIxMDUwNDAiLCJHdFhCWUFrT1ZhQS93U1ZSOEgvTTFaNlpxVG05SkZXeXZ2WFNSd2JnIl0="

# حالة المفتاح
activation_status = "غير محدد"

def Authkey():
    global activation_status  # لجعل المتغير عامًا
    key = 'IZRMJ-TCFTU-XJNWW-UTJRN'
    result = Key.activate(
        token=auth,
        rsa_pub_key=RSAPubKey,
        product_id='28708',
        key=key,
        machine_code=Helpers.GetMachineCode()
    )

    if result[0] is None or not Helpers.IsOnRightMachine(result[0]):
        activation_status = "المفتاح غير صحيح"
        print("\033[0;37m\033[1;41m الأداة موقفة او معطلة! ❌ تواصل مع @AA8DQ لتفعيلها : {0}\033[0m".format(result[1]))
        webbrowser.open("https://t.me/AA8DQ")  
        exit()
    else:
        activation_status = "شغالة تمام الحمد لله"

# الألوان
L = '\033[1;33m'
C = "\033[1;97m"
Y = '\033[1;34m'
G = '\033[1;32m'
R = '\033[1;31m'
j= '\033[1;36m' 
reset = "\033[0m"

# الشعار
logo = f"""
{Y} ######   ####   #######  #######  ##   ##  ##   ##  
{j}#######  ######  #######  #######  ##   ##  ### ###  
{G}##   ##  ##  ##   ##  ##   ##  ##  ##   ##  #######  
{L} ###     ##  ##   ####     ####    ##   ##  #######  
{R}   ###   ######   ####     ####    ##   ##  ## # ##  
{L}##   ##  ######   ##       ##  ##  ##   ##  ##   ##  
{Y}#######  ##  ##  ####     #######  #######  ##   ##  
{j}######   ##  ##  ####     #######   #####   ##   ##  
"""

# استدعاء الدالة للتحقق من المفتاح
Authkey()

# معلومات الإصدار والمطور
info = f"""
{j}══════════════════════════════════════════
{Y} الاصدار : 4.2.0                        
{L}  عالاساس مطور : @AA8DQ                  
{G} عمل الاداة : {activation_status}             
{j}══════════════════════════════════════════
"""

# طباعة الشعار والمعلومات
print(logo)
print(info)

    



# المتغيرات العامة
failed = 0
success = 0
retry = 0
processed = 0  
accounts = []

#اتذكر ظبط g يارب ما انساها
def get_telegram_info():
    bot_token = input(" \033[0;30m\033[1;47m● أدخل توكن بوتك : \033[0m\n\n")
    chat_id = input(" \033[0;30m\033[1;47m ● ادخل الأيدي الخاص بك :\033[0m \n\n")
    return bot_token, chat_id

TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID = get_telegram_info()


def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"Error sending message to Telegram: {response.text}")
    except Exception as e:
        print(f"Telegram send error: {e}")


def choose_mode():
    print('''\033[0;37m\033[1;43m « 1 » إنشاء بسرعة محددة باختيارك( سحب بقيمة ثابتة ):  \033[0m\n''' )
    print (''' \033[0;37m\033[1;46m « 2 » تشغيل بأقصى سرعة( قد تتعرض للحظر ):       \033[0m\n''')
    print('''\033[0;37m\033[1;44m « 3 » إنشاء حسابات بحقوقك ( أدخل اول خمس حروف ): \033[0m\n''' )
    
    while True:
        try:
            choice = int(input("\033[1;37m>>> \033[0m"))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("\033[0;37m\033[1;41m⚠️ خيار غير صالح. اختر 1، 2، أو 3.\033[0m")
        except ValueError:
            print("\033[0;37m\033[1;41m⚠️ أدخل رقمًا صحيحًا.\033[0m")

# السرعة اتذكر لا خريها مشان ما يروح الاتصال
def choose_speed():
    while True:
        speed = input("\033[0;34m\033[1;47m • SPEED • اختر السرعة من 1 الى 10 ( حيث 1 بطيئة و 10 سريعة جدا ):\033[0m\n")
        if speed.isdigit() and 1 <= int(speed) <= 10:
            return int(speed)
        else:
            print("\033[0;37m\033[1;41m⚠️ اختر سرعة بين 1 و 10.\033[0m")


def work(rate_limit=None, user_input=None, mode=1):
    global failed, success, retry, processed

    if mode == 3 and user_input:
        username = user_input + ''.join(choices('qwertyuioplkjhgfdsazxcvbnm1234567890', k=13))
    else:
        username = ''.join(choices('qwertyuioplkjhgfdsazxcvbnm1234567890', k=14))

    data0 = {
        "action": "Register",
        "subaction": "Desktop",
        "locale": "ar_EG",
        "gmt": "+03",
        "password": {
            "m1x": "20cdd6837f20b8c2d5b49d2869382944066d94701ac3534fe46e7a9319d9baca",
            "m1y": "162855774aa4a4a9f29396b403283eed57523c058cd41128c31d6e3a878257ca",
            "m2": "63d2d920b2cf297900a73f06b4bfdc92e8a6cefdd926b222f9fa7ec4d84be7ca",
            "iv": "5219217a6da410c811a6d64a7eea11b0",
            "message": "6f2562d48d806502fbdc90b00d2bd40e6273df73c6936cc32150713849ceb379d744515929788c0ce41309e1adb5296a9efce8a33b704c5cb39ed6b99cbc617282374535227b957e58a3d701ee2162ed"
        },
        "magicword": {
            "m1x": "3997a0b7cbaf8406fa5899761795691d0663f850d95a55e32f9b3d7f7079dde3",
            "m1y": "9a4698e3c7ecf42e52e0460c2c6c5804e20a95b245a9345877fc29acf373094e",
            "m2": "cf2a5967404191c484d61d1746a0dd5f086b374a2146d5b3b32a5478b75eec15",
            "iv": "24f8933c45ed73e1739cc56dd8817ff1",
            "message": "00600c45db558a41d493435236909142"
        },
        "magicwordhint": "0000",
        "login": str(username),
        "devicename": "Xiaomi 23049PCD8G",
        "softwareversion": "1.1.0.2300",
        "nickname": str(username),
        "os": "AND",
        "deviceuid": "e32c837189aee948",
        "devicepushuid": "*dcxd1GSwQHasyTdA_0bkBi:APA91bGFdGbZhXTnfI-bceJS9_ysIUPuX7czkGZ5KZ0i67QO29Lfv-9KjPue_FOQyJcHXi1lNWDPXdh3Ri4jp2zhsnOEqPeCe1Mg3SWaAZUMGhk2WFenMhg",
        "osversion": "and_13.0.0",
        "id": "2067594203"
    }

    try:
        ws = create_connection("wss://51.79.208.190/Auth", sslopt={"cert_reqs": CERT_NONE})
        ws.send(json.dumps(data0))
        result = ws.recv()

        if isinstance(result, str):
            result = result.encode()
        decoded_data = decompress(result).decode('utf-8')

        if '"comment":"Exists"' in decoded_data:
            failed += 1
        elif '"status":"Success"' in decoded_data:
            success += 1
            account = f"{username}|aa8dq"
            accounts.append(account)
            with open('@AA8DQ.txt', 'a') as f:
                f.write(f"{account} | TG : @sandaveX\n")
            send_telegram_message(f"✅️ حساب ناجح : @AA8DQ {account}")
        elif '"comment":"Retry"' in decoded_data:
            retry += 1
        processed += 1

    except Exception as e:
        retry += 1
        processed += 1


def main():
    global processed
    mode = choose_mode()
    user_input = None
    if mode == 3:
        while True:
            user_input = input("\033[0;34m\033[1;47m أدخل أول خمسة احرف ( من a... الى z):\033[0m ")
            if len(user_input) == 5 and user_input.islower() and user_input[0].isalpha():
                break
            else:
                print("\033[0;37m\033[1;41m⚠️غير صحيح ! لا تنقص حرف او تزود حرف حصرا خمسة احرف  ولا تبدأ برقم او حرف كبير \033[0m")
    
    speed = 1
    if mode == 1:
        speed = choose_speed()

    executor = ThreadPoolExecutor(max_workers=1000 if mode == 2 else 200)
    while True:  # يستمر في العمل حتى يتم إيقافه يدويًا
        executor.submit(work, user_input=user_input, mode=mode)
        os.system('cls' if os.name == 'nt' else 'clear')
        progress = processed  # عرض عدد الحسابات التي تم معالجتها
        completed_length = (processed % 50)
        remaining_length = 50 - completed_length

        bar = f"{G}{'▓' * completed_length}{R}{'▒' * remaining_length}{reset}"
        print(f"\033[0;37m\033[1;42mصحيح✅️:\033[0m {G}{success}{reset}, \033[0;37m\033[1;41mخطأ ❌️: \033[0m{R}{failed}{reset}, \033[0;37m\033[1;44m الفحص ♻️\033[0m {Y}{retry}{reset}\n")
        print(f"{bar} {processed} \033[0;37m\033[1;43m🔥تم فحصه\033[0m\n")
        print('\033[1;36m@AA8DQ | @sandaveX | @aayco\033[0m\n')
        
        for account in accounts:
            print(f"{G}{account}{reset}")

        time.sleep(0.1)

if __name__ == "__main__":
    main()