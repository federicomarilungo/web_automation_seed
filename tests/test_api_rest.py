import requests
from data.data_reader import DataReader

def test_get_example():
     get_host_url = DataReader.read_file("url_enviroments.json").get('get_host')
     some_location = DataReader.read_file("get_test_data.json").get('some_location')
     response = requests.get(get_host_url + some_location)
     assert response.status_code == 200

def test_post_example():
     post_host_url = DataReader.read_file("url_enviroments.json").get('post_host')
     some_user_and_name = DataReader.read_file("post_test_data.json")
     response = requests.post(post_host_url, data = some_user_and_name)
     r_dictionary= response.json()
     assert response.status_code == 200
     assert r_dictionary['form'] == some_user_and_name
     