from conans import ConanFile, CMake


class ConfigConan(ConanFile):
    name = "config"
    version = "0.1"
    exports = "myhw/*"
