import requests
import web3

from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
from ens import ENS

from get_assets import get_assets
from get_token_address import get_tokens


def main():
	print("beep")
	# print(get_assets())
	url = "https://eth-rinkeby.alchemyapi.io/v2/"

	w3 = web3.Web3(web3.HTTPProvider(url))
	w3.middleware_onion.inject(geth_poa_middleware, layer=0)

	w3.isConnected()

	ns = ENS.fromWeb3(w3)

	# get address
	address = ns.address('hermes.eth')


	url = "https://testnets-api.opensea.io/api/v1/asset_contract/"+str(address)

	response = requests.get(url)

	print(response)

	print(response.text)


	# print(get_tokens(ns))



if __name__ == "__main__":
	print("boop")
	main()