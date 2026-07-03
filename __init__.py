__version__ = "0.1.0"
__author__ = "Lidhin Sanjai V"
__license__ = "Apache-2.0"

__copyright__ = "Copyright 2026 Lidhin Sanjai V"
__maintainer__ = "Lidhin Sanjai V"
__email__ = "lidhinoffc@gmail.com"
__status__ = "Production/Stable"

#----------------------


from . import image

from .image import (
    resize,
    crop,
    rotate,
    flip,
    blur,
    convert,
    thumbnail,
    Image
)

image = Image


#-------------------

from .image import Image
from .file import File

image = Image
file = File

#-------------------

from .image import Image
from .file import File
from .text import Text

image = Image
file = File
text = Text

#----------------------

from .image import Image
from .file import File
from .text import Text
from .core import log

image = Image
file = File
text = Text

#----------------------

from .image import Image
from .file import File
from .text import Text
from .ai import AI
from .core import log

image = Image
file = File
text = Text
ai = AI

#------------------------

from .image import Image
from .file import File
from .text import Text
from .ai import AI

from .core import (
    log,
    set_config,
    get_config,
    register,
    get_plugin,
    list_plugins
)

image = Image
file = File
text = Text
ai = AI

#-------------------------

from .image import Image
from .file import File
from .text import Text
from .ai import AI

from .core import log, set_config, get_config, register, get_plugin, list_plugins

image = Image
file = File
text = Text
ai = AI


#--------------------------

from .pdf import PDF

pdf = PDF

#--------------------------
from .audio import Audio

audio = Audio

#---------------------------
from .video import Video

video = Video

#--------------------------

from .web import Web

web = Web

#------------------------
from .data import Data

data = Data
#-----------------------
from .system import System

system = System
#-------------------------

from .ai import AI

ai = AI

#-------------------------
from .math import Math

math = Math
#----------------------------
__all__ = [
    "text",
    "math",
    "image",
    "pdf",
    "audio",
    "video",
    "web",
    "data",
    "file",
    "system",
    "ai",
]

#---------------------------------