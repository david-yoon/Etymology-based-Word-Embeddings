#-*- coding: utf-8 -*-
'''
date  : 2017
author: dato
where : SNU milab
what  : utils
'''

import os

def create_dir(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
        
        
