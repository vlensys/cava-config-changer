import subprocess
import shutil
import os
import json
import sys 

config_path = "config.json"

if not os.path.exists(config_path):
    home_dir = input("home directory please! (be awear to not add a / at the end as it will break everything), the cava-config folder will be created there\n> ")
    wallpaper_dir = input("where is your wallpapers folder? ex: /Pictures/Wallpapers (do NOT add a / at the end)\n> ")
    rl_wallpaper = f"{home_dir}{wallpaper_dir}"
    makedr = f"mkdir {home_dir}/cava-configs"
    os.system(makedr)
    wallpaper1_name = input("enter your first wallpaper's name (this MUST match the exact name of your wallpaper and the file extension, keep this in mind for all 3)\n> ")
    wallpaper2_name = input("enter your second wallpaper's name\n> ")
    wallpaper3_name = input("enter your third wallpaper's name\n> ")
    mkdir1 = f"mkdir {home_dir}/cava-configs/{wallpaper1_name}"
    mkdir2 = f"mkdir {home_dir}/cava-configs/{wallpaper2_name}"
    mkdir3 = f"mkdir {home_dir}/cava-configs/{wallpaper3_name}"
    os.system(mkdir1)
    os.system(mkdir2)
    os.system(mkdir3)

    config = {"home_dir": home_dir,
              "wallpaper1": wallpaper1_name,
              "wallpaper2": wallpaper2_name,
              "wallpaper3": wallpaper3_name,
              "wallpaperdir": rl_wallpaper,
              }
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)
        print(f"done! now go add your config file to each of the folders created in {home_dir}/cava-configs")
        sys.exit(1)
with open(config_path, "r") as f:
    config = json.load(f)

home_dir = config["home_dir"]
wallpaper1_name = config["wallpaper1"]
wallpaper2_name = config["wallpaper2"]
wallpaper3_name = config["wallpaper3"]
wallpaperdir = config["wallpaperdir"]

source_eva = f"{home_dir}/cava-configs/{wallpaper1_name}/config"
source_yk = f"{home_dir}/cava-configs/{wallpaper2_name}/config"
source_uhh = f"{home_dir}/cava-configs/{wallpaper3_name}/config"
dest = f"{home_dir}/.config/cava/config"

cava_path = f"{home_dir}/.config/cava/config"
cmd = "caelestia wallpaper"
output = subprocess.check_output(cmd, shell=True).decode().strip()

if output == f"{wallpaperdir}/{wallpaper1_name}":
    if os.path.exists(cava_path):
        os.remove(cava_path)
    shutil.copy(source_eva, dest)
    print(f"changing cava's config to {wallpaper1_name}'s worked!")

elif output == f"{wallpaperdir}/{wallpaper2_name}":
    if os.path.exists(cava_path):
        os.remove(cava_path)
    shutil.copy(source_yk, dest)
    print(f"changing cava's config to {wallpaper2_name}'s worked!")

elif output == f"{wallpaperdir}/{wallpaper3_name}":
    if os.path.exists(cava_path):
        os.remove(cava_path)
    shutil.copy(source_uhh, dest)
    print(f"changing cava's config to {wallpaper3_name}'s worked!")

print("exiting...")
