import vaex
import pandas as pd
import panel as pn
import math
import param


class Board(param.Parameterized):
    # Inital Class that houses the basic Dashboard params

    # param that takes file path
    file_path = param.String(default="", doc="Enter File Path")
    # param that triggers gen_df function
    load_file = param.Action(lambda x: x.param.trigger('load_file'))
    # param that takes page number
    page = param.Integer(1, bounds=(1, 30))
    # param that takes column to be selected for filtering
    select_column = param.Selector(default="--Select Column--", objects=['--Select Column--'])

   
    def __init__(self, **params):
        super(Board, self).__init__(**params)
        self.df = pd.DataFrame()               # initializes empty pandas dataframe 
        self.total_length = 0                  # total length of dataframe
        self.per_page = 30                     # records per page
        self.last_page = 30                    # last page  
        self.data = self.df                    # copy of dataframe subsequently used to store the filtered dataframe
        self.data_page = self.df               # initializes the variable subsequently used for current page of dataframe
        
        
    #Generate DataFrame    
    @param.depends('load_file')
    def gen_df(self):
        if self.file_path != "":
            self.df = vaex.open(str(self.file_path))                                     # loads the file as a vaex dataframe
            self.total_length = len(self.df)                                             # modifies total length variable
            self.last_page = math.ceil(len(self.df) / 30)                                # modifies last page variable based on file size
            self.param.page.bounds = (1, self.last_page)                                 # modifies upper bound of page param based on size of dataframe
            self.param.select_column.default = self.df.get_column_names()[0]             # modifies the default value of the select column param
            self.param.select_column.objects = list(self.df.get_column_names())          # modifies the objects listed as part of the select column param 
            self.data = self.df                                                          # replaces data variable with the newly loaded data 
            self.data_page = self.df.take(range(0, self.per_page)).to_pandas_df()        # slices the loaded dataframe and passes the scliced dataframe to data page variable

    
    # following function is triggered on page change
    @param.depends('page')
    def paginate(self):
        if self.file_path != "":
            self.from_item = ((self.page) - 1) * 30                                             # calculates starting index for current page     
            self.to_item = (self.page * 30)                                                     # calculates ending index for current page 
            self.data_page = self.data.take(range(self.from_item, self.to_item)).to_pandas_df() # slices the datframe to get records for current page
            df_widget = pn.widgets.DataFrame(self.data_page, name= 'DataSlice', width=1200)     # feeds the sliced dataframe to dataframe widget
            return df_widget
    
    @param.depends('load_file')
    def view(self):
        return pn.Row(self.gen_df, self.paginate)    #renders generated df and calls the paginate function