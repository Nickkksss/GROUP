from platform import python_version
from pytgcalls import __version__ as pytgcalls
from git import Repo
from telethon import version as telethonver


repo = Repo()
branch = repo.active_branch.name


__Tgl__ = "10"
__Bln__ = "04"
__Thn__ = "2022"

__telethonver = f"{telethonver.__version__}"
__python_version__ = f"{python_version()}"
__license__ = "GNU Affero General Public License v3.0"
__author__ = "PandaX_UserBot <https://github.com/ilhammansiz/PandaX_Userbot>"
__copyright__ = "PandaX_UserBot Copyright (©) 2020 - 2021  " + __author__
pytgcallsver = f"{pytgcalls.__version__}"

bot = f"-0-g5e884ad"

__version__ = "UserbotVersion" + ":" + "@" + branch + bot + "|" + "Python" + __python_version__ + "|" + "Telethon" + __telethonver + "|" + "Pytgcalls" + pytgcallsver
