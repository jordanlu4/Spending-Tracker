import csv
from datetime import datetime
from typing import List, Dict


class Budget:
    def __init__(self, budget: float): #Set a budget
        self.budget = budget
