# import os
# from subprocess import call

# call('putty -ssh username@tsdb.eie.wits.ac.za -pw password -D 4242')
# ('python app.py')



# import os                                                                       
# from multiprocessing import Pool                                                
                                                                                
                                                                                
# processes = ('app.py', 'SSHTunnel.py')                                    
                                                  
                                                                                
# def run_process(process):                                                             
#     os.system('python {}'.format(process))                                       
                                                                                
                                                                                
# pool = Pool(processes=2)                                                        
# pool.map(run_process, processes)  
from threading import Thread
import os
from app import app
# from SSHTunnel import createTunnel

def appLaunch():
    app()
    

# def tunnel():
    # createTunnel()

Thread(target = appLaunch).start() 
# Thread(target = tunnel).start()