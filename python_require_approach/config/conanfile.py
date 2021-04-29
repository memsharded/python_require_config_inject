from conans import ConanFile, CMake

def configuration():
    return "Hello"

class ConfigConan(ConanFile):
    name = "config"
    version = "0.1"
