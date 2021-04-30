import os

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Cmd failed: {}".format(cmd))


cwd = os.getcwd()
run("conan export config")
run("conan create pkg".format(cwd))
