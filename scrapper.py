from telethon import TelegramClient
import re
import asyncio
r = '\033[91m'
w = '\033[97m'
api_id = ''  
api_hash = ''  
phone_number = ''  
channel_username = input('channel Username or Link :')
client = TelegramClient('session_name', api_id, api_hash)
async def main():
    await client.start()
    try:
        channel = await client.get_entity(channel_username)
        print(f'Exporting messages from channel: {channel.title}, ID: {channel.id}')  
        messages = await client.get_messages(channel, limit=None)  
        combo = f"{channel.title}.txt".replace('/', '_')  
        with open(combo, 'w', encoding='utf-8') as f:
            for message in messages:
                f.write(f'{message.date} - {message.sender_id}: {message.message}\n')
        print("Export completed!")
        try:
            with open(combo, 'r', encoding='utf-8') as file:
                input_text = file.read()
        except FileNotFoundError:
            print(f"File '{combo}' not found. Make sure the file exists and try again")
            exit()
        matches = re.findall(r'\b(\d{14,16})\|(\d{1,2})[\|/](\d{2,4})\|(\d{3,4})\b', input_text)
        cleaned_cc = []
        for match in matches:
            cc, mm, year, cvv = match
            mm = mm.zfill(2)  
            if len(year) == 2:
                year = '20' + year  
            cleaned_cc.append(f"{cc}|{mm}|{year}|{cvv}")
        output = f"{combo.split('.')[0]}_cleaned.txt"
        with open(output, 'w') as file:
            for cc in cleaned_cc:
                file.write(cc + '\n')
                print(r + cc + w)
        print(f"Cards are saved to '{output}'")
    except Exception as e:
        print(f"An error occurred: {e}")
asyncio.run(main())