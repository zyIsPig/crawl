from myfirstSpider.spiders import setting_self

def header_construct(n):

    head_temp=setting_self.header
    if n==1:
        head_temp['Authorization']=setting_self.token
    elif n==2:
        head_temp['Authorization'] = setting_self.token1
    return head_temp