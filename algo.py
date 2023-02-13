import pandas as pd 
inputa = int(input("Enter your break-point : "))
series1 = pd.Series([1,inputa,3])
# series2 = pd.Series([4,5,6])
# get username
columns1 = ['PLAYER_NAME','START', 'PREDICTION', 'END']
df = pd.DataFrame([list(series1)],columns=columns1)


print(df)