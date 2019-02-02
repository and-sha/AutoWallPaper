#!/usr/bin/python3
from random import choice
from os import listdir, system
from os.path import isfile, join
import configparser


config = configparser.ConfigParser()
config_file = "/home/andysha/wp/wp.conf"
config.read(config_file)

DIR = config.get('config', 'directory')


cmd = "./xfcewphelper.sh"
onlyfiles = [f for f in listdir(DIR) if isfile(join(DIR, f))]
full_dir = []
for item in onlyfiles:
    full_dir.append(f"{DIR}/{item}")


paper = choice(full_dir)
execute = f"{cmd} {paper}"
system(execute)
