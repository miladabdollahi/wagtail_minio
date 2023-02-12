"""
try to activate local settings. if it failed, we
load the production environment.
"""


try:
    from project_name.settings.local import *
except ImportError:
    from project_name.settings.production import *
