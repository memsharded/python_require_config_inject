from conans import ConanFile, CMake

config = "TEAM 2 CONFIG"

def pre_build():
    print("*"*50)
    print("******* TEAM 2 pre-build specifics")
    print("*"*50)

class ConfigConan(ConanFile):
    name = "config"
    version = "0.1"
    exports = "*"
