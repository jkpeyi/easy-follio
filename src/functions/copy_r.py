import os
import shutil


def copy_r(dir: str, dst_dir:str = './public'):

    dir_contents = os.listdir(dir)
    

    for content in dir_contents:
        
        abs_path=os.path.join(dir,content)
        
        if os.path.isfile(abs_path):
            shutil.copy(abs_path, dst_dir)
        else:

            dst_dir = os.path.join(dst_dir, content)
            if not os.path.exists(dst_dir):
                os.mkdir(dst_dir)
            copy_r(abs_path, dst_dir)
        
    
    print (dir_contents)
    pass