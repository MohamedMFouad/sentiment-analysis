#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:17:36 2024

@author: asabry
"""

from sentiment_api import app

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 3040)