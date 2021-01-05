from Filter import Filter

class Slice(Filter):
    
    query_string = param.String(default="", doc="Query String")              # param that displays the consolidated string of queries applied to the dataframe
    apply_filter = param.Action(lambda x: x.param.trigger('apply_filter'))   # triggers the create_query_str function that also filters the dataframe
    download_file = param.Action(lambda x: x.param.trigger('download_file')) # download file button
    
    
    @param.depends('apply_filter')
    def create_query_st(self):
        qs = "".join(extract_val(self._filters))         # creates consolidates query string
        self.query_string = qs                           
        if qs != "":
            for i in extract_val(self._filters):         # iteratively applies each item from list of filters to slice the dataframe 
                self.data = self.data[self.data[i]]      
        else:
            self.data = self.df
            
    @param.depends('download_file')
    def export_data(self):
        self.data.export(f'data_.hdf5')