import vaex
import pandas as pd
import panel as pn
import math
import param
import os
import glob
import datetime

class Loader(param.Parameterized):
    
    '''Initilizes the elements required to create the load module
    '''

    file_path = param.String(default="", doc="Enter File Path")
    load_file = param.Action(lambda x: x.param.trigger('load_file'))
    
    
    def __init__(self, **params):
        super(Loader, self).__init__(**params)
        self.data = pd.DataFrame()
        self.data_length = len(self.data)
        self.data_columns = []
        
    @param.depends('load_file', watch=True)
    def load(self):
        '''function the gets triggered by the load_file param
        '''
        if self.file_path != "":
            self.data = vaex.open(str(self.file_path))
            self.data_length = len(self.data)
            self.data_columns = list(self.data.get_column_names())