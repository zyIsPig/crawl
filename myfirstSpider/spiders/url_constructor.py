
class github_search_url:

    repo_search='https://api.github.com/search/'
    q=''
    sort=''
    page=1
    per_page=1
    language=''
    type=''


    def __init__(self,q,sort='stars',page=1,per_page=100,language='',type='repositories'):
        self.q=q
        self.sort=sort
        self.page=page
        self.per_page=per_page
        self.language=language
        self.type=type


    def construct(self):
        ans = self.repo_search + self.type + '?' + 'q=' + self.q
        if self.language!='':
            ans+='language:'+self.language

        if self.type=='repositories':
            ans+='+'+ '&sort='+self.sort+'&page='+str(self.page)+'&per_page='+str(self.per_page)

        return ans
