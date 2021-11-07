import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import json
from us_state_abbrev import us_state_to_abbrev

path_to_data = 'data/'

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


#Top sellers for all drugs
top_TRx_all = data.nlargest(10, 'TRx_sum')
top_NRx_all = data.nlargest(10, 'NRx_sum')

with open(path_to_data + 'topSellersTRx.json', 'w') as outfile:
    json.dump(top_TRx_all.to_json(orient='index'), outfile)
with open(path_to_data + 'topSellersNRx.json', 'w') as outfile:
    json.dump(top_NRx_all.to_json(orient='index'), outfile)

Cholecap = data.loc[data.Product == 'Cholecap']
Zap_a_Pain = data.loc[data.Product == 'Zap-a-Pain']
Nasalclear = data.loc[data.Product == 'Nasalclear']
Nova_itch = data.loc[data.Product == 'Nova-itch']
    
#get state info
Cholecap_sum = Cholecap['TRx_sum'].sum()
Cholecap_state_sum = pd.DataFrame(columns = ['State', 'Total'])
for i, state in enumerate(states):
    current_state_data = Cholecap.loc[data.State == state]
    trx = current_state_data['TRx_sum'].sum()
    Cholecap_state_sum.loc[i] = [us_state_to_abbrev[state], trx]
Cholecap_state_sum['Percent'] = Cholecap_state_sum['Total'].astype(float).div(Cholecap_sum)
Cholecap_max_percent = Cholecap_state_sum['Percent'].max()
Cholecap_state_sum['AdjustedPercent'] = Cholecap_state_sum['Percent'].astype(float).div(Cholecap_max_percent).round(2)
Cholecap_state_sum = Cholecap_state_sum.drop(columns=['Percent'])
with open(path_to_data + 'CholecapStateInfo.json', 'w') as outfile:
    json.dump(Cholecap_state_sum.to_json(orient='index'), outfile)

Zap_a_Pain_sum = Zap_a_Pain['TRx_sum'].sum()
Zap_a_Pain_state_sum = pd.DataFrame(columns = ['State', 'Total'])
for i, state in enumerate(states):
    current_state_data = Zap_a_Pain.loc[data.State == state]
    trx = current_state_data['TRx_sum'].sum()
    Zap_a_Pain_state_sum.loc[i] = [us_state_to_abbrev[state], trx]
Zap_a_Pain_state_sum['Percent'] = Zap_a_Pain_state_sum['Total'].astype(float).div(Zap_a_Pain_sum)
Zap_a_Pain_max_percent = Zap_a_Pain_state_sum['Percent'].max()
Zap_a_Pain_state_sum['AdjustedPercent'] = Zap_a_Pain_state_sum['Percent'].astype(float).div(Zap_a_Pain_max_percent).round(2)
Zap_a_Pain_state_sum = Zap_a_Pain_state_sum.drop(columns=['Percent'])
with open(path_to_data + 'Zap_a_PainStateInfo.json', 'w') as outfile:
    json.dump(Zap_a_Pain_state_sum.to_json(orient='index'), outfile)

Nasalclear_sum = Nasalclear['TRx_sum'].sum()
Nasalclear_state_sum = pd.DataFrame(columns = ['State', 'Total'])
for i, state in enumerate(states):
    current_state_data = Nasalclear.loc[data.State == state]
    trx = current_state_data['TRx_sum'].sum()
    Nasalclear_state_sum.loc[i] = [us_state_to_abbrev[state], trx]
Nasalclear_state_sum['Percent'] = Nasalclear_state_sum['Total'].astype(float).div(Nasalclear_sum)
Nasalclear_max_percent = Nasalclear_state_sum['Percent'].max()
Nasalclear_state_sum['AdjustedPercent'] = Nasalclear_state_sum['Percent'].astype(float).div(Nasalclear_max_percent).round(2)
Nasalclear_state_sum = Nasalclear_state_sum.drop(columns=['Percent'])
with open(path_to_data + 'NasalclearStateInfo.json', 'w') as outfile:
    json.dump(Nasalclear_state_sum.to_json(orient='index'), outfile)

