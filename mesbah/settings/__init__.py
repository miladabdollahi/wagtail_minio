"""
try to activate local settings. if it failed, we
load the production environment.
"""


try:
    from mesbah.settings.local import *
except ImportError:
    from mesbah.settings.production import *
