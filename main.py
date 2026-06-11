import subprocess
import os

downloads_path = os.path.expanduser('~/Documents/Coding')
scan_downloads = subprocess.run(['ls', downloads_path], capture_output=True, text=True)
downloads_array = scan_downloads.stdout.splitlines()

for file in downloads_array:
    print(file)
