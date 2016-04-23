from __future__ import division
import sys, os, inspect


def hpcc_rf(parameter):
    from modify_ecl_file import modify_file
    from random import randint
    modify_file(parameter[0], parameter[1], parameter[2], parameter[3], parameter[4])

    from time import sleep
    sleep(1)
    print "# ",
    sys.stdout.flush()
    command = "ecl run ./Problems/RF/rf.ecl -I\"/home/vnair2/GIT/ecl-ml\" --target=thor"

    import subprocess
    DEVNULL = open(os.devnull, "wb")
    output = subprocess.check_output(command, shell=True)
    import pdb
    pdb.set_trace()
    result = output.split("\n")[3]
    import re
    res = re.search(r"_1>(.*)</Result_1>", result)
    return_value = int(res.group(1))
    return [return_value]

