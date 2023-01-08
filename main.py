import shutil, os, time

your_source_folder = sf = 'D:/trial/fol1'
your_master_destination_folder = mdf = 'D:/trial/fol2'


def main():
    while True:
        for filename in os.listdir(sf):
            if filename.__contains__('#'):
                parser(filename)
        time.sleep(5)

def parser(fn):
    index = fn.find('#')
    final = fn.find('.')
    new_folder_name = fn[index+1:final]
    file_copy(fn,new_folder_name)

def file_copy(fn,new_folder_name):
    if new_folder_name in os.listdir(mdf):
        shutil.copy( (f'{sf}/' + fn), f'{mdf}/{new_folder_name}')
    else:
        os.mkdir(f'{mdf}/{new_folder_name}')
        shutil.copy( (f'{sf}/' + fn), f'{mdf}/{new_folder_name}')

main()