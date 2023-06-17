import FDC 
import pandas as pd


DataSet = pd.read_csv('Filepath') # Provide filepath

fdc = FDC.FDClustering(DataSet)