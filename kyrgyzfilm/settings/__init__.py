DEBUG = True

if DEBUG:
    from .production import *
else:
    try:
        from .production import *
    except:
        from .production import *
