import requests
data_url = "https://www.eia.gov/dnav/pet/xls/PET_PNP_INPT_A_EPC0_YIR_MBBL_M.xls"
r = requests.get(data_url) 
with open("data_set.csv",'wb') as f:
	f.write(r.content)
