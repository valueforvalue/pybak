#-------------------------------------------------------------------------------
# Name:        pybak.py
# Purpose:     Create a backup of files contained in one or more directories.
#
# Author:      Jeremy Morris
#
# Created:     14/03/2015
# Copyright:   (c) Jeremy 2015
# License:     MIT
#-------------------------------------------------------------------------------

import datetime
import os
import shutil
import errno
import yaml

def parse_config():
    #This path will need to be edited depening on how you run this script.
    with open('config\data.yaml') as f:
        return  yaml.load(f)
    
def get_backup_directory(target_dir, name):
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
    return target_dir.format(name, date)

def copy_files_to(task): #EDIT this to include ignore_patterns.
    try:
        shutil.copytree(task['source'], task['target'])
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(task['source'], task['target'])
        else:
            print('Directory not copied. Error: %s' % e)

def perform_backup(task):
    task['target'] = get_backup_directory(task['base_backup_dir'], task['name'])
    copy_files_to(task)

def job_runner(task):
    current_job = {'base_backup_dir' : task['base_backup_dir']}
    for job in task['jobs']:
        current_job['name'] = job[0]
        current_job['source'] = job[1]
        perform_backup(current_job)

def main():
    job_runner(parse_config())
    

if __name__ == '__main__':
    main()