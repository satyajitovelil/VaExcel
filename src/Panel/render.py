from .Filter import Filter


class Render(Filter):
    
    def __init__(self):
        ''' Initializes Filter Module'''
        self.filt = Filter()

    def render(self):
        ''' Renders the final Panel App
            Args: (None)
            Returns: Panel Object or App that can be served using a wsgi server
        '''
        render = pn.Row(pn.Column(self.filt.load, 
                                  self.filt.param.page, 
                                  self.filt.pagination,
                                ),
                 pn.Column(self.filt.build_query_df,
                           self.filt.query_menu,
                           self.filt.param.apply,
                           self.filt.apply_query,
                           self.filt.refresh_frame, 
                           self.filt.show_frame
                        )
                )
        return render