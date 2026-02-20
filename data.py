import pandas as pd
import numpy as np

def initialization():
    decay_data = {
        #time in mircoseconds
        "x": [0.0, 48.0, 88.00, 128.0, 168.0, 208.0, 248.0, 288.0, 328.0, 368.0, 408.0, 448.0, 528.0, 568.0, 608.0, 736.0, 896.0, 1056, 1240],
        #voltage in volts
        "y": [1.76, 1.52, 1.34, 1.20, 1.04, 0.920, 0.820, 0.720, 0.640, 0.580, 0.520, 0.460, 0.400, 0.340, 0.300, 0.280, 0.160, 0.060, 0.040]
    }

    decay_df = pd.DataFrame(decay_data)

    low_pass_data = {
        #frequency in hertz
        "Frequency": [20.00, 40.00, 60.00, 80.00, 100.0, 200.0, 300.8, 400.0, 502.5, 602.4, 701.8, 801.3, 900.9, 1000, 1506, 2000, 2500, 4000, 6024, 8000, 10000, 15020, 20040],
        #peak to peak voltage output in volts
        "V_pp (Out)": [5.121, 5.121, 5.121, 5.121, 5.121, 4.881, 4.481, 4.081, 3.561, 3.201, 2.921, 2.641, 2.441, 2.281, 1.601, 1.241, 1.041, 0.616, 0.424, 0.324, 0.260, 0.180, 0.138]
    }

    low_pass_df = pd.DataFrame(low_pass_data)

    high_pass_data = {
        #frequency in hertz
        "Frequency": [20.00, 40.00, 60.24, 80.00, 100.0, 120.0, 160.0, 200.0, 240.0, 280.0, 350.0, 400.0, 500.0, 600.0, 700.0, 802.6, 1000, 2000, 4000, 8065, 16050, 20000],
        #peak to peak voltage output in volts
        "V_pp (Out)": [0.228, 0.432, 0.640, 0.848, 1.041, 1.221, 1.621, 1.941, 2.261, 2.601, 3.001, 3.281, 3.641, 3.921, 4.161, 4.321, 4.561, 5.041, 5.121, 5.121, 5.121, 5.121]
    }

    high_pass_df = pd.DataFrame(high_pass_data)

    print(decay_df)
    print(low_pass_df)
    print(high_pass_df)

initialization()
