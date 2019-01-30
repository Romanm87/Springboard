#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 18:19:40 2019

@author: roman
"""

import numpy as np
import pandas as pd
import os
os.chdir('/home/roman/Documents/Projects/Coding challenges/MarketData')

sectors = ['technology', 'healthcare', 'finance', 'consumer']
mc_min = 1e10
mc_lower = 1e11
mc_upper = 5e11
mc_max = 1e12

# positive cases:
analyst1 = np.random.choice(5, 150, p=[0.1, 0.05, 0.2, 0.3, 0.35]) + 1
analyst2 = np.random.choice(5, 150, p=[0.25, 0.075, 0.125, 0.25, 0.3]) + 1
analyst3 = np.random.choice(5, 150, p=[0.15, 0.1, 0.3, 0.2, 0.25]) + 1
sector = np.random.choice(sectors, 150, p=[0.35, 0.2, 0.2, 0.25])
market_cap1 = np.random.random_sample(35) * (mc_lower - mc_min) + mc_min
market_cap2 = np.random.random_sample(70) * (mc_upper - mc_lower) + mc_lower
market_cap3 = np.random.random_sample(45) * (mc_max - mc_upper) + mc_upper
market_cap = np.concatenate((market_cap1, market_cap2, market_cap3))
performance = np.ones(150)
df_pos = pd.DataFrame([analyst1, analyst2, analyst3, sector, \
                   market_cap, performance]).T
df_pos.columns = ['analyst1', 'analyst2', 'analyst3', 'sector', \
                   'market_cap', 'performance']

# neutral cases:
analyst1 = np.random.choice(5, 200, p=[0.15, 0.1, 0.3, 0.25, 0.2]) + 1
analyst2 = np.random.choice(5, 200, p=[0.25, 0.1, 0.25, 0.15, 0.25]) + 1
analyst3 = np.random.choice(5, 200, p=[0.15, 0.15, 0.35, 0.15, 0.2]) + 1
sector = np.random.choice(sectors, 200, p=[0.3, 0.25, 0.15, 0.3])
market_cap1 = np.random.random_sample(60) * (mc_lower - mc_min) + mc_min
market_cap2 = np.random.random_sample(90) * (mc_upper - mc_lower) + mc_lower
market_cap3 = np.random.random_sample(50) * (mc_max - mc_upper) + mc_upper
market_cap = np.concatenate((market_cap1, market_cap2, market_cap3))
performance = np.zeros(200)
df_neu = pd.DataFrame([analyst1, analyst2, analyst3, sector, \
                   market_cap, performance]).T
df_neu.columns = ['analyst1', 'analyst2', 'analyst3', 'sector', \
                   'market_cap', 'performance']

# negative cases:
analyst1 = np.random.choice(5, 160, p=[0.35, 0.15, 0.25, 0.1, 0.15]) + 1
analyst2 = np.random.choice(5, 160, p=[0.3, 0.15, 0.2, 0.15, 0.2]) + 1
analyst3 = np.random.choice(5, 160, p=[0.25, 0.2, 0.3, 0.1, 0.15]) + 1
sector = np.random.choice(sectors, 160, p=[0.25, 0.3, 0.3, 0.15])
market_cap1 = np.random.random_sample(65) * (mc_lower - mc_min) + mc_min
market_cap2 = np.random.random_sample(75) * (mc_upper - mc_lower) + mc_lower
market_cap3 = np.random.random_sample(20) * (mc_max - mc_upper) + mc_upper
market_cap = np.concatenate((market_cap1, market_cap2, market_cap3))
performance = -np.ones(160)
df_neg = pd.DataFrame([analyst1, analyst2, analyst3, sector, \
                   market_cap, performance]).T
df_neg.columns = ['analyst1', 'analyst2', 'analyst3', 'sector', \
                   'market_cap', 'performance']

# combine dataframe
df_combined = pd.concat([df_pos, df_neu, df_neg]).sample(frac=1).reset_index(drop=True)

# introduce missing values
nan_analyst1 = list(set(np.random.randint(0, df_combined.shape[0] - 1, 15)))
nan_analyst2 = list(set(np.random.randint(0, df_combined.shape[0] - 1, 30)))
nan_analyst3 = list(set(np.random.randint(0, df_combined.shape[0] - 1, 20)))
empty_sector = list(set(np.random.randint(0, df_combined.shape[0] - 1, 50)))
nan_market_cap = list(set(np.random.randint(0, df_combined.shape[0] - 1, 30)))
df_combined['analyst1'].iloc[nan_analyst1] = np.nan
df_combined['analyst2'].iloc[nan_analyst2] = np.nan
df_combined['analyst3'].iloc[nan_analyst3] = np.nan
df_combined['sector'].iloc[empty_sector] = ""
df_combined['market_cap'].iloc[nan_market_cap] = np.nan

df_combined.to_csv("market_data.csv", index=False)























