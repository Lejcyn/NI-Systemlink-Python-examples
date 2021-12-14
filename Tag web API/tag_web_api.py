#Import required dependencies
import constants
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TagAPI(object):

    def __init__(self, master_name: str = None, user_name:str=None, password:str=None, protocol:str='http', output=False, session=None):
        self.master_name = master_name
        self.master_auth = (user_name, password)
        self.protocol = protocol
        self.output = output
        self.session = requests.Session() #session if session != None else requests.Session()
    
    
    def get_workspaces(self, take) -> requests.Response:
        url = constants.USER_SVC_URLS['base_sans_protocol'].format(self.protocol, self.master_name) + \
              constants.USER_SVC_URLS['get_workspaces'].format(take)
        if self.output == True:
            print(url)
            print(self.master_auth)
        return self.session.get(url,
                             json={},
                             verify=False,
                             auth=self.master_auth)

    def create_tag(self, query_json) -> requests.Response:
        url = constants.TAG_SVC_URLS['base_sans_protocol'].format(self.protocol, self.master_name) + \
              constants.TAG_SVC_URLS['create_tag']
        if self.output == True:
            print(url)
            print(self.master_auth)
        return self.session.post(url,
                             json=query_json,
                             verify=False,
                             auth=self.master_auth)

    def get_tag_value(self, workspace_id, tag_path) -> requests.Response:
        url = constants.TAG_SVC_URLS['base_sans_protocol'].format(self.protocol, self.master_name) + \
              constants.TAG_SVC_URLS['get_tag_value'].format(workspace_id, tag_path)
        if self.output == True:
            print(url)
            print(self.master_auth)
        return self.session.get(url,
                             json={},
                             verify=False,
                             auth=self.master_auth)
    
    def put_tag_value(self, tag_json) -> requests.Response:
        url = constants.TAG_SVC_URLS['base_sans_protocol'].format(self.protocol, self.master_name) + \
              constants.TAG_SVC_URLS['put_tag_value']
        if self.output == True:
            print(url)
            print(self.master_auth)
        return self.session.post(url,
                             json=tag_json,
                             verify=False,
                             auth=self.master_auth)
