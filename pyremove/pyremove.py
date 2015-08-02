import os
os.system("sudo python setup.py install --record delete2.txt")
os.system("sudo python3 setup.py install --record delete3.txt")
os.system("cat delete2.txt | sudo xargs rm -rf")
os.system("cat delete3.txt | sudo xargs rm -rf")
os.system("rm -f delete2.txt delete3.txt")
