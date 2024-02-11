import requests
import sys
from io import StringIO
import numpy as np
import pandas as pd

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
raw_v = r.json()['data']