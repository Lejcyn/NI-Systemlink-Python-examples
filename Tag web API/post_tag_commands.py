#Import required dependencies
from tag_web_api import TagAPI

actions = ["create"] # ["workspaces", "create", "write", "read"]
server = "10.92.1.27:80"                     # "localhost:9090"
# username = "admin"                            # enter the credentials here that you
# password = "admin"                     # use to log in to SystemLink web pages
username = "SystemLink Tester"                            # enter the credentials here that you
password = "Demonstration0!"                     # use to log in to SystemLink web pages
protocol = "http"                             # protocol for the server connection ["http", "https"]
print_output = True                           # whether to print the url and the authorization used
print_response = True                         # whether to print the response of the web service command
tag_api = TagAPI(server, username, password, protocol, print_output, session=None)

if "workspaces" in actions:
    response_json = tag_api.get_workspaces(50).json()
    if print_response == True: print(response_json)

if "create" in actions:
    workspace_id = "ffb0bc13-ff53-4bc4-8c30-48afe96632f7" # Default Workspace
    #workspace_id = "dd520ec0-461c-4887-8900-512d7f97cac1" # TestWorkspace1
    tag_path = "Python Test"
    tag_properties = {"key1": "value1", "key2": "value2"}
    tag_keywords = ["fooKeyword", "barKeyword"]
    tag_create_json = {"type": "DOUBLE", "properties": tag_properties, "path": tag_path, "keywords": tag_keywords, "collectAggregates": True, "workspace": workspace_id}
    response = tag_api.create_tag(tag_create_json)
    if print_response == True: print(response)

if "read" in actions:
    workspace_id = "e8c4a2c6-867a-49d6-a948-dfe231a41c81"
    tag_path = "AWS.Station.Report.Concat.Duration"
    response_json = tag_api.get_tag_value(workspace_id, tag_path).json()
    if print_response == True: print(response_json)

if "write" in actions:
    workspace_id = "e8c4a2c6-867a-49d6-a948-dfe231a41c81"
    tag_path = "AWS.Station.Report.Concat.Duration"
    tag_update_json = {"value": {"type": "DOUBLE", "value": "3.145"}, "timestamp": "2021-05-03T18:45:08Z"}
    tag_write_json = [ {"path": tag_path, "updates": [tag_update_json], "workspace": workspace_id} ]
    response = tag_api.put_tag_value(tag_write_json)
    if print_response == True: print(response)
