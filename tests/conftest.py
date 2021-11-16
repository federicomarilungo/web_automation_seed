"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):

  # Read the file
  with open('config.json') as config_file:
    config = json.load(config_file)
  
  # Assert values are acceptable
  assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome', 'Remote']
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0

  # Return config so it can be used
  return config

@pytest.fixture
def browser(config):

  opts = selenium.webdriver.ChromeOptions()
  #This option is to avoid an ERROR in logs 
  opts.add_experimental_option('excludeSwitches', ['enable-logging']) 

  # Initialize the WebDriver instance
  if config['browser'] == 'Firefox':
    b = selenium.webdriver.Firefox()
  elif config['browser'] == 'Chrome':
    b = selenium.webdriver.Chrome(options=opts)
  elif config['browser'] == 'Headless Chrome':
    opts.add_argument('headless')
    b = selenium.webdriver.Chrome(options=opts)
  elif config['browser'] == 'Remote':
    b = selenium.webdriver.Remote(
      command_executor='http://localhost:4444')
  else:
    raise Exception(f'Browser "{config["browser"]}" is not supported')

  # Make its calls wait for elements to appear
  b.implicitly_wait(config['implicit_wait'])

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()
