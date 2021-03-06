import json
import pygal
from pygal.style import RotateStyle as RS
from pygal.style import LightColorizedStyle as LCS
from countries import get_country_code

# Load the data into a list.
filename = 'Data_Visualization/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}
# Print the 2010 population for each country.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(country_name + ': ' + str(population))
            cc_populations[code] = population
        else:
            print('ERROR - ' + country_name)


# Group the countries into 3 popilation levels.
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

# See how many countries are in each level
print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))


wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('Data_Visualization/world_populations.svg')
