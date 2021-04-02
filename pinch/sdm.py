import pandas as pd 
import numpy as np 

def sdm(input_data, min_temp_diff):
    """
    The acronym sdm stands for Streams Data Manipulator. This function will take in the input stream data from the user and apply the problem table algorithm based on the minimum temperature difference selected by the user. 
    
    Parameters
    ----------
    input_data : Pandas DataFrame
              The process plant's streams data obtained from Aspen HYSYS/Plus. 
    
    min_temp_diff : float
                     The minimum temperature selected by the user, which determines the maximum possible amount of heat recovery.
    
    Returns
    -------
    sd_tidy : Pandas DataFrame
                  The converted process plant's streams data.

    Examples 
    --------
    >>> from pinch import sdm
    >>> min_temp_diff = 10.0
    >>> data = pd.DataFrame(np.array([['Cold', 105.6, 271.47, 48.0, 88.1], 
                                      ['hot', 77.75, 149.52, 80.7, 30.0],
                                      ['hot', 15.16, 47.41, 140.2, 25.0],
                                      ['hot', 14.63, 41.72, 59.8, 25.0],
                                      ['hot', 5.25, 34.79, 80.0, 25.0]]), 
                            columns = ['stream_type', 'mass_flow_rate', 
                                       'flowing_heat_capacity', 'initial_temp', 'final_temp'])
    >>> sd_tidy = sdm(data = input_data, min_temp_diff = 10.0)
    """
    