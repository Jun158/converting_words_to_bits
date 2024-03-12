# import lib
import pandas as pd
import re

# read the main file
tgt="target_data/tgtData.csv"
df=pd.read_csv(tgt, encoding='shift_jis')
   
 # retrieve the target columns and create a list containing the words between the slashes
def main(row):
    row=row["Column45"]
    [flag.append(word) for word in row.split("/") if word not in flag]

flag=[]
df.apply(main, axis=1)
# print("flag: ", flag)

# create a clmn from a list
for idx, i in enumerate(flag):
    df.at[idx, 'flags'] = i

# df["flags"].to_csv("temp.csv")

print(flag)