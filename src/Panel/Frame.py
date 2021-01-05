class Frame(param.Parameterized):
    
    frame = param.DataFrame(pd.DataFrame())
    page = param.Integer(1)
    load = Loader()
    
    def __init__(self, **params):
        '''initializes the params associated with this class
        '''
        super(Frame, self).__init__(**params)
        self.per_page = 30

    @param.depends('load.load_file')
    def pagination(self):
        '''Modifies the bounds of page param once load file button is pressed
        '''
        self.last_page = math.ceil(self.load.data_length / 30)
        self.param.page.bounds = (1, self.last_page)

    @param.depends('load.load_file', 'page')
    def refresh_frame(self):
        '''Changes the current dataframe object being diplayed based on the page value
        '''
        if self.load.file_path != "":
            self.from_item = ((self.page) - 1) * self.per_page
            self.to_item = (self.page * self.per_page)
            self.frame = self.load.data[self.from_item: self.to_item].to_pandas_df()
#             self.frame = self.load.data.take(range(self.from_item, self.to_item)).to_pandas_df()

    @param.depends('frame')
    def show_frame(self):
        ''' Renders the Dataframe object as a Panel Widget. Depends on the current value of the frame.
        '''
        df_widget = pn.widgets.DataFrame(self.frame, name= 'DataSlice', width=1200)
        return df_widget