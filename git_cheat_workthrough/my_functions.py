import subprocess
    
def build_git_commit_cmd(commit_message):
    return 'git commit -m "{0}"'.format(commit_message)
    
def execute_cmd(cmd_text):
    """
    Exectues cmd on shell, returns True is Successs else False.
    """
    return subprocess.call(cmd_text) == 0

def split_date_string(date_str):
    """
    Returns a tuple (day, month, year) based on string:
        dd/mm
        dd/mm/yy
        dd/mm/yyyy
    returns None for year if not provided.
    
    Raise Errors xy
    """
    date_elements = date_str.split('/')
    try:
        day = int(date_elements[0])
        month = int(date_elements[1])
        if len(date_elements) == 3:
            year = int(date_elements[2])
        else:
            year = None
        return day, month, year
    except (ValueError, IndexError):
        raise BaseException("Invalid date format provided, must be dd/mm or dd/mm/yy")
        
    #print ("Invalid date format provided, must be dd/mm or dd/mm/yy")
    #    
        
    
def patch_year_if_in_yy_fomrat(year):
    now = datetime.datetime.now()
    if year < 100:
        year = year + 2000 
    else:
        year = now.year
        
def buidl_git_ammend_cmd_text(date):
    
    

split_date_string("hello")
