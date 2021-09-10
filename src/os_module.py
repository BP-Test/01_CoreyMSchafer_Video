import os
from datetime import datetime
#print(f'all modules:{dir(os)}')
print(f'Change Directory:"{os.chdir("../data")}"')
print(f'working_directory:"{os.getcwd()}"')
#os.makedirs('./abc/def/geh') #Creates directories
#os.rename('before_name','after_name')
print(os.stat(f"{os.listdir()[-1]}").st_size) # prints statistic information of the file
mod_time = os.stat(f"{os.listdir()[-1]}").st_mtime #modified time
print(datetime.fromtimestamp(mod_time)) # print modified time in readable format

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print(f'Current Path: {dirpath}')
#     print(f'Directories: {dirnames}')
#     print(f'Files: {filenames}')
#     print()
#os.path.join()
print(os.environ.get('HOME'))