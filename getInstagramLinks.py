import re

def getInstagramLinks(biography):
    if not biography:
        return []
    return re.findall(r'(https?://\S+|www\.\S+|\S+\.\S+)', biography)