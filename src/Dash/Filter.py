from Board import Board

class Filter(Board):
     # Class Deals with Filtering the dataframe
        
    query = param.String(default="", doc="Query")                        # param that takes filter to be applied to the column selected
    add_filter = param.Action(lambda x: x.param.trigger('add_filter'))   # param that triggers add_query function

    _filters = {}                                                        # dict that stores all the queries

    
    # Function that adds the name of column as key to _filters dict every time a new column in selected
    @param.depends('select_column')                                      
    def new_query(self):
        self.query = ""
        if self.select_column not in self._filters.keys():
            self._filters[self.select_column] = []
    
    # adds the query string used to filter the selected column to _filters dict 
    @param.depends('add_filter')
    def add_query(self):
        if self.select_column not in self._filters.keys():
            self._filters[self.select_column] = []                          # initializes empty list to house the queries for the column selected 
        if self.select_column in self._filters.keys():                       
            if self.query not in self._filters[self.select_column]:         # if the enetered query of filter is not in list of queries for the selected column    
                self._filters[self.select_column].append(self.query)        # appends it to the list of queries
        if self.select_column in self._filters.keys() and self.query=="":   # if you select a column with the keu already in the filters dict and add a null string 
            self._filters[self.select_column] = []                          # clears the list of queries for the slected column