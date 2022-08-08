import requests

import config as cfg


def get_assets():
	r = requests.get(cfg.base_url+"/assets") #, auth=(cfg.user, cfg.pw))

	return r.text