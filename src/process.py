import sys
import os
import signal
import subprocess

from time import sleep
from update import download_release, replace_exe

version, parent_pid = sys.argv[1], int(sys.argv[2])
# sleep(20)
download_release(version)
os.kill(parent_pid, signal.SIGTERM)
# sleep(10)
while (True):
  try:
    replace_exe()
    break
  except: pass

subprocess.Popen([".\\risi.exe"])

