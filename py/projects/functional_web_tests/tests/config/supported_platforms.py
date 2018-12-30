from qaviton import crosstest
from tests.config.private import hub
#from tests.config.supported_platforms import sessionTimeout

app = 'https://www.google.com/'
screenResolution = "1000x860x24"


# create cross-platform testing object
platforms = crosstest.Platforms()
platforms.web.command_executor = hub

sessionTimeout = 600

# add chrome browser support
platforms.web({
    'browserName': "chrome",
    'version': "",
    'platform': "ANY",
    'app': app,
    'screenResolution': screenResolution,
    'sessionTimeout': sessionTimeout,
    'enableVNC': True,
    'enableVideo': True,
    'name': "{}",
    'videoName': "{}.mp4",
    'logName': "{}.log"})


