from ens import ENS


ens_names = ["hermes.eth"]


def get_tokens(ns):
	names_mapping = {}

	for name in ens_names: 
		names_mapping.update({name: ns.address(name)})

	return names_mapping