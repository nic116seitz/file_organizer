import subprocess
import os

downloads_path = os.path.expanduser('~/Downloads/')
scan_downloads = subprocess.run(['ls', '-l', downloads_path], capture_output=True, text=True)
downloads_array = scan_downloads.stdout.splitlines()

for file in downloads_array:
    file = file[53:]
    print(file)
