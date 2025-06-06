class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7657218453"
    sudo_users = ["7657218453", "7135097212", "6957310269"]
    GROUP_ID = "-1002746226173"
    TOKEN = "7517205575:AAHJgmhzzI0sRy5RDddvcuihdLaSwmEa-6U"
    mongo_url = "mongodb+srv://chffdgf0:olpYdyMsXzEGXqS5@cluster0.ivpoxxi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://envs.sh/gOG.jpg", "https://envs.sh/gOK.jpg", "https://envs.sh/gOz.jpg", "https://envs.sh/gO3.jpg"]
    SUPPORT_CHAT = "SandVillage"
    UPDATE_CHAT = "lustxUpdate"
    BOT_USERNAME = "lustXcatcherrobot"
    CHARA_CHANNEL_ID = "-1002592320932"
    api_id = "20457610"
    api_hash = "b7de0dfecd19375d3f84dbedaeb92537"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
