Hii first python project for github kinda nervous

this currently ONLY works for caelestia shell, i am planning on making it work with swww and hyprpaper sometime (maybe)
currently this is not designed for use for anyone but me as the files are in my directory 
but if you want to use it for some reason heres how:
1. obv download te file and open it
2. copy your current config from cava and copy paste it into 3 (or more if u want to) folders in /home/yourname/cava-configs/
3. for each wallpaper youre going to use make one folder in cava-configs (ex /cava-configs/example1/) and put your config file youre going to use into it
4. edit the source_eva, yk and uhh to match your source (like source_wallpaper1 = "/home/myname/cava-configs/wallpaper1/config)
5. dest needs to be changed to "/home/yourname/.config/cava/config"
6. BACKUP YOUR ORIGINAL CONFIG FILE INCASE YOU DID SOMETHING WRONG, THIS WILL DELETE IT
7. cava_path will be te same as dest (huh might need to make cava_path = dest)
8. i havent tested out anything other than caelestia with this so u can TRY but the output NEEDS TO BE THE EXACT DESTINATION OF YOUR CURRENT WALLPAPER
9. change the "if output == "/home/yourname/Pictures/Wallpapers/wallpaper.png" (change yourname and wallpaper.png to.. your name and wallpaper name)
10. edit shutil.copy to shutil.copy(source_{whatever you put as youre source_ var}, dest)
11. edit for all 3 if statements
12. cd into where you downloaded cava-cfg.py, do python3 cava-cfg.py in your terminal of choice and restart cava and see if it worked!

this is my first python project dont flame me for bad coding
