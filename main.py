import requests
import pandas as pd
from getpass import getpass
import json
import os
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt

rent = pd.read_csv('/Users/juniorlinhares/Documents/projects/Project-Data-Pipeline/data/Barcelona_rent_price.csv')