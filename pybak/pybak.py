#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jeremy
#
# Created:     14/03/2015
# Copyright:   (c) Jeremy 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import datetime
import os
import shutil
import yaml

#SOURCE_BACKUP_DIR = 'C:/Important Files/'
#TARGET_BACKUP_DIR_fmt = 'C:/Backups/md_backup_{0}'


def load_config():
    f = open('config/data.yaml','r')
    return f


def parse_config():
    data_file = load_config()
    data = yaml.load(data_file)
    return data

def get_backup_directory(target_dir, name):
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
    return target_dir.format(name, date)

def copy_files_to(srcdir, dstdir):
    for file in os.listdir(srcdir):
        file_path = os.path.join(srcdir, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dstdir)

def copy_files(task):
    copy_files_to(task['source'], task['target'])


def perform_backup(task):
    target_dir = get_backup_directory(task['target'], task['name'])
    os.makedirs(target_dir)
    task['target'] = target_dir
    copy_files(task)

def job_runner(task):
    base_target = task['target']
    current_job = {'target': task['target']}
    for job in task['jobs']:
        current_job['name'] = job[0]
        current_job['source'] = job[1]
        perform_backup(current_job)
        current_job['target'] = base_target

def main():
    task = parse_config()
    job_runner(task)


if __name__ == '__main__':
    main()