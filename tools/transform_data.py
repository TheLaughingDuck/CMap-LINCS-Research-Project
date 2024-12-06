

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