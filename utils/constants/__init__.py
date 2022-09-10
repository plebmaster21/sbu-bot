import os
import dotenv

dotenv.load_dotenv()

SBU_LOGO_URL = 'https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096'

# Pseudo constants
GUILD_ID = 0

BOT_OWNER_ROLE_ID = 0  # the bot administrator role, has access to load, unload commands
JR_MOD_ROLE_ID = 0
QOTD_ROLE_ID = 0

QOTD_CHANNEL_ID = 0
MOD_CHAT_ID = 0

TOTAL_MEMBER_COUNT_VC_ID = 0
MEMBER_COUNT_VC_IDS = []
SBU_BOT_LOGS_CHANNEL_ID = 0

# User constants for chat triggers
ADU_ID = 397389995113185293
FLOP_ID = 615987518890049555
PINGU_ID = 381494697073573899
NOOMI_ID = 566329261535920175
WINCHAE_ID = 797274543042986024
PLEB_ID = 519985798393626634
SKYE_ID = 681475158975971329
MEGA_ID = 675106662302089247
COCOMONKEY_ID = 283326249735028736


if os.getenv('MODE') == 'PRODUCTION':
    GUILD_ID = 764326796736856066
    BOT_OWNER_ROLE_ID = 1015989853202169877
    QOTD_CHANNEL_ID = 868630191080083476
    MEMBER_COUNT_VC_IDS = [945493379599446056, 945493468539654205, 945493492434604072, 945493508398153808,
                           945493526047776889, 945493540748791899, 945493556909473812, 945493573263040522]
    TOTAL_MEMBER_COUNT_VC_ID = 890288776302190602
    SBU_BOT_LOGS_CHANNEL_ID = 946591422616838264
    JR_MOD_ROLE_ID = 924332988743966751
    MOD_CHAT_ID = 802982854291488808
    QOTD_ROLE_ID = 868630686712614922

else:
    GUILD_ID = 1017925960177303612
    BOT_OWNER_ROLE_ID = 1017925960592531587
    QOTD_CHANNEL_ID = 1017925962194747402
    MEMBER_COUNT_VC_IDS = [1017925961406238728, 1017925961406238729, 1017925961603358890, 1017925961603358891,
                           1017925961603358892, 1017925961603358893, 1017925961603358894, 1017925961603358895]
    TOTAL_MEMBER_COUNT_VC_ID = 1017925961406238727
    SBU_BOT_LOGS_CHANNEL_ID = 1017925964690358399
    JR_MOD_ROLE_ID = 1017925960571568344
    MOD_CHAT_ID = 1017925964270932022
    QOTD_ROLE_ID = 1017925960223436836
