# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 08:15:33 2023

@author: agdtu
"""
import random
import time

def timer(func):
    """
    Get the run time of the decorated function.
    

    Parameters
    ----------
    func : The function to be timed.
        DESCRIPTION.

    Returns
    -------
    Tuple
        The run time then func output.
    """
    def inner_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        run_time = time.perf_counter() - start
        return run_time, value
    return inner_timer

@timer
def create_agents(n_agents):
    """
    A function to create a list of agents. The decorator will print the time
    it takes to run this function.

    Parameters
    ----------
    n_agents : Integer
        The number of agents to create.

    Returns
    -------
    agents : List
        A list of the created agents.

    """
    agents = []
    for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])
    return agents

# Create agents
n_agents = 1000000
run_time, agents = create_agents(n_agents)
print(run_time, "seconds to create", n_agents, "agents.")