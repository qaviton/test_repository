from qaviton import crosstest
from tests.config.private import hub
from tests.config import url


sessionTimeout = 60
screenResolution = "1000x860x24"

platforms = crosstest.Platforms()
platforms.web.command_executor = hub


# add chrome browser support
platforms.web({
    'browserName': "chrome",
    'version': "68",
    'platform': "ANY",
    'app': url.home,
    'screenResolution': screenResolution,
    'sessionTimeout': sessionTimeout,
    'enableVNC': True,
    'enableVideo': True,
    'name': "{}",
    'videoName': "{}.mp4",
    'logName': "{}.log"})
