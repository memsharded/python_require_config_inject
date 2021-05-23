import os

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Cmd failed: {}".format(cmd))


# In team1 repo (separated f team2)
cwd = os.getcwd()
run("conan export team1_config")
run("conan create pkg")

# Now team2 changes the config python-require
run("conan export team2_config")
run("conan create pkg")

run("conan search pkg/0.1@")
