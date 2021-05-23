import os
from conans import ConanFile, load
from conans.tools import save


class PkgConan(ConanFile):
    name = "pkg"
    version = "0.1"
    python_requires = "config/0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"config": "ANY"}

    def config_options(self):
        self.options.config = self.python_requires["config"].module.config

    def build(self):
        self.python_requires["config"].module.pre_build()
        hw = load(os.path.join(self.python_requires["config"].path, "hw"))
        save("hw.txt", hw)

    def package(self):
        self.copy("*")
