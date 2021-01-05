from Slicer import Slicer

Slicer = Slice()

svatdash = pn.Row(pn.Column(Slicer.param.file_path,
                            Slicer.param.load_file,
                            Slicer.param.download_file
                            ), 
                  Slicer.view,
                  pn.Column(Slicer.param.select_column,
                            Slicer.param.query,
                            Slicer.param.add_filter,
                            Slicer.param.query_string,
                            Slicer.param.apply_filter,
                            Slicer.param.page,
                            Slicer.new_query, Slicer.add_query, Slicer.create_query_st
                            )
                  )