Nova_itch_sum = Nova_itch['TRx_sum'].sum()
Nova_itch_state_sum = pd.DataFrame(columns = ['State', 'Total'])
for i, state in enumerate(states):
    current_state_data = Nova_itch.loc[data.State == state]
    trx = current_state_data['TRx_sum'].sum()
    Nova_itch_state_sum.loc[i] = [us_state_to_abbrev[state], trx]
Nova_itch_state_sum['Percent'] = Nova_itch_state_sum['Total'].astype(float).div(Nova_itch_sum)
Nova_itch_max_percent = Nova_itch_state_sum['Percent'].max()
Nova_itch_state_sum['AdjustedPercent'] = Nova_itch_state_sum['Percent'].astype(float).div(Nova_itch_max_percent).round(2)
Nova_itch_state_sum = Nova_itch_state_sum.drop(columns=['Percent'])
with open(path_to_data + 'Nova_itchStateInfo.json', 'w') as outfile:
    json.dump(Nova_itch_state_sum.to_json(orient='index'), outfile)

#Get trx sums
sums = pd.DataFrame(columns = ['Product'])
for product in products:
    sums.loc[len(sums.index)] = product
for trx in TRx_columns:
    trx_sum = [Cholecap[trx].sum(), Zap_a_Pain[trx].sum(), Nasalclear[trx].sum(), Nova_itch[trx].sum()]
    sums[trx] = trx_sum

with open(path_to_data + 'sums.json', 'w') as outfile:
    json.dump(sums.to_json(orient='index'), outfile)

X = np.array([1,2,3,4,5,6]).reshape(-1,1)
Cholecap_Y = sums[sums['Product'] == 'Cholecap'][TRx_columns].values.reshape(-1, 1)
Zap_a_Pain_Y = sums[sums['Product'] == 'Zap-a-Pain'][TRx_columns].values.reshape(-1, 1)
Nasalclear_Y = sums[sums['Product'] == 'Nasalclear'][TRx_columns].values.reshape(-1, 1)
Nova_itch_Y = sums[sums['Product'] == 'Nova-itch'][TRx_columns].values.reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(X, Cholecap_Y)
Cholecap_Y_pred = linear_regressor.predict(X)
linear_regressor.fit(X, Zap_a_Pain_Y)
Zap_a_Pain_Y_pred = linear_regressor.predict(X)
linear_regressor.fit(X, Nasalclear_Y)
Nasalclear_Y_pred = linear_regressor.predict(X)
linear_regressor.fit(X, Nova_itch_Y)
Nova_itch_Y_pred = linear_regressor.predict(X)
plt.scatter(X, Cholecap_Y)
plt.plot(X, Cholecap_Y_pred, color='red')
plt.savefig(path_to_data + 'Cholecap.png')
plt.close()
plt.scatter(X, Zap_a_Pain_Y)
plt.plot(X, Zap_a_Pain_Y_pred, color='red')
plt.savefig(path_to_data + 'Zap_a_Pain.png')
plt.close()
plt.scatter(X, Nasalclear_Y)
plt.plot(X, Nasalclear_Y_pred, color='red')
plt.savefig(path_to_data + 'Nasalclear.png')
plt.close()
plt.scatter(X, Nova_itch_Y)
plt.plot(X, Nova_itch_Y_pred, color='red')
plt.savefig(path_to_data + 'Nova_itch.png')
plt.close()
    

#Top sellers for each drug
top_TRx_Cholecap = Cholecap.nlargest(20, 'TRx_sum')
top_TRx_Zap_a_Pain = Zap_a_Pain.nlargest(20, 'TRx_sum')
top_TRx_Nasalclear = Nasalclear.nlargest(20, 'TRx_sum')
top_TRx_Nova_itch = Nova_itch.nlargest(20, 'TRx_sum')

with open(path_to_data + 'topSellersCholecap.json', 'w') as outfile:
    json.dump(top_TRx_Cholecap.to_json(orient='index'), outfile)

