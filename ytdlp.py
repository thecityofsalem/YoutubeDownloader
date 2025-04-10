import os
from yt_dlp import YoutubeDL
from os import system

def salemc(text):
    system(""); faded = ""
    red = 80
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

dota = '''
   ▄████████    ▄████████  ▄█          ▄████████   ▄▄▄▄███▄▄▄▄   
  ███    ███   ███    ███ ███         ███    ███ ▄██▀▀▀███▀▀▀██▄ 
  ███    █▀    ███    ███ ███         ███    █▀  ███   ███   ███ 
  ███          ███    ███ ███        ▄███▄▄▄     ███   ███   ███ 
▀███████████ ▀███████████ ███       ▀▀███▀▀▀     ███   ███   ███ 
         ███   ███    ███ ███         ███    █▄  ███   ███   ███ 
   ▄█    ███   ███    ███ ███▌    ▄   ███    ███ ███   ███   ███ 
 ▄████████▀    ███    █▀  █████▄▄██   ██████████  ▀█   ███   █▀  
                          ▀                                      
'''

def salemv(url):
    download_folder = os.path.join(os.getcwd(), "downloaded")
    os.makedirs(download_folder, exist_ok=True)
    
    options = {
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
    }
    
    with YoutubeDL(options) as ydl:
        try:
            ydl.download([url])
            print(f"\nDownloaded to: {download_folder}")
        except Exception as e:
            print(f"An error occurred: {e}")

def salemm():
    while True:
        print(salemc(dota))
        url = input("url = ").strip()
        
        if url.lower() == "q":
            print(salemc("Exiting..."))
            break

        if url:
            salemv(url)
        else:
            print(salemc("put a url."))

if __name__ == "__main__":
    salemm()
