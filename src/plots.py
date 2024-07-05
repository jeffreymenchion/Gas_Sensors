import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def eight_sensor_heatmap(df, path=None):
    """Returns heatmap of correlations 
    for the eight important sensors"""
    

    sensor_col_list = ['PT08.S1(CO)', 'PT08.S2(NMHC)', 'PT08.S3(NOx)', 'PT08.S4(NO2)', 'PT08.S5(O3)', 'T', 'RH', 'AH']
    df3 = df[sensor_col_list]

    sns.heatmap(df3.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')

    #Save or show the plot
    if path:
        plt.savefig(path)
    else:
        plt.show()
        



if __name__ == "__main__":
    pass
