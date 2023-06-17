import pandas as pd



class FDClustering :
    
    """

        FDC takes the pandas Dataframe and does Feature Type Distributed Clustering on the DataFrame

        DataSet : pandas DataFrame 

    """ 

    def __init__(self , DataSet : pd.DataFrame) -> None:
        import pandas as pd
        self.DataSet = DataSet
        self._Normalize()


    """

        Function to change DataFrame after initialization
        
        DataSet     : pandas DataFrame
        
    """

    def SetData(self, DataSet : pd.DataFrame) :
        self.DataFrame = DataSet
        self.Normalize()


    """
    
        Funtion to Normalize the DataFrame 

    """

    def _Normalize(self) :
        self.DataFrame = (self.DataFrame - self.DataFrame.mean()) / self.DataFrame.std()

    """
    
        Preprocessing Function to process the data, set to protected to avoid access from outside class
    
    """
    
    
    
    def _Preprocessing(self) :
        try :
            pass


        except :
            return 'Error'
        


    """
    
        Function to arrange data features to different feature types
    
    """
        

    def DistributeData() : 
        pass


    """
    
        Function to reduce data to lower dimensions 

        axes    : The number of axes to keep after reduction 
        method  : The dimension reduction technique used
    
    """

    def ReduceData(self, axes : int , method : str) :
        if method == 'UMAP' :
            pass
        
        elif method == 'PCA' : 
            pass

        else : 
            pass