import os
import sys

def get_cwd():
    dll_folder = os.getcwd()
    # dll_folder = os.path.dirname(os.path.realpath(sys.argv[0]))
    dll_folder = dll_folder + '\\Runtime'
    dll_env = ';{}'.format(dll_folder)
    # print('dll_env',dll_env)
    os.environ['path'] += dll_env
    return dll_folder

def get_model_path():
    model_folder = os.getcwd()
    model_folder = model_folder + '\\net_file\\model_data'
    return model_folder

def get_save_path():
    pic_folder = os.getcwd()
    pic_folder = pic_folder + '\\SAVE_PICS'
    if not os.path.exists(pic_folder):
        os.mkdir(pic_folder)
    return pic_folder

def get_save_excel():
    excel_folder = os.getcwd()
    excel_folder = excel_folder + '\\EXCEL'
    if not os.path.exists(excel_folder):
        os.mkdir(excel_folder)
    return excel_folder

