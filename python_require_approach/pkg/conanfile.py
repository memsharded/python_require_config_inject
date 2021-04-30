import os
from conans import ConanFile, load


class PkgConan(ConanFile):
    name = "pkg"
    version = "0.1"
    python_requires = "config/0.1"
    settings = "os", "compiler", "build_type", "arch"

