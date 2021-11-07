import numpy as np
import pandas as pd
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

def getTopSellers(productData, outputFileNoJson):
    top_sellers_num = 20
    top_TRx = productData.nlargest(top_sellers_num, 'TRx_sum').copy().set_index(pd.Index(list(range(0,top_sellers_num))))
    top_TRx.to_json(path_to_data + outputFileNoJson + '.json', orient='records') 
    top_TRx.to_json(path_to_data + outputFileNoJson + 'KV.json', orient='index')
    return top_TRx

def getSalesTargets(productData, average, drugName):
    total_targets_num = 10

    upandcoming = productData.loc[productData.NRx_sum>average].nlargest(total_targets_num, 'NRx_sum_last3').copy().set_index(pd.Index(list(range(0,total_targets_num))))
    rising = productData[productData.NRx_sum<average].nlargest(total_targets_num, 'NRx_sum_last3').copy().set_index(pd.Index(list(range(0,total_targets_num))))
    drop_off = productData.nlargest(total_targets_num, 'NRx_sum_half_diff').copy().set_index(pd.Index(list(range(0,total_targets_num))))

    upandcoming.to_json(path_to_data + 'targetUAC'+ drugName +'.json',orient='index')
    rising.to_json(path_to_data + 'targetRise' + drugName + '.json',orient='index')
    drop_off.to_json(path_to_data + 'targetDrop' + drugName + '.json',orient='index')

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
top_TRx_Cholecap = getTopSellers(Cholecap, 'topSellersCholecap')
top_TRx_Zap_a_Pain = getTopSellers(Zap_a_Pain, 'topSellersZap_a_Pain')
top_TRx_Nasalclear = getTopSellers(Nasalclear, 'topSellersNasalclear')
top_TRx_Nova_itch = getTopSellers(Nova_itch, 'topSellersNova_itch')


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

total_targets_num = 10

getSalesTargets(Cholecap_r_top, average_NRx_Cholecape, 'Cholecap')
getSalesTargets(Nasalclear_r_top, average_NRx_Nasalclear, 'Nasalclear')
getSalesTargets(Zap_a_Pain_r_top, average_NRx_Zap_a_Pain, 'Zap_a_Pain')
getSalesTargets(Nova_itch_r_top, average_NRx_Nova_itch, 'Nova_itch')

