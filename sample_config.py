from os import environ

# To use manual values, change these
default_bot_token = "1746107359:AAHh21LvFhmkPwiyNeT8Tpsz7c_51zI0ocQ"
default_sudo_chat_id = -419748359
default_owner_id = 1723431231

# Don't change these value
bot_token = environ.get("BOT_TOKEN", default_bot_token)
sudo_chat_id = int(environ.get("SUDO_CHAT_ID", default_sudo_chat_id))
owner_id = int(environ.get("OWNER_ID", default_owner_id))
