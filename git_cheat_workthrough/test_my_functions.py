from my_functions import *
import pytest

def test_build_git_commit_cmd():
    assert build_git_commit_cmd("initial commit") == 'git commit -m "initial commit"'

def test_split_date_string():
    assert split_date_string("11/05") == (11, 5, None)
    assert split_date_string("11/05/16") == (11, 5, 16)
    assert split_date_string("11/5/16") == (11, 5, 16)
    assert split_date_string("11/05/2016") == (11, 5, 2016)
    
        
@pytest.mark.xfail(raises=BaseException)
def test_split_date_string_raise_excdeption_on_bad_input(): 
    split_date_string("11/")