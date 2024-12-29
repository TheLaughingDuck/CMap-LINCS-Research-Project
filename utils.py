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

def standardize_dose_unit(pert_dose, pert_dose_unit):
    '''pert_dose: the precise dose used in an experiment.
    pert_dose_unit: the unit of the dose.
    
    This function returns the pert_dose given in unit mg/ml.
    
    The possible units are: {'ng/ml', nan, 'ng/uL', 'ug/ml', 'uM', 'mg/ml'}
    
    But 'nan' and 'uM' should be removed before they get to this function.'''

    if pert_dose_unit == "ng/ml": multiplier = 10**(-6) #nanogram per mililitre
    elif pert_dose_unit == "ng/uL": multiplier =  10**(-3) #nanogram per microlitre
    elif pert_dose_unit == "ug/ml": multiplier = 10**(-3) # microgram per mililitre
    elif pert_dose_unit == "mg/ml": multiplier = 1 # miligram per mililitre
    else: raise ValueError("Urecognized pert_dose_unit: " + str(pert_dose_unit))

    return(multiplier * pert_dose)