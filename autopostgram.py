import sqlite3
import time
from telethon.sync import TelegramClient
from telethon.tl import types
from colorama import init, Fore, Back, Style

init(autoreset=True)

welcome_message = """
 █████╗ ██╗     ██╗ ██████╗███████╗    ██████╗ ██╗   ██╗"""
welcome_message1 ="""
██╔══██╗██║     ██║██╔════╝██╔════╝    ██╔══██╗╚██╗ ██╔╝
███████║██║     ██║██║     █████╗      ██████╔╝ ╚████╔╝ """
welcome_message2 ="""
██╔══██║██║     ██║██║     ██╔══╝      ██╔═══╝   ╚██╔╝  """
welcome_message3 ="""
██║  ██║███████╗██║╚██████╗███████╗    ██║        ██║   
╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝╚══════╝    ╚═╝        ╚═╝   """
print(Fore.RED + welcome_message,Fore.YELLOW + welcome_message1,Fore.WHITE + welcome_message2,Fore.BLUE + welcome_message3)
print("--------------------------------------------------------")
print("--------------------------------------------------------")
def main():
    print("1- send content to channel")
    print("2- we are in maintenance")

    secim = input("PLS CLICK NUMBER: ")
    if secim=='1':

        api_id = ''
        api_hash = ''

        channel_titles = [
            "VIXEN",
            "WEBCAM",
            "XVIDEOS",
            "XHAMSTER",
            "LEGALPORNO",
            "PORNHUBPREMIUM",
            "NAUGHTYAMERICA",
            "TIKTOK ONLYFANS",
            "HARDX",
            "FAKEHUB",
            "BRAZZERSPREMIUM",
            "ONLYFANS VIP",
            "BRATTYSIS",
            "ONLYFANS",
            "CUMSHOT",
            "ONLYFANS -1",
            "XVIDEOS -1",
            "BRAZZERSPREMIUM -1",
            "ONLYFANS VIP -1",
            "ONLYFANS VIP -2",
            "ONLYFANS VIP -3",
            "ONLYFANS VIP -4",
            "TIKTOK ONLYFANS -1",
            "BRAZZERSPREMIUM -2",
            "VIXEN -1",
            "WEBCAM -1",
            "XHAMSTER -1",
            "LEGALPORNO -1",
            "HARDX -1",
            "FAKEHUB -1",
            "BRATTYSIS -1",
            "CUMSHOT -1",
            "PORNO PREMIUM",
            "PORNO PREMIUM -2",
            "PORNO PREMIUM -3",
        ]
        channels_and_users = [
            {
                "channel_name_or_id": "Pr00n", #vixen
                "user_name_or_id": -1001864154860 
            },
            {
                "channel_name_or_id": "webcam_free", #webcam
                "user_name_or_id": -1001670459140
            },
            {
                "channel_name_or_id": "digitalplaygroundcom", #xvideos
                "user_name_or_id": -1001821276606
            },
            {
                "channel_name_or_id": "vixengirl", #xhamster
                "user_name_or_id": -1001849076145
            },
            {
                "channel_name_or_id": "legalporno_com", #legalporno
                "user_name_or_id": -1001952931841
            },
            {
                "channel_name_or_id": "pornhub_pr", #pornhubpre
                "user_name_or_id": -1001503163071
            },
            {
                "channel_name_or_id": "Naughty_America_premium", #naughtyamerica
                "user_name_or_id": -1001653585304
            },
            {
                "channel_name_or_id": "fapaton", #tiktok onlyfans
                "user_name_or_id": -1001964048982
            },
            {
                "channel_name_or_id": "hardx_dp", #hardx
                "user_name_or_id": -1001964255796
            },
            {
                "channel_name_or_id": "faketaxifree", #fakehub
                "user_name_or_id": -1001601379655
            },
            {
                "channel_name_or_id": "brazzers_prem1", #brazzerspre
                "user_name_or_id": -1001871287836
            },
            {
                "channel_name_or_id": "Oasis69", #brazzers girls onlyfans
                "user_name_or_id": -1001957208254
            },
            {
                "channel_name_or_id": "brattysist", #brattysis
                "user_name_or_id": -1001948886779
            },
            {
                "channel_name_or_id": -1001401786893, #modo incognito
                "user_name_or_id": -1001899054726 #onlyfans
            },
            {
                "channel_name_or_id": "bukkakecore", #cumshot
                "user_name_or_id": -1001957440366
            },
            {
                "channel_name_or_id": -1001155383280, #𝔸𝕕𝕦𝕝𝕥 𝕧𝕚𝕕𝕖𝕠 (ᴄʟɪᴄᴋ ꜰᴏʀ ᴍᴏʀᴇ) short video
                "user_name_or_id": -1001899054726 #onlyfans
            },
                {
                "channel_name_or_id": "XVideos365", #xvideos
                "user_name_or_id": -1001821276606
            },
            {
                "channel_name_or_id": "brazzers_premiummmmm", #BRAZZERS PREMIUM COLLECTION
                "user_name_or_id": -1001871287836
            },
            {
                "channel_name_or_id": -1001295174357, #morbo crudo
                "user_name_or_id": -1001957208254
            },
            {
                "channel_name_or_id": -1001250302760, #onlyfansvip
                "user_name_or_id": -1001957208254
            },
            {
                "channel_name_or_id": -1001378279199, #onlyfansgratis
                "user_name_or_id": -1001957208254
            },
            {
                "channel_name_or_id": -1001778908447, #poemasxxx
                "user_name_or_id": -1001957208254
            },
            {
                "channel_name_or_id": -1001465697081, #666K HOT
                "user_name_or_id": -1001964048982 #tiktok onlyfans
            },
            {
                "channel_name_or_id": "blacked_prem", #blacked
                "user_name_or_id": -1001871287836 #brazzerspremium
            },
            {
                "channel_name_or_id": -1001157686610, #cerocensuras
                "user_name_or_id": -1001864154860 #vixen
            },
            {
                "channel_name_or_id": -1001485432738, #agenteganso
                "user_name_or_id": -1001670459140 #webcam
            },
            {
                "channel_name_or_id": -1001665289142, #orgasmos 2023
                "user_name_or_id": -1001849076145 #xhamster
            },
            {
                "channel_name_or_id": -1001625319952, #tio roshi
                "user_name_or_id": -1001952931841 #legalporno
            },
            {
                "channel_name_or_id": -1001794863438, #oasis69
                "user_name_or_id": -1001964255796 #hardx
            },
            {
                "channel_name_or_id": -1001494435969, #porno tv
                "user_name_or_id": -1001601379655 #fakehub
            },
            {
                "channel_name_or_id": -1001486085838, #camaraoculta
                "user_name_or_id": -1001948886779 #brattysis
            },
            {
                "channel_name_or_id": -1001360555938, #pervesion
                "user_name_or_id": -1001957440366 #cumshot
            },
            {
                "channel_name_or_id": -1001178508591, #porno premium
                "user_name_or_id": -1001810680526 
            },
            {
                "channel_name_or_id": -1001180083777, #CALVO EXCLUSİVO
                "user_name_or_id": -1001810680526 
            },
            {
                "channel_name_or_id": -1001519641492, #TİOTED
                "user_name_or_id": -1001810680526 
            },

        ]

        database_file = 'barutlift.db'

        start_message_id = 1
        end_message_id = 10

        wait_minutes = 2  
        wait_seconds = wait_minutes * 60 

        with TelegramClient('session_name', api_id, api_hash) as client:
            conn = sqlite3.connect(database_file)
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS media (
                    id INTEGER PRIMARY KEY,
                    media_id TEXT UNIQUE,
                    date TEXT,
                    media_type TEXT
                )
            ''')
            conn.commit()

            for channel_title, item in zip(channel_titles, channels_and_users):
                channel_name_or_id = item["channel_name_or_id"]
                user_name_or_id = item["user_name_or_id"]

                channel_entity = client.get_entity(channel_name_or_id)
                user_entity = client.get_entity(user_name_or_id)

                messages = client.iter_messages(channel_entity, min_id=start_message_id, max_id=end_message_id)

                print(Fore.GREEN + f"{channel_title} started...")

                for message in messages:
                    if isinstance(message.media, types.MessageMediaDocument):
                        media = message.media.document
                        if 'video' in media.mime_type:
                            media_id = media.id
                            if not cursor.execute("SELECT * FROM media WHERE media_id=?", (media_id,)).fetchone():
                                client.send_file(user_entity, media, caption=None)
                                cursor.execute("INSERT INTO media (media_id, date, media_type) VALUES (?, ?, ?)", (media_id, message.date, media.mime_type))
                                conn.commit()
                        elif 'image' in media.mime_type:
                            media_id = media.id
                            if not cursor.execute("SELECT * FROM media WHERE media_id=?", (media_id,)).fetchone():
                                client.send_file(user_entity, media, caption=None)
                                cursor.execute("INSERT INTO media (media_id, date, media_type) VALUES (?, ?, ?)", (media_id, message.date, media.mime_type))
                                conn.commit()
                                
                print(Fore.GREEN + f"{channel_title} OK.")
                
                if channel_title != channel_titles[-1]:
                    print(Fore.GREEN + "moving to the next channel...")

                    for i in range(wait_seconds, 0, -1):
                        countdown_text = f"TIME: {i // 60} MINUTE {i % 60} SECOND"
                        print(Fore.GREEN + countdown_text, end='\r')
                        time.sleep(1) 
                    print() 
                    print("------------------------------")
        print(Fore.RED+"saved to database.")
        print(Fore.RED+"contents sent.")

    elif secim=='2':
        print("WTF...")

    else:
        print("What are u DOING MANN.")

if __name__ == "__main__":
    main()
