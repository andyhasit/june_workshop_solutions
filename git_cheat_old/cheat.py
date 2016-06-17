"""
Script for creating past dated git commits. For the github green dots.

Usage:
    
    >>> cheat 27/2 "my commit message"
    
    will trigger:
        
    >>>git commit -m "my commit message"
    >>>git commit --amend --no-edit --date="Wed 27 Feb 21:56:23 2016"
"""

import sys, datetime
from os_utils import execute_command, build_commit_command

def commit(commit_message):
    """
    Will send:
    git commit -m "your message"
    """
    cmd_text = build_commit_command(commit_message)
    return execute_command(cmd_text)


#assert build_commit_command("initial commit") == 'git commit -m "initial commit"'

def amend(date_str):
    """
    Will send:
    git commit --amend --no-edit --date="Wed 03 Feb 21:56:23 2016"
    """    
    new_date = build_date_from_date_str(date_str)             
    cmd = build_ammend_command_text(new_date)
    return execute_command(cmd)

def format_git_date_string(date):
    return new_date_str = date.strftime('%a %d %b %H:%M:%S %Y')
    
def build_ammend_command_text(date):
    new_date_str = format_git_date_string(date)
    return 'git commit --amend --no-edit --date="{0}"'.format(new_date_str)
    
def build_date_from_date_str(date_str):
    now = datetime.datetime.now()
    date_elements = date_str.split('/')
    day = int(date_elements[0])
    month = int(date_elements[1])
    if len(date_elements) == 3:
        year = int(date_elements[2])
        if year < 100:
            year = year + 2000 
    else:
        year = now.year
    new_date = datetime.datetime(year, month, day, now.hour, now.minute, 
                now.second)
                
"""

message = sys.argv[2]
date_str = sys.argv[1]

commit_succeded = commit(message)
if commit_succeded:
    amend(date_str)
else:
    print 'Commit failed'


['C:\\mine\\cmd\\cheat.py', '27/2', 'hello']

"""

