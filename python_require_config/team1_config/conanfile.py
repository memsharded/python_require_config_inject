from conans import ConanFile, CMake

config = "TEAM 1 CONFIG"

def pre_build():
    print("*"*50)
    print("******* TEAM 1 pre-build specifics")
    print("*"*50)

class ConfigConan(ConanFile):
    name = "config"
    version = "0.1"
    exports = "*"
