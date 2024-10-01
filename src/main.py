from analyzer import Analyzer
from finder import Finder
from researchers import PdfResearcher, ImageResearcher

class IndianaJones:

    def __init__(self, path):
            
        researchers = {
            '.pdf': PdfResearcher(),
            '.png': ImageResearcher(),
            '.jpg': ImageResearcher(),
            '.jpeg': ImageResearcher(),
        }

        self.path = path
        self.finder = Finder(path, researchers)
        self.analyzer = Analyzer(self.finder.find())

indiana = IndianaJones('your/path')
print(indiana.finder.find())
indiana.finder.save_search_results('path/to/csv_results/file.csv')
