#!/usr/bin/env python3

import os
import shutil
import json
import sys
from pathlib import Path
import argparse

cfg_path = "config.json"

def getPaths():
    home_dir = input("whats your home directory (must be /home/yourname, starting with a / and not ending with a /)\n> ")
    wallpaper_phrase = input("where does your wallpaper directory exist? (ex /Pictures/Wallpapers)\n> ")
    wallpaper_dir = f"{home_dir}{wallpaper_phrase}"
    print(wallpaper_dir)
    config = {
        "home_path": home_dir,
        "wallpaper_path": wallpaper_dir,
    }
    with open(cfg_path, "w") as f:
        json.dump(config, f, indent=4)
        print("cfg saved to the same place this script is in")

if not Path(cfg_path).exists():
    getPaths()

with open(cfg_path) as f:
    config = json.load(f)

home_path = config["home_path"]
wallpaper_path = config["wallpaper_path"]

def getWalls(wallpaper_path):
    files = os.listdir(wallpaper_path)
    return files

def folderCreator(wallpaper_path):
    files = [f for f in os.listdir(wallpaper_path) if os.path.isfile(os.path.join(wallpaper_path, f))]
    base_folder = f"{home_path}/cava-configs"
    os.makedirs(base_folder, exist_ok=True)
    for file_name in files:
        folder_path = os.path.join(base_folder, file_name)
        config_path = os.path.join(folder_path, 'config')
        if os.path.exists(config_path):
            continue
        os.makedirs(folder_path, exist_ok=True)
        with open(config_path, 'w') as config_file:
            config_file.write('# config!')
        print(f"creating folder + cfg for {file_name} worked")

def Maincava():
    current_wallpaper = os.popen("caelestia wallpaper").read().strip()
    wallpaper_file = os.path.basename(current_wallpaper)
    config_source = os.path.join(home_path, 'cava-configs', wallpaper_file, 'config')
    config_target_dir = os.path.join(home_path, '.config', 'cava')
    config_target_file = os.path.join(config_target_dir, 'config')
    if not os.path.exists(config_source):
        print(f"conig file not found for {wallpaper_file} (did u idk delete it?)")
        return
    if os.path.exists(config_target_file):
        os.remove(config_target_file)
    os.makedirs(config_target_dir, exist_ok=True)
    shutil.copy(config_source, config_target_file)
    print(f"{wallpaper_file} applied!")

def main():
    parser = argparse.ArgumentParser(description="wallpaper config manager")
    parser.add_argument('-r', '--refresh', action='store_true', help='refresh and make folders')
    args = parser.parse_args()
    if args.refresh:
        folderCreator(wallpaper_path)
    else:
        Maincava()

if __name__ == "__main__":
    main()

