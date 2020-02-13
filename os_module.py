import os

#Executing a shell command
os.system()    

#Get the users environment 
os.environ()   

#Return the real group id of the current process.
os.getgid()       

#Return the current process’s user id.
os.getuid()    

#Returns the real process ID of the current process.
os.getpid()     

#Set the current numeric umask and return the previous umask.
os.umask(mask)   

#Return information identifying the current operating system.
os.uname()     

#Change the root directory of the current process to path.
os.chroot(path)   
 
# To get the system name; 
os.name()

# To get current working directory: 
os.getcwd()

# To change directory: 
os.chdir('/home/user/')

# To list all files & folders in current directory: 
os.listdir(os.getcwd())

# To make a directory:
os.mkdir('123')

# To make directories inside directory(structure of directories):
os.makedirs('1/2/3/4/5')

# To remove directory: 
os.rmdir('123') 

# To remove sructure of directories: 
os.removedirs('1/2/3/4/5')	
