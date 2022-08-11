import requests
import time
import json

import config as cfg


ens_names = {'frank.eth': {}, '123456.eth': {}, 'test0.eth': {}}


"""
1. retrieve assets - address = owner_id
2. retrieve asset - address = asset_contract[address]/token_id
"""

def get_token_address(ns, ens_name):
	print(ns)
	return ns.address(ens_name)


def get_assets_opensea(address):
	url = "https://testnets-api.opensea.io/api/v1/asset/"+address

	response = requests.get(url)

	return json.loads(response.text)


def get_asset_metadata(ns):
	average_last_sale = 0

	for name in ens_names:
		print(name)
		address = get_token_address(ns, name)
		ens_names[name]['address'] = address

		url_owner_assets = "https://testnets-api.opensea.io/api/v1/assets?owner=" + address

		time.sleep(10)

		response = requests.get(url_owner_assets)

		owner_assets_data = json.loads(response.text)


		if owner_assets_data["assets"]:


			token_id = owner_assets_data["assets"][0]["token_id"]
			asset_contract_address = owner_assets_data["assets"][0]["asset_contract"]["address"]

			ens_names[name]['token_id'] = token_id
			ens_names[name]['asset_adress'] = asset_contract_address

			asset_url = f"https://testnets-api.opensea.io/api/v1/asset/{asset_contract_address}/{token_id}/"

			res = requests.get(asset_url)
			asset_data = json.loads(res.text)

			if asset_data.get("last_sale", None):

				average_last_sale+=asset_data["last_sale"]

		else:
			print(response)
			print(data)

	print(average_last_sale/len(ens_names))

	return average_last_sale/len(ens_names)
