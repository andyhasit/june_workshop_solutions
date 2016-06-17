"""
Script for creating past dated git commits. For the github green dots.

Usage:
    
    >>> cheat 27/2 "my commit message"
    
    will trigger:
        
    >>>git commit -m "my commit message"
    >>>git commit --amend --no-edit --date="Wed 27 Feb 21:56:23 2016"
    
"""

import sys, datetime
from my_functions import *

def commit(commit_message):
    """
    Will send:
    git commit -m "your message"
    """
    cmd_text = build_git_commit_cmd(commit_message)
    return execute_cmd(cmd_text)
   
def amend(date_str):
    """
    Will send:
        git commit --amend --no-edit --date="Wed 03 Feb 21:56:23 2016"
    """
    now = datetime.datetime.now()
    day, month, year = split_date_string(date_str) 
    year = patch_year_if_in_yy_fomrat(year)

    
    #creating date object
    #exectuing command
    return execute_cmd(cmd)
    

commit_message = sys.argv[2]
date_str = sys.argv[1]

commit_succeded = call_commit_command(message)
if commit_succeded:
    call_amend_command(date_str)
else:
    print 'Commit failed'
    
    

if commit(sys.argv[2]) == 0:
    amend(sys.argv[1))
else:
    print 'Commit failed'


"""



['C:\\mine\\cmd\\cheat.py', '27/2', 'hello']


def execute_command(cmd_text):
    result = subprocess.call(cmd)
    return result == 0

def build_commit_command(commit_message):
    return 'git commit -m "{0}"'.format(commit_message) 


"""

