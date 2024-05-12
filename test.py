import subprocess
import os
from time import sleep

from src.update import get_latest_version_num
from src.version import is_uptodate
from src.path import resource_path

pid = str(os.getpid())
latest = get_latest_version_num()
if is_uptodate(latest):
  subprocess.Popen([resource_path("dist\\updater.exe"), latest, pid])

sleep(30)
print("failed")
