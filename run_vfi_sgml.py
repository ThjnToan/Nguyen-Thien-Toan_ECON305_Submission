"""

run_vfi_sgml.py
--------------
This code solves the stochastic growth model using value function iteration.

"""

#%% Import from Python and set project directory

import os
os.chdir('C:\\Users\\Laptop K1\\Downloads\\Stochastic_Growth_with_Labor_export\\Python')
main = os.getcwd()
figout = main+"\\output\\figures"

# Ensure the output directory exists
os.makedirs(figout, exist_ok=True)

#%% Import from folder
from model import planner
from solve import plan_allocations
from simulate import grow_economy
from my_graph import track_growth

#%% Stochastic Growth Model.
benevolent_dictator = planner()

# Set the parameters, state space, and utility function.
benevolent_dictator.setup(main=main, figout=figout, beta=0.96, sigma=2.00, policy_g=0.05)  # Increase technology growth rate by 5%

# Solve the model.
plan_allocations(benevolent_dictator) # Obtain the policy functions for capital.

# Simulate the model.
grow_economy(benevolent_dictator) # Simulate forward in time.

# Graphs.
track_growth(benevolent_dictator) # Plot policy functions and simulations.
