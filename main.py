from twitch_chat_irc import twitch_chat_irc
import pyautogui

username = '' # eggwick
oauth = '' # You can get it from: https://twitchapps.com/tmi/
connection = twitch_chat_irc.TwitchChatIRC(username, oauth)

def handle_message(message):
  sender = message['display-name']
  content = message['message'].lower().trim()
  keys = ["w", "a", "s", "d"]
  
  if content in keys:
    print(f"· {sender} pressed {content}")
    pyautogui.press(content)

connection.listen(username, on_message=handle_message)
