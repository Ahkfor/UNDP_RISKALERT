import Visualization.visualization as vis
from HAPI.hapi_class import HapiClass


# Example
country = "AFG"
country_data = HapiClass(country)
# visualization.plot_humanitarian_needs(country_data).show()
# visualization.plot_conflict_events(country_data).show()
# vis.plot_funding(country_data)
# vis.plot_population(country_data)
vis.plot_events(country_data)
