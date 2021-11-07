import numpy as np
import pandas as pd
import json
from us_state_abbrev import us_state_to_abbrev

path_to_data = 'data/'

def getStateInfo(productData, outputFile):
    sum = productData['TRx_sum'].sum()
    state_sum = pd.DataFrame(columns = ['State', 'Total'])
    for i, state in enumerate(states):
        current_state_data = productData.loc[data.State == state]
        trx = current_state_data['TRx_sum'].sum()
        state_sum.loc[i] = [us_state_to_abbrev[state], trx]
    state_sum['Percent'] = state_sum['Total'].astype(float).div(sum)
    max_percent = state_sum['Percent'].max()
    state_sum['AdjustedPercent'] = state_sum['Percent'].astype(float).div(max_percent).round(2)
    state_sum = state_sum.drop(columns=['Percent'])
    state_sum.to_json(outputFile,orient='records')

data = pd.read_csv('data_analytics/Prescriber_Data.csv')
states = data.State.unique()
products = data.Product.unique()
TRx_columns = ['TRx_Month_1','TRx_Month_2','TRx_Month_3','TRx_Month_4','TRx_Month_5','TRx_Month_6']
NRx_columns = ['NRx_Month_1','NRx_Month_2','NRx_Month_3','NRx_Month_4','NRx_Month_5','NRx_Month_6']
NRx_columns_first3 = ['NRx_Month_1','NRx_Month_2','NRx_Month_3']
NRx_columns_last3 = ['NRx_Month_4','NRx_Month_5','NRx_Month_6']

data["TRx_sum"] = data[TRx_columns].sum(axis=1)
data["NRx_sum"] = data[NRx_columns].sum(axis=1)
data["NRx_sum_first3"] = data[NRx_columns_first3].sum(axis=1)
data["NRx_sum_last3"] = data[NRx_columns_last3].sum(axis=1)
data["NRx_sum_half_diff"] = data['NRx_sum_first3']-data['NRx_sum_last3']

Cholecap = data.loc[data.Product == 'Cholecap']
Zap_a_Pain = data.loc[data.Product == 'Zap-a-Pain']
Nasalclear = data.loc[data.Product == 'Nasalclear']
Nova_itch = data.loc[data.Product == 'Nova-itch']
    
#get state info
getStateInfo(Cholecap, path_to_data + 'StateInfoCholecap.json')
getStateInfo(Zap_a_Pain, path_to_data + 'StateInfoZap_a_Pain.json')
getStateInfo(Nasalclear, path_to_data + 'StateInfoNasalclear.json')
getStateInfo(Nova_itch, path_to_data + 'StateInfoNova_itch.json')

#Get trx sums
sums = pd.DataFrame(columns = ['Product'])
for product in products:
    sums.loc[len(sums.index)] = product
for trx in TRx_columns:
    trx_sum = [Cholecap[trx].sum(), Zap_a_Pain[trx].sum(), Nasalclear[trx].sum(), Nova_itch[trx].sum()]
    sums[trx] = trx_sum

sums.to_json(path_to_data + 'sums.json',orient='records')

#Top sellers for each drug
top_sellers_num = 20
top_TRx_Cholecap = Cholecap.nlargest(top_sellers_num, 'TRx_sum').copy().set_index(pd.Index(list(range(0,top_sellers_num))))
top_TRx_Zap_a_Pain = Zap_a_Pain.nlargest(top_sellers_num, 'TRx_sum').copy().set_index(pd.Index(list(range(0,top_sellers_num))))
top_TRx_Nasalclear = Nasalclear.nlargest(top_sellers_num, 'TRx_sum').copy().set_index(pd.Index(list(range(0,top_sellers_num))))
top_TRx_Nova_itch = Nova_itch.nlargest(top_sellers_num, 'TRx_sum').copy().set_index(pd.Index(list(range(0,top_sellers_num))))

top_TRx_Cholecap.to_json(path_to_data + 'topSellersCholecap.json', orient='records')
top_TRx_Zap_a_Pain.to_json(path_to_data + 'topSellersZap_a_Pain.json', orient='records')
top_TRx_Nasalclear.to_json(path_to_data + 'topSellersNasalclear.json',orient='records')
top_TRx_Nova_itch.to_json(path_to_data + 'topSellersNova_itch.json',orient='records')

top_TRx_Cholecap.to_json(path_to_data + 'topSellersCholecapKV.json', orient='index')
top_TRx_Zap_a_Pain.to_json(path_to_data + 'topSellersZap_a_PainKV.json', orient='index')
top_TRx_Nasalclear.to_json(path_to_data + 'topSellersNasalclearKV.json',orient='index')
top_TRx_Nova_itch.to_json(path_to_data + 'topSellersNova_itchKV.json',orient='index')

