# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:06:02 2019

@author: user
"""

'''
entrophy scale
'''
import pandas as pd
import math
import numpy as np
#表格資料內容設定
M_aggregate=[[3,5,40,506,96,27],[4,7,280,29,39,2],[1,1,1,7,4,671],[10,162,3,119,73,2],[331,22,5,70,13,23],[5,358,12,212,48,13]]
col_name=['Entertainment','Financial','Foreign','Metro','National','Sports','Entropy']

e = 0 #Total Entropy
m_sum=0 #樣本總數
e_i = [0 for x in range(0,6)] #各群的Entropy
M_aggregate_2d_arrary = np.array(M_aggregate)
m_j =  M_aggregate_2d_arrary.sum(axis=1) #計算各群的數量

temp=0
for i in range(0,6): #群數
    for j in range(0,6): #類別個數
        p_i_j = M_aggregate_2d_arrary[i][j]/m_j[i] #在i群下之各類別的百分比
        e_i[i] += 0 - p_i_j*math.log2(p_i_j)
    M_aggregate[i].append(e_i[i])
    
#將資料轉換成dataframe形式輸出
df=pd.DataFrame(M_aggregate,columns=col_name,index=range(1,len(M_aggregate)+1))

for i in m_j:
    m_sum+=i
#計算Total Entropy
for i in range(0,6):
    e += m_j[i]/m_sum*e_i[i]
print(df)
print("-"*73+"\n Total Entropy:"+str(e))