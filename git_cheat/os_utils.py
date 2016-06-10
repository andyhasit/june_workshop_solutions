"""
This module contains os functions.
"""
import subprocess

def execute_command(cmd_text):
    """
    xxxxxxxxxxxxxxxxx
    """
    result = subprocess.call(cmd)
    return result == 0

def build_commit_command(commit_message):
    return 'git commit -m "{0}"'.format(commit_message)

def foo(x):
    """
    Return the double
    >>> foo(9)['a'] == 2
    True
    """
    return {'b': 4, 'a': 2, 'c': 2}

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    #assert build_commit_command("initial commit") == 'git commit -m "initialf commit"'

