
class q:
    #1:issue 2:pr
    type=1
    closed=True
    repo=''
    def __init__(self,types=1,closed=True,repo=''):
        self.type=types
        self.closed=closed
        self.repo=repo

    def generate_q(self):
        #q=is%3Apr+is%3Aclosed+sort%3Acomments-desc
        q=''
        curr_type=''
        curr_closed='open'
        if self.type==1:
            curr_type='issue'
        elif self.type==2:
            curr_type='pr'
        if self.closed:
            curr_closed='closed'

        if self.repo!='':
            q='repo:'+self.repo+'+'+'is%3A'+curr_type+'+'+'is%3A'+curr_closed+'+sort%3Acreated-asc'

        return q

