'''语法测试'''
import os

a={1:1,2:2}
b={21:1,2:2}
s=set()
for k in a.keys():
    for k1 in b.keys():
        if k==k1:
            s.add(k)
print(s)
print(list(s))

c={1:1,2:2,3:3}
d={2:3}
c[2]=d[2]
print(c)

print(os.path.exists(r'F:\bm_api\data\config_dat1a.py'))