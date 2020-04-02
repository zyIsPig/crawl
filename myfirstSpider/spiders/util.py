import re
def read_to_list(path,sta,num):
    ans=[]
    cnt=0
    with open(path,'r') as f:
        for s in f.readlines():
            cnt+=1
            if cnt>=sta:

                ans.append(s)
            if(cnt==num):
                break

    return ans

def phase_dir(name):

    #xxxx/xxxx/n
    partten1='^[^/]*'
    partten2='[^/]*$'

    fir_name=re.search(partten1,name)
    # print(fir_name.group())
    sec_name=re.search(partten2,name)
    # print(sec_name.group())
    return fir_name.group(),sec_name.group()[:-1]

if __name__ == '__main__':


    a,b=phase_dir('aaaassss/klklklk\n')
    print(b)
    print(a)



