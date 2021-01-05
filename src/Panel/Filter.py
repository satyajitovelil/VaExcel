import vaex
import pandas as pd
import panel as pn
import math
import param
import os
import glob
import datetime

from .Frame import Frame
from .utils import create_query_string, split_filter_part
from .utils import operators

class Filter(Frame):
    ''' Creates the elements required to filter the dataframe 
    '''

    query_df = param.DataFrame(pd.DataFrame())
    apply = param.Action(lambda x: x.param.trigger('apply'))
    _filters = []
    
    
    @param.depends('load.load_file')
    def build_query_df(self):
        ''' creates a dataframe that has a row to deal with all the with all the filters you pass 
            and column names equal to the file being loaded
        '''
        self.query_df = pd.DataFrame({k:'' for k in self.load.data_columns}, index=[0])
    
    @param.depends('load.load_file', 'query_df')
    def query_menu(self):
        '''loads the file as a dataframe
        '''
        return pn.widgets.DataFrame(self.query_df, width=1200)
    
    @param.depends('apply')
    def apply_query(self):
        '''Function to apply all the filters
           triggered by apply param which is a renderd as a button
        '''
        if self.load.file_path != "":
            for key, row_value in self.query_df.iteritems():
                qs = row_value[0]
                op, value = split_filter_part(qs)
                query_s = create_query_string(key, op, value)
                if query_s is not '':
                    self._filters.append(query_s)
            for f in list(set(self._filters)):         
                self.load.data = self.load.data[self.load.data[f]]
            self.refresh_frame()
            self.pagination()