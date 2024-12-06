from cmapPy.pandasGEXpress.parse import parse
from cmapPy.pandasGEXpress.GCToo import GCToo

class gctx():
    def __init__(self, obj=None):
        # Load object via
        if type(obj) == str:
            self.obj = parse(obj)
        elif type(obj) == GCToo: self.obj = obj
        else:
            raise TypeError("obj must be either path (str) to a GCToo object, or a GCToo object.")
        
        self.rids = self.obj.row_metadata_df.index.tolist()
        self.cids = self.obj.col_metadata_df.index.tolist()

        # Precomputed Attributes
        self.shape = self.obj.data_df.shape
    
    def __getitem__(self, item):
        return(self.obj.data_df.iloc[item])
    
    def __repr__(self):
        out = ["Custom gctx container object.\n",
               "-----------------------------\n",
               "Shape: ", str(self.obj.data_df.shape), "\n\n",
               "Example rownames: ", str(self.rids[0:5]), "\n",
               "Example colnames: ", str(self.cids[0:5]), "\n"]
        return("".join(out))

        
# Example usage
#file = gctx(gctx_file)
#file
#file.cids
#file.rids
#file[0:3,[0,1]]