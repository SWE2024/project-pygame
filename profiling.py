import cProfile
import pygame
import os
from pygame import mixer;

def main():
    """
    Enter the game code here
    """

"""
Runs the profiler in the background, you can 
sort the results by following this guide:
https://docs.python.org/2/library/profile.html#pstats.Stats.sort_stats
"""
cProfile.run('main()', sort = 'cumulative')

"""
Example profile:
Ordered by: primitive call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     7126    0.001    0.000    0.001    0.000 {method 'get_width' of 'pygame.surface.Surface' objects}
     5818    1.049    0.000    1.049    0.000 {method 'blit' of 'pygame.surface.Surface' objects}
     4748    0.001    0.000    0.001    0.000 {method 'lower' of 'str' objects}
     4402    0.001    0.000    0.002    0.000 sysfont.py:45(<genexpr>)
     4053    0.000    0.000    0.000    0.000 {method 'isalnum' of 'str' objects}
"""