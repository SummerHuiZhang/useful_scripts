import os
import sys
# usage: python delete_some_word.py *.txt word_to_delete
#temp_file=sys[1]
#word=sys[2]
with open('/home/timing/StarGAN_Norland/data/Norland/test/winter/test_winter.txt','r') as fpr:
	content=fpr.read()
content = content.replace('./','')
print(content)
with open('/home/timing/StarGAN_Norland/data/Norland/test/winter/test_winter.txt','w') as fpw:
	fpw.write(content)

