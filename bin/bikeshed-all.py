#!/usr/bin/env python
import os.path

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)
for name in os.listdir('.'):
    path = os.path.join(root, name)
    if os.path.isdir(path):
        os.chdir(path)
        if os.path.isfile('Overview.bs') and not os.path.isfile('Overview.html'):
            print('Bikeshedding %s…' % name)
            os.system('bikeshed')
