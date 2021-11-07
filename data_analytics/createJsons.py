import shutil
import os

dir = 'src/data/'
shutil.rmtree(dir)

os.mkdir(dir)

exec(open('data_analytics/prescription_data.py').read())
exec(open('data_analytics/trxjson.py').read())