with open(path_to_data + 'topSellersZap_a_Pain.json', 'w') as outfile:
    json.dump(top_TRx_Zap_a_Pain.to_json(orient='index'), outfile)

with open(path_to_data + 'topSellersNasalclear.json', 'w') as outfile:
    json.dump(top_TRx_Nasalclear.to_json(orient='index'), outfile)

with open(path_to_data + 'topSellersNova_itch.json', 'w') as outfile:
    json.dump(top_TRx_Nova_itch.to_json(orient='index'), outfile)


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

with open(path_to_data + 'targetUACCholecap.json', 'w') as outfile:
    json.dump(Cholecap_upandcoming.to_json(orient='index'), outfile)

with open(path_to_data + 'targetRiseCholecap.json', 'w') as outfile:
    json.dump(Cholecap_rising.to_json(orient='index'), outfile)

with open(path_to_data + 'targetDropCholecap.json', 'w') as outfile:
    json.dump(Cholecap_drop_off.to_json(orient='index'), outfile)

Zap_a_Pain_upandcoming = Zap_a_Pain_r_top.loc[Zap_a_Pain_r_top.NRx_sum>average_NRx_Zap_a_Pain].nlargest(10, 'NRx_sum_last3')
Zap_a_Pain_rising = Zap_a_Pain_r_top.loc[Zap_a_Pain_r_top.NRx_sum<average_NRx_Zap_a_Pain].nlargest(10, 'NRx_sum_last3')
Zap_a_Pain_drop_off = Zap_a_Pain_r_top.nlargest(10, 'NRx_sum_half_diff')

with open(path_to_data + 'targetUACZap_a_Pain.json', 'w') as outfile:
    json.dump(Zap_a_Pain_upandcoming.to_json(orient='index'), outfile)

with open(path_to_data + 'targetRiseZap_a_Pain.json', 'w') as outfile:
    json.dump(Zap_a_Pain_rising.to_json(orient='index'), outfile)

with open(path_to_data + 'targetDropZap_a_Pain.json', 'w') as outfile:
    json.dump(Zap_a_Pain_drop_off.to_json(orient='index'), outfile)

Nasalclear_upandcoming = Nasalclear_r_top.loc[Nasalclear_r_top.NRx_sum>average_NRx_Nasalclear].nlargest(10, 'NRx_sum_last3')
Nasalclear_rising = Nasalclear_r_top.loc[Nasalclear_r_top.NRx_sum<average_NRx_Nasalclear].nlargest(10, 'NRx_sum_last3')
Nasalclear_drop_off = Nasalclear_r_top.nlargest(10, 'NRx_sum_half_diff')

with open(path_to_data + 'targetUACNasalclear.json', 'w') as outfile:
    json.dump(Nasalclear_upandcoming.to_json(orient='index'), outfile)

with open(path_to_data + 'targetRiseNasalclear.json', 'w') as outfile:
    json.dump(Nasalclear_rising.to_json(orient='index'), outfile)

with open(path_to_data + 'targetDropNasalclear.json', 'w') as outfile:
    json.dump(Nasalclear_drop_off.to_json(orient='index'), outfile)

Nova_itch_upandcoming = Nova_itch_r_top.loc[Nova_itch_r_top.NRx_sum>average_NRx_Nova_itch].nlargest(10, 'NRx_sum_last3')
Nova_itch_rising = Nova_itch_r_top.loc[Nova_itch_r_top.NRx_sum<average_NRx_Nova_itch].nlargest(10, 'NRx_sum_last3')
Nova_itch_drop_off = Nova_itch_r_top.nlargest(10, 'NRx_sum_half_diff')

with open(path_to_data + 'targetUACNova_itch.json', 'w') as outfile:
    json.dump(Nova_itch_upandcoming.to_json(orient='index'), outfile)

with open(path_to_data + 'targetRiseNova_itch.json', 'w') as outfile:
    json.dump(Nova_itch_rising.to_json(orient='index'), outfile)

with open(path_to_data + 'targetDropNova_itch.json', 'w') as outfile:
    json.dump(Nova_itch_drop_off.to_json(orient='index'), outfile)

