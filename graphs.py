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

graph = {
    list_of_countries[0]: [list_of_countries[1], list_of_countries[2], list_of_countries[36]],
    list_of_countries[1]: [list_of_countries[0], list_of_countries[2], list_of_countries[3], list_of_countries[8]],
    list_of_countries[2]: [list_of_countries[0], list_of_countries[1], list_of_countries[3], list_of_countries[5]],
    list_of_countries[3]: [list_of_countries[1], list_of_countries[2], list_of_countries[4], list_of_countries[5], list_of_countries[6], list_of_countries[8]],
    list_of_countries[4]: [list_of_countries[3], list_of_countries[6], list_of_countries[8]],
    list_of_countries[5]: [list_of_countries[2], list_of_countries[3], list_of_countries[6], list_of_countries[7]],
    list_of_countries[6]: [list_of_countries[3], list_of_countries[4], list_of_countries[5], list_of_countries[7]],
    list_of_countries[7]: [list_of_countries[5], list_of_countries[6], list_of_countries[9]],
    list_of_countries[8]: [list_of_countries[1], list_of_countries[3], list_of_countries[4], list_of_countries[13]],
    list_of_countries[9]: [list_of_countries[7], list_of_countries[10], list_of_countries[11]],
    list_of_countries[10]: [list_of_countries[9], list_of_countries[11], list_of_countries[20]],
    list_of_countries[11]: [list_of_countries[9], list_of_countries[10], list_of_countries[12]],
    list_of_countries[12]: [list_of_countries[10], list_of_countries[11]],
    list_of_countries[13]: [list_of_countries[8], list_of_countries[14], list_of_countries[15]],
    list_of_countries[14]: [list_of_countries[13], list_of_countries[15], list_of_countries[17], list_of_countries[18]],
    list_of_countries[15]: [list_of_countries[13], list_of_countries[14], list_of_countries[16], list_of_countries[17]],
    list_of_countries[16]: [list_of_countries[15], list_of_countries[17], list_of_countries[19], list_of_countries[26], list_of_countries[27], list_of_countries[28]],
    list_of_countries[17]: [list_of_countries[14], list_of_countries[15], list_of_countries[16], list_of_countries[18], list_of_countries[19]],
    list_of_countries[18]: [list_of_countries[14], list_of_countries[17], list_of_countries[19], list_of_countries[20]],
    list_of_countries[19]: [list_of_countries[16], list_of_countries[17], list_of_countries[18], list_of_countries[21], list_of_countries[28]],
    list_of_countries[20]: [list_of_countries[10], list_of_countries[18], list_of_countries[21], list_of_countries[22], list_of_countries[23]],
    list_of_countries[21]: [list_of_countries[19], list_of_countries[20], list_of_countries[22], list_of_countries[28]],
    list_of_countries[22]: [list_of_countries[20], list_of_countries[21], list_of_countries[23], list_of_countries[25], list_of_countries[28]],
    list_of_countries[23]: [list_of_countries[20], list_of_countries[22], list_of_countries[24]],
    list_of_countries[24]: [list_of_countries[22], list_of_countries[23], list_of_countries[25]],
    list_of_countries[25]: [list_of_countries[22], list_of_countries[24]],
    list_of_countries[26]: [list_of_countries[16], list_of_countries[27], list_of_countries[31], list_of_countries[33]],
    list_of_countries[27]: [list_of_countries[16], list_of_countries[26], list_of_countries[28], list_of_countries[29], list_of_countries[31]],
    list_of_countries[28]: [list_of_countries[16], list_of_countries[19], list_of_countries[21], list_of_countries[22], list_of_countries[27], list_of_countries[29]],
    list_of_countries[29]: [list_of_countries[27], list_of_countries[28], list_of_countries[30], list_of_countries[31]],
    list_of_countries[30]: [list_of_countries[29], list_of_countries[31], list_of_countries[40]],
    list_of_countries[31]: [list_of_countries[26], list_of_countries[27], list_of_countries[29], list_of_countries[30], list_of_countries[32], list_of_countries[33]],
    list_of_countries[32]: [list_of_countries[31], list_of_countries[33], list_of_countries[34], list_of_countries[38], list_of_countries[39]],
    list_of_countries[33]: [list_of_countries[26], list_of_countries[31], list_of_countries[32], list_of_countries[34], list_of_countries[35]],
    list_of_countries[34]: [list_of_countries[32], list_of_countries[33], list_of_countries[35], list_of_countries[37], list_of_countries[38]],
    list_of_countries[35]: [list_of_countries[33], list_of_countries[34], list_of_countries[36], list_of_countries[37]],
    list_of_countries[36]: [list_of_countries[0], list_of_countries[35], list_of_countries[37]],
    list_of_countries[37]: [list_of_countries[34], list_of_countries[35], list_of_countries[38]],
    list_of_countries[38]: [list_of_countries[32], list_of_countries[34], list_of_countries[37], list_of_countries[39]],
    list_of_countries[39]: [list_of_countries[32], list_of_countries[38]],
    list_of_countries[40]: [list_of_countries[30], list_of_countries[41]],
    list_of_countries[41]: [list_of_countries[40], list_of_countries[42], list_of_countries[43]],
    list_of_countries[42]: [list_of_countries[41], list_of_countries[43]],
    list_of_countries[43]: [list_of_countries[41], list_of_countries[42]]
}

