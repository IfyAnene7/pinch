from pinch import __version__
from pinch import sdm
import pandas as pd
import numpy as np
from pytest import raises

data = pd.DataFrame(np.array([['Cold', 105.6, 271.47, 48.0, 88.1], 
                                      ['hot', 77.75, 149.52, 80.7, 30.0],
                                      ['hot', 15.16, 47.41, 140.2, 25.0],
                                      ['hot', 14.63, 41.72, 59.8, 25.0],
                                      ['hot', 5.25, 34.79, 80.0, 25.0]]), 
                            columns = ['stream_type', 'mass_flow_rate', 
                                       'flowing_heat_capacity', 'initial_temp', 'final_temp'])


def test_input_data():

    with raises(TypeError):
        sdm(input_data = 1.0, min_temp_diff = 10.0)

    with raises(TypeError):
        sdm(data, min_temp_diff = data)
        
    with raises(TypeError):
        sdm("data", min_temp_diff = data)
        
    with raises(TypeError):
        sdm("data", min_temp_diff = "data")
        
    with raises(TypeError):
        sdm("data", min_temp_diff = "10.0")
