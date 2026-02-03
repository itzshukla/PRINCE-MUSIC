from PRINCEMUSIC.core.bot import PRINCE
from PRINCEMUSIC.core.dir import dirr
from PRINCEMUSIC.core.git import git
from PRINCEMUSIC.core.userbot import Userbot
from PRINCEMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
