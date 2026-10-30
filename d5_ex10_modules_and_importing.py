"""
import module

import module as alias

from module import symbol

from module import symbol as alias

from module import symbol1, symbol2

from module import *
"""

import os.path
import os.path as p
from os.path import join
from os.path import join as j
from os.path import join as j, abspath as absp

from os.path import *


print("»»»» __name__", __name__)

import mymodule
import mypackage
