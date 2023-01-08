import shutil, os, time

# while True:
#     for filename in os.listdir('D:/trial/fol1'):
#         if filename.endswith('.txt'):
#             shutil.move( ('D:/trial/fol1/' + filename), 'D:/trial/fol2')
#     time.sleep(6)

your_source_folder = sf = 'D:/trial/fol1'
your_master_destination_folder = mdf = 'D:/trial/fol2'



# while True:
#     for filename in os.listdir(sf):
#         # print(type(filename))
#         if filename.__contains__('#'):
#             index = filename.find('#')
#             final = filename.find('.')
#             new_folder_name = filename[index+1:final]
#             # print(new_folder_name)
#             shutil.copy( ('D:/trial/fol1/' + filename), f'D:/trial/fol2/{new_folder_name}')
#     time.sleep(5)

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