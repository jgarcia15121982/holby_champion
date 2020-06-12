#!/usr/bin/python3
"""class Base Champion"""



class BaseChampion():
    """base class for the Holbie Champion project"""

    __nb_objects = 0

    def __init__(self, id=0, name, race, gender, level, exp_nlvl, exp_cur, exp_tot, stats, stat_pts):
        """Initializes class BaseChampion"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        self.name = name
        self.race = race
        self.gender = gender
        self.level = level
        self.exp_nlvl = exp_nlvl
        self.exp_cur = exp_cur
        self.exp_tot = exp_tot
        self.stats = stats
        self.stat_pts = stat_pts
