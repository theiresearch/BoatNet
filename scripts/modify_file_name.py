#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os

home_folder = "/Users/realgjl/Desktop/BENV0096/3b_Sharpened_Loreto/2019/"
folder = os.listdir(home_folder)
os.chdir(home_folder)

for file in folder:
	if file.endswith('jpg') or file.endswith('txt'): # check the extension of a file
		print(file)
		if file[-6] =='_':
			print('yes')
			first_half = file[:-5]
			print(first_half)
			second_half = file[-5:]
			print(second_half)
			new_name = first_half + '0' + second_half
			os.rename(file, new_name)
			print("work!")
			