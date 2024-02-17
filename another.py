import pygame
import os
from main import Country
current_path = os.path.dirname(__file__)
list_of_countries = []
for i in range(1, len(os.listdir(current_path + '/assets/countries/')) + 1):
    country_no = f"{i}"
    country = Country(country_no, f"killzone #{country_no}", pygame.image.load(current_path + f'/assets/countries/country{country_no}.png').convert_alpha(), None)
    list_of_countries.append(country)
    # update_progress_bar()

"""
list_of_countries[0].neighbours = [list_of_countries[1], list_of_countries[2], list_of_countries[3], list_of_countries[4]]
list_of_countries[1].neighbours = [list_of_countries[0], list_of_countries[2], list_of_countries[5]]
list_of_countries[2].neighbours = [list_of_countries[1], list_of_countries[3], list_of_countries[5]]
list_of_countries[3].neighbours = [list_of_countries[0], list_of_countries[2], list_of_countries[3], list_of_countries[4],list_of_countries[5]]
list_of_countries[4].neighbours = [list_of_countries[0], list_of_countries[3], list_of_countries[5]]
list_of_countries[5].neighbours = [list_of_countries[1], list_of_countries[2], list_of_countries[3], list_of_countries[4],list_of_countries[6], list_of_countries[7], list_of_countries[8], list_of_countries[9]]
list_of_countries[6].neighbours = [list_of_countries[5], list_of_countries[7]]
list_of_countries[7].neighbours = [list_of_countries[5], list_of_countries[6], list_of_countries[8]]
list_of_countries[8].neighbours = [list_of_countries[5], list_of_countries[7], list_of_countries[9], list_of_countries[10]]
list_of_countries[9].neighbours = [list_of_countries[5], list_of_countries[8], list_of_countries[10]]
list_of_countries[10].neighbours = [list_of_countries[8], list_of_countries[9]]
list_of_countries[11].neighbours = [list_of_countries[12]]
list_of_countries[12].neighbours = [list_of_countries[11], list_of_countries[13]]
list_of_countries[13].neighbours = [list_of_countries[12], list_of_countries[14], list_of_countries[15]]
list_of_countries[14].neighbours = []
list_of_countries[15].neighbours = []
list_of_countries[16].neighbours = []
"""

graph1 = {
    list_of_countries[0]: [list_of_countries[1], list_of_countries[2], list_of_countries[3], list_of_countries[4]],
    list_of_countries[1]: [list_of_countries[0], list_of_countries[2], list_of_countries[5]],
    list_of_countries[2]: [list_of_countries[1], list_of_countries[3], list_of_countries[5]],
    list_of_countries[3]: [list_of_countries[0], list_of_countries[2], list_of_countries[3], list_of_countries[4],list_of_countries[5]],
    list_of_countries[4]: [list_of_countries[0], list_of_countries[3], list_of_countries[5]],
    list_of_countries[5]: [list_of_countries[1], list_of_countries[2], list_of_countries[3], list_of_countries[4],list_of_countries[6], list_of_countries[7], list_of_countries[8], list_of_countries[9]],
    list_of_countries[6]: [list_of_countries[5], list_of_countries[7]],
    list_of_countries[7]: [list_of_countries[5], list_of_countries[6], list_of_countries[8]],
    list_of_countries[8]: [list_of_countries[5], list_of_countries[7], list_of_countries[9], list_of_countries[10]],
    list_of_countries[9]: [list_of_countries[5], list_of_countries[8], list_of_countries[10]],
    list_of_countries[10]: [list_of_countries[8], list_of_countries[9]],
    list_of_countries[11]: [list_of_countries[12]],
    list_of_countries[12]: [list_of_countries[11], list_of_countries[13]],
    list_of_countries[13]: [list_of_countries[12], list_of_countries[14], list_of_countries[15]],
    list_of_countries[14]: [list_of_countries[13], list_of_countries[15], list_of_countries[16]],
    list_of_countries[15]: [list_of_countries[13], list_of_countries[16], list_of_countries[17], list_of_countries[18]],
    list_of_countries[16]: [list_of_countries[14], list_of_countries[15], list_of_countries[18], list_of_countries[19]],
    


}