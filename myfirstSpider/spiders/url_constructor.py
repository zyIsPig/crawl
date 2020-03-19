
class github_search_url:

    repo_search='https://api.github.com/search/repositories?'
    q=''
    sort=''
    page=1
    per_page=1
    language=''


    def __init__(self,q,sort='stars',page=1,per_page=3,language=''):
        self.q=q
        self.sort=sort
        self.page=page
        self.per_page=per_page
        self.language=language


    def construct(self):

        ans=self.repo_search+'q='+self.q+'+'+'language:'+self.language+'&sort='+self.sort+'&page='+str(self.page)+'&per_page='+str(self.per_page)

        return ans
