import os

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Cmd failed: {}".format(cmd))


cwd = os.getcwd()
run("conan create pkg -o pkg:hardware={}/myhw/hw1_v1.0".format(cwd))
run("conan create pkg -o pkg:hardware={}/myhw/hw1_v1.1".format(cwd))
run("conan create pkg -o pkg:hardware={}/myhw/hw2_v1.0".format(cwd))
run("conan search pkg/0.1@")

# They can be installed with just the name, if don't need to build
run("conan install pkg/0.1@ -o pkg:hardware=hw2_v1.0")