#Sales targets
average_NRx_Cholecape = Cholecap['NRx_sum'].mean()
average_NRx_Zap_a_Pain = Zap_a_Pain['NRx_sum'].mean()
average_NRx_Nasalclear = Nasalclear['NRx_sum'].mean()
average_NRx_Nova_itch = Nova_itch['NRx_sum'].mean()

Cholecap_r_top = Cholecap.copy()
Zap_a_Pain_r_top = Zap_a_Pain.copy()
Nasalclear_r_top = Nasalclear.copy()
Nova_itch_r_top = Nova_itch.copy()
for index, row in top_TRx_Cholecap.iterrows():
    Cholecap_r_top.drop(Cholecap_r_top[Cholecap_r_top['id'] == row['id']].index, inplace=True)
for index, row in top_TRx_Zap_a_Pain.iterrows():
    Zap_a_Pain_r_top.drop(Zap_a_Pain_r_top[Zap_a_Pain_r_top['id'] == row['id']].index, inplace=True)
for index, row in top_TRx_Nasalclear.iterrows():
    Nasalclear_r_top.drop(Nasalclear_r_top[Nasalclear_r_top['id'] == row['id']].index, inplace=True)
for index, row in top_TRx_Nova_itch.iterrows():
    Nova_itch_r_top.drop(Nova_itch_r_top[Nova_itch_r_top['id'] == row['id']].index, inplace=True)

Cholecap_upandcoming = Cholecap_r_top.loc[Cholecap_r_top.NRx_sum>average_NRx_Cholecape].nlargest(10, 'NRx_sum_last3')
Cholecap_rising = Cholecap_r_top.loc[Cholecap_r_top.NRx_sum<average_NRx_Cholecape].nlargest(10, 'NRx_sum_last3')
Cholecap_drop_off = Cholecap_r_top.nlargest(10, 'NRx_sum_half_diff')

Cholecap_upandcoming.to_json(path_to_data + 'targetUACCholecap.json',orient='records')
Cholecap_rising.to_json(path_to_data + 'targetRiseCholecap.json',orient='records')
Cholecap_drop_off.to_json(path_to_data + 'targetDropCholecap.json',orient='records')


Zap_a_Pain_upandcoming = Zap_a_Pain_r_top.loc[Zap_a_Pain_r_top.NRx_sum>average_NRx_Zap_a_Pain].nlargest(10, 'NRx_sum_last3')
Zap_a_Pain_rising = Zap_a_Pain_r_top.loc[Zap_a_Pain_r_top.NRx_sum<average_NRx_Zap_a_Pain].nlargest(10, 'NRx_sum_last3')
Zap_a_Pain_drop_off = Zap_a_Pain_r_top.nlargest(10, 'NRx_sum_half_diff')

Zap_a_Pain_upandcoming.to_json(path_to_data + 'targetUACZap_a_Pain.json',orient='records')
Zap_a_Pain_rising.to_json(path_to_data + 'targetRiseZap_a_Pain.json',orient='records')
Zap_a_Pain_drop_off.to_json(path_to_data + 'targetDropZap_a_Pain.json',orient='records')


Nasalclear_upandcoming = Nasalclear_r_top.loc[Nasalclear_r_top.NRx_sum>average_NRx_Nasalclear].nlargest(10, 'NRx_sum_last3')
Nasalclear_rising = Nasalclear_r_top.loc[Nasalclear_r_top.NRx_sum<average_NRx_Nasalclear].nlargest(10, 'NRx_sum_last3')
Nasalclear_drop_off = Nasalclear_r_top.nlargest(10, 'NRx_sum_half_diff')

Nasalclear_upandcoming.to_json(path_to_data + 'targetUACNasalclear.json',orient='records')
Nasalclear_rising.to_json(path_to_data + 'targetRiseNasalclear.json',orient='records')
Nasalclear_drop_off.to_json(path_to_data + 'targetDropNasalclear.json',orient='records')


Nova_itch_upandcoming = Nova_itch_r_top.loc[Nova_itch_r_top.NRx_sum>average_NRx_Nova_itch].nlargest(10, 'NRx_sum_last3')
Nova_itch_rising = Nova_itch_r_top.loc[Nova_itch_r_top.NRx_sum<average_NRx_Nova_itch].nlargest(10, 'NRx_sum_last3')
Nova_itch_drop_off = Nova_itch_r_top.nlargest(10, 'NRx_sum_half_diff')

Nova_itch_upandcoming.to_json(path_to_data + 'targetUACNova_itch.json',orient='records')
Nova_itch_rising.to_json(path_to_data + 'targetRiseNova_itch.json',orient='records')
Nova_itch_drop_off.to_json(path_to_data + 'targetDropNova_itch.json',orient='records')
