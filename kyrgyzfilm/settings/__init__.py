DEBUG = True

if DEBUG:
    from .dev import *
else:
    try:
        from .production import *
    except:
        from .production import *