graph = {
    list_of_countries[0]: [list_of_countries[1], list_of_countries[2], list_of_countries[3], list_of_countries[4]],
    list_of_countries[1]: [list_of_countries[0], list_of_countries[2], list_of_countries[5]],
    list_of_countries[2]: [list_of_countries[0], list_of_countries[1], list_of_countries[3], list_of_countries[5]],
    list_of_countries[3]: [list_of_countries[0], list_of_countries[2], list_of_countries[4], list_of_countries[5]],
    list_of_countries[4]: [list_of_countries[0], list_of_countries[3], list_of_countries[5], list_of_countries[17]],
    list_of_countries[5]: [list_of_countries[1], list_of_countries[2], list_of_countries[3], list_of_countries[4], list_of_countries[6], list_of_countries[7], list_of_countries[8], list_of_countries[9]],
    list_of_countries[6]: [list_of_countries[5], list_of_countries[7]],
    list_of_countries[7]: [list_of_countries[5], list_of_countries[6], list_of_countries[8], list_of_countries[20]],
    list_of_countries[8]: [list_of_countries[5], list_of_countries[7], list_of_countries[9], list_of_countries[10]],
    list_of_countries[9]: [list_of_countries[5], list_of_countries[8], list_of_countries[10]],
    list_of_countries[10]: [list_of_countries[8], list_of_countries[9], list_of_countries[24]],
    list_of_countries[11]: [list_of_countries[12]],
    list_of_countries[12]: [list_of_countries[11], list_of_countries[13]],
    list_of_countries[13]: [list_of_countries[12], list_of_countries[14], list_of_countries[15]],
    list_of_countries[14]: [list_of_countries[13], list_of_countries[15], list_of_countries[16]],
    list_of_countries[15]: [list_of_countries[13], list_of_countries[14], list_of_countries[16], list_of_countries[17], list_of_countries[18]],
    list_of_countries[16]: [list_of_countries[14], list_of_countries[15], list_of_countries[18], list_of_countries[19]],
    list_of_countries[17]: [list_of_countries[4], list_of_countries[15], list_of_countries[18]],
    list_of_countries[18]: [list_of_countries[15], list_of_countries[16], list_of_countries[17], list_of_countries[19], list_of_countries[24]],
    list_of_countries[19]: [list_of_countries[16], list_of_countries[18], list_of_countries[26]],
    list_of_countries[20]: [list_of_countries[7], list_of_countries[21]],
    list_of_countries[21]: [list_of_countries[20], list_of_countries[22]],
    list_of_countries[22]: [list_of_countries[21], list_of_countries[23], list_of_countries[24]],
    list_of_countries[23]: [list_of_countries[22], list_of_countries[24], list_of_countries[26]],
    list_of_countries[24]: [list_of_countries[10], list_of_countries[18], list_of_countries[22], list_of_countries[23]],
    list_of_countries[25]: [list_of_countries[26]],
    list_of_countries[26]: [list_of_countries[19], list_of_countries[23], list_of_countries[25]]
}