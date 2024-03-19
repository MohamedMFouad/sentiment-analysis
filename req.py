#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:04:25 2024

@author: asabry
"""

import requests

response = requests.post("http://0.0.0.0:3041/sentiment-analysis",
                         json = {"text": "I have a wonderful news"}).json()

print(response)
