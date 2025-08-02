import subprocess
import shutil
import os

source_eva = "/home/valen/cava-configs/eva/config"
source_yk = "/home/valen/cava-configs/yk/config"
source_uhh = "/home/valen/cava-configs/uhh/config"
dest = "/home/valen/.config/cava/config"

cava_path = "/home/valen/.config/cava/config"
cmd = "caelestia wallpaper"
output = subprocess.check_output(cmd, shell=True).decode().strip()
print(output)

if output == "/home/valen/Pictures/Wallpapers/uhh.png":
    os.remove(cava_path)
    shutil.copy(source_uhh, dest)
    print("mightve worked idk")

if output == "/home/valen/Pictures/Wallpapers/EVA.png":
    os.remove(cava_path)
    shutil.copy(source_eva, dest)
    print("eva worked")

if output == "/home/valen/Pictures/Wallpapers/yk.png":
    os.remove(cava_path)
    shutil.copy(source_yk, dest)
    print("yk worked")
