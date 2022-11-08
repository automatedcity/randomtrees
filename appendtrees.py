import subprocess 
import sys 
import os




def func():
  for i in range(101):
    accumulator = i+1

   

    os.environ["count"] =  str(accumulator)



    env=os.environ


    output_file = 'alpha.txt'
    sys.stdout = open(output_file, 'a')




    subprocess.call(['python3', 'tree.py'], env=env,stdout=sys.stdout, stderr=subprocess.STDOUT)


 

 
func()