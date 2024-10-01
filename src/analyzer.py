class Analyzer:
    def __init__(self, table_results):
        self.table_results = table_results

    def get_top_largest(self):
        return self.table_results.sort_values(by='size(bytes)', ascending=False).head()
    
    def get_top_oldest(self):
        return self.table_results.sort_values(by='create_time', ascending=False)
