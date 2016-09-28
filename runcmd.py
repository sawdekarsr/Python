import time, subprocess
from subprocess import Popen,PIPE
def runCmd(cmd, msg):
    output  = ""
    error   = ""
    retCode = 0
    print('TIMESTAMP : ' + time.strftime("%m_%d_%Y") +' at ' + time.strftime("%H:%M:%S"))
    print(msg)
    print('COMMAND : '+cmd)
    try:
        pObj = Popen(cmd, stdout=PIPE, stderr=subprocess.STDOUT, shell=True)
        (output) = pObj.communicate()
        print("{} {}".format(pObj.returncode, output))
    except subprocess.CalledProcessError as e:
        (retCode, output) = (e.returncode, e.output)
        error = e.output
    except:
        print "ERROR"
    finally:
        print(output[0])
        print('TIMESTAMP : ' + time.strftime("%m_%d_%Y") +' at ' + time.strftime("%H:%M:%S"))
        return (pObj.returncode, output[0])

cmd = "ls -l "
msg = "List files"
runCmd(cmd, msg)
