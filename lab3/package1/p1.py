# Задание № 1
class Sum_sum:

    def __init__ (self):
        pass
        
    def Sum(row1):

        s = sum(row1)
        
        return s
    
# Задание № 2    
class Count_words:

    def __init__(self):
        pass

    def count(self, string):
        from collections import Counter
        import re
        # words = string.split()
        words = re.split(r'[ ,]+', string)
        c = Counter(words)
        return c

# Задание № 3    
class Parsing:
    
    def __init__(self, url_):
        import requests
        self.req = requests.get(url_)

    def get_text(self):
        from bs4 import BeautifulSoup
        code_from_the_page = BeautifulSoup(self.req.content, 'html.parser')
        return(code_from_the_page)
            