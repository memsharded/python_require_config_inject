import os
from conans import ConanFile, load


class PkgConan(ConanFile):
    name = "pkg"
    version = "0.1"
    options = {"hardware": "ANY"}
    settings = "os", "compiler", "build_type", "arch"

    def build(self):
        # The build can actually do stuff with it!
        # here we need self.options.hardware to be a full path
        self.output.info(load(str(self.options.hardware)))

    def package_id(self):
        # We make the package_id to depend only on the filename, no path
        # filename should be versioned
        filename = os.path.basename(str(self.options.hardware))
        self.info.options.hardware = filename
