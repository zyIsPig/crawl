import json






if __name__ == '__main__':

    with open('/Users/gulu/myfirstSpider/github.json','r') as f:
        k=f.readline()
        k_f=json.loads(k)['items']
        print(k_f[2])
        k_f_f=k_f[2]
        print(k_f_f['url'])
