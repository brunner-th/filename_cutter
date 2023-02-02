# -*- coding: utf-8 -*-

#-----------------------------------------------------------------
#
# name: thomas brunner
#
#-----------------------------------------------------------------

from os import rename, listdir

suffix_list = ["h5","xdmf"]
filenames_not_to_cut = ["pressure","velo"]

delimiter = " "

files = listdir()
print("the files in this directory are:")
print(files)
print("\n")
for file in files:
    name, suffix = file.split(".")
    state_suf = False
    state_name = True
    for suf in suffix_list:
        if suf == suffix:
            state_suf = True
            
    if state_suf == True:
        
        for filename in filenames_not_to_cut:
            if filename != name and state_name == True:
                state_name = True
            else:
                state_name = False
                
        if state_name == True:
            var = name.split(delimiter)[0]
            new_name = var+"."+suffix
            rename(file, new_name)
            print("changed "+file+" to "+new_name)
        else:
            print(file+" skipped (already renamed or wrong name)")
    else:
        print(file+" skipped (wrong extension)")





