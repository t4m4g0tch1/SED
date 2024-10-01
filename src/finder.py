import os 
from os.path import join, getsize, getctime, getmtime, splitext
import pandas as pd
from time import ctime
from time import localtime, strftime
from researchers import PdfResearcher, ImageResearcher

class Finder:
    def __init__(self, path, researchers):
        self.path = path
        self.researchers = researchers
    def __get_files(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                extension = splitext(file)[1].lower()
                yield (join(root,file), file, extension)

    def find(self):
        table_results = pd.DataFrame({'name':[], 'size(bytes)':[], 'extension':[], 'create_time':[], 'last_edit_time':[], 'extension_info': []})
        
        for file_info in self.__get_files():
            file_path, file_name, file_extantion = file_info
            researcher = self.researchers.get(file_extantion)
            if researcher:
                extension_info = researcher.get_extension_info(file_path)
            else:
                extension_info = '-'
            table_results = table_results._append({
                                                   'name': file_name,
                                                   'size(bytes)': getsize(file_path),
                                                   'extension': file_extantion,
                                                   'create_time':ctime(getctime(file_path)),
                                                   'last_edit_time':ctime(getmtime(file_path)),
                                                   'extension_info': extension_info},
                                                   ignore_index=True)
        
        return table_results

    def save_search_results(self, path):
        self.find().to_csv(f'{path}/search_results {strftime("%Y-%m-%d %H:%M:%S", localtime())}.csv')

