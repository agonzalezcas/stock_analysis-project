from imports import *
from functions import *
from settings import *

# start = time.time()

# df_all = Analyze_all ()
# df1 = df_all[0]

# jsonFile = overview_jsonPath + 'overview.json'

# df1.to_json(jsonFile)

# end = time.time()
# delta = end-start
# print('time elapsed = ' + str(delta))

try:

	start = time.time()

	#df_all = Analyze_all_MP ()
	df_all = Analyze_all()

except Exception as ex:
	print('Function failed')

end = time.time()
delta = end-start
print('time elapsed = ' + str(delta))
