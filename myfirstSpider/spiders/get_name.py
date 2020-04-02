
import re
from myfirstSpider.spiders.q_constructor import q
from myfirstSpider.spiders.url_constructor import github_search_url
from myfirstSpider.spiders.util import read_to_list
if __name__ == '__main__':

    test_url='https://api.github.com/search/issues?q=repo:google/guava+is%3Apr+is%3Aclosed+sort%3Acreated-asc\n'
    pattern='(?<=issues\?q\=repo\:)[a-z]*/'
    pattern1='[^/]*(?=\+is\%3Apr)'

    a=re.search(pattern1,test_url)

    if a==None:
        print("none")
    else:
        print(a.group())

