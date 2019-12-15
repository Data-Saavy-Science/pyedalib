def easyEDA(dataFrame, columnName):
    #Return type of variable
    if(len(dataFrame[columnName].unique()) < 50 and (str(dataFrame[columnName].dtype).startswith('float') or str(dataFrame[columnName].dtype).startswith('int') )):
        if(dataFrame[columnName].nunique() == 2 or dataFrame[columnName].nunique() < 5 or dataFrame[columnName].nunique() < 15 ):
                    print('    Type of Data: Categorical')
                    print('    '+ str(dict(dataFrame.groupby([columnName]).count().iloc[:,0])))
        else:
            print('    Type of Data: Numerical and Discrete')
            print('    '+ str(dataFrame[columnName].unique()))
    elif(len(dataFrame[columnName].unique()) > 50 and (str(dataFrame[columnName].dtype).startswith('float') or str(dataFrame[columnName].dtype).startswith('int'))):
        print('    Type of Data: Numerical and Continuous')
    elif(len(dataFrame[columnName].unique()) < 50 and str(dataFrame[columnName].dtype).startswith('object')):
        print('    Type of Data: Categorical')
        print('    '+ str(dict(dataFrame.groupby([columnName]).count().iloc[:,0])))
    else:
        print('    Type of Data: Unknown dig in to find out')
    
    #Number of unique values
    print('    Number of uniques values : ' + str(dataFrame[columnName].nunique()))
    
    #Number of Null Values
    print('    Percentage of missing values : ' + str(round(((dataFrame[columnName].isnull().sum()/dataFrame.shape[0])*100),2)) + '%')
    

def eda(dataFrame):
    counter = 1
    print('Total number of Rows : ' + str(len(dataFrame)))
    print('Total number of columns : ' + str(len(dataFrame.columns)))
    for i in dataFrame.columns:
        print('\n Column ' + str(counter) + ' : ' + str(i))
        easyEDA(dataFrame,i)
        counter = counter + 1