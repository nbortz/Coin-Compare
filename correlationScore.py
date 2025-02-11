import numpy as np

# Intake user coin data in set1, pass compare token data as set 2
def correlation_score(set1, set2):
    # Check set lengths before comparision
    if len(set1) != 4 or len(set2) != 4 :
        raise ValueError("One or both sets of data are missing a value, please try again")
    # Return correlation score
    return np.corrcoef(set1, set2)[0,1]