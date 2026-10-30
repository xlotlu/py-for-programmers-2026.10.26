from . import submodule

# ^^ acesta este singuru loc unde funcționează
#    căile relative. în interiorul unui package.

from .submodule import SUBVAR


__version__ = '1.2'
print("eu sunt corpul 'pachetului'")


print("» __name__", __name__)
