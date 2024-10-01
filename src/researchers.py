from typing import Any
from PIL import Image
from PyPDF2 import PdfFileReader 
from os.path import  getsize, getctime, getmtime 
from time import ctime
import abc

class FileResearcher(abc.ABC):
    @abc.abstractmethod
    def get_extension_info(self, file) -> Any:
        pass

    @abc.abstractmethod
    def display_extension_info(self, extension_info) -> None:
        pass

    def display_file_info(self, file):
        print((f"Name:\t\t{file}\nSize:\t\t{getsize(file)}\nCreate\t\t{ctime(getctime(file))}\nLast edit:\t{ctime(getmtime(file))}\n"))
        extension_info = self.get_extension_info(file) 

        self.display_extension_info(extension_info)

        
class ImageResearcher(FileResearcher):
    def get_extension_info(self, file):
        image = Image.open(file)
        return (image.size)

    def display_extension_info(self, extension_info) -> None:
        width = extension_info[0]
        height = extension_info[1]

        print(f'Width: {width}')
        print(f'Height: {height}')

class PdfResearcher(FileResearcher):
    def get_extension_info(self, file):
        pdf = PdfFileReader(file) 
        num_pages = pdf.getNumPages()
        
        return (num_pages)
    def display_extension_info(self, extension_info) -> None:
        print(f'Pages count: {extension_info}')
