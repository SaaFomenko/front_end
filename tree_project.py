#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python 2.7.12
This script for fast creat dirs project front-end
"""

import os

"""
Define dirs, keys dictonary top dirs project, values subdirs.
If dir not contein subdirs, value = 0
ok flag for accept user
"""

ok = 'y'
dirs = {"app": ['css', 'fronts', 'libs', 'img', 'js', 'sass'],
        "dist": 0}


def make_dir(new_dir):
    """TODO: Docstring for make_dir. Make only dir top level.
    :returns: TODO creat top level dir.

    """
    try:
        os.mkdir(new_dir)
    except OSError:
        print('Create dir ' + new_dir + 'do NOT possible')
    else:
        print('Create dir ' + new_dir + 'do possible')


def make_dirs(new_dir):
    """TODO: Docstring for make_dirs. Create all dir in way.
    :returns: TODO

    """
    try:
        os.makedirs(new_dir)
    except OSError:
        print('Create dirs ' + new_dir + ' do NOT possible')
    else:
        print('Create dirs ' + new_dir + ' do possible')


def creat_dirs(dirs):
    """TODO: Docstring for creat_dirs.

    :dirs: TODO Dictionary with dirs name
    :returns: TODO make dirs for project

    """
    path = ''
    path = os.getcwd()
    current_dir = 'Current directory: ' + path + ' . '
    x = input(current_dir + 'You want create dirs project where?(y/n): ')
    if x == ok:
        for k, v in dirs.items():
            if v == 0:
                new_dir = path + '/' + k
                make_dir(new_dir)
            else:
                for i in v:
                    new_dir = path + '/' + k + '/' + i
                    make_dirs(new_dir)


creat_dirs(dirs)
