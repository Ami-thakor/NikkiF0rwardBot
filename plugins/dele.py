#!/usr/bin/env python3
# pylint: disable=missing-docstring,unused-import,invalid-name,wildcard-import,unused-wildcard-import,broad-exception-caught,bare-except,unused-argument



import pickle


async def msg_dict_func(msg_ids_dic,filename:str):
    file_path = f"{filename}-DELEMSGs.dat"
    with open(file_path, 'wb') as file:
        pickle.dump(msg_ids_dic, file)


async def showdata(filename:str):
    file_path = f"{filename}-DELEMSGs.dat"
    
    with open(file_path, 'rb+') as file:
        data = pickle.load(file)
        return data
