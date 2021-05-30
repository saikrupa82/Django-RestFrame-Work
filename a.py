import random,string
for _ in range(100):
    try:
        with open('data.csv','r+') as fp:
            if not fp.read():
                fp.write('Name Numbers\n')
        with open('data.csv','a+') as fp:
            for j in fp.read():
                print(fp.read())
            n=''
            s=''
            for i in range(10):
                n+=str(random.randint(0,9))
                s+=''.join(random.choice(string.ascii_lowercase))
            fp.write('%s %s\n'%(n,s))
    except:
        with open('data.csv','a+') as fp:
            for j in fp.read():
                print(fp.read())
            n=''
            s=''
            for i in range(10):
                n+=str(random.randint(0,9))
                s+=''.join(random.choice(string.ascii_lowercase))
            fp.write('%s %s\n'%(n,s))