import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
  

df = pd.read_csv('final_data.csv', delimiter="\t")

def barGraph(xAxisData,yAxisData,graphName,xAxisLabel,yAxisLabel,titleLabel):
    plt.bar(xAxisData, yAxisData, color ='blue',
            width = 0.4)
    
    plt.xlabel(xAxisLabel)
    plt.ylabel(yAxisLabel)
    plt.title(titleLabel)
    plt.savefig(graphName)


null_values = df.isna().sum()

barGraph(None,null_values,'null_value_graph.png','columns','null value count','Null Value Graph')
