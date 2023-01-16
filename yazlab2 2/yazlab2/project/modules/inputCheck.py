

def isfloatAble(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
    
def isintegerAble(num):
    try:
        int(num)
        return True
    except ValueError:
        return False