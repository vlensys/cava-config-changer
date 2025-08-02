import subprocess
import shutil
import os
import json

config_path = "config.json"

if not os.path.exists(config_path):
    home_dir = input("homedir pls")
    config = {"home_dir": home_dir}
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)

with open(config_path, "r") as f:
    config = json.load(f)

home_dir = config["home_dir"]
print(home_dir)

source_eva = f"{home_dir}/cava-configs/eva/config"
source_yk = f"{home_dir}/cava-configs/yk/config"
source_uhh = f"{home_dir}/cava-configs/uhh/config"
dest = f"{home_dir}/.config/cava/config"

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
