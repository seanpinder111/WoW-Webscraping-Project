from os.path import isfile
from os import mkdir
from os import chdir
from os import getcwd
from os.path import exists

class_name = "Donkey"

# crate new directory
dir_path = "C:/Users/seanp/Documents/JavascriptProjects/WoW Talent Project/" + class_name + " Talents"
if not exists(dir_path):
    mkdir(dir_path)

# change working directory
chdir(dir_path)
