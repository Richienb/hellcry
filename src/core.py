"""
The main core file
"""
import quilt_lang as _

try:
    from fabulous import image
    print(image.Image(_.absolutepath("../assets/banner-background.png")))
except ModuleNotFoundError:
    print("HellCry")

print("Loading...")
temp_dir = _.tempdir()

import game
