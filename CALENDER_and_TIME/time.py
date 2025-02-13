import time
#localtime=time.asctime()#--> gives present time
localtime =time.asctime(time.localtime(time.time()))#-->almost same output
print(localtime)