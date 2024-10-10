import visualization
from HAPI.hapi_class import HapiClass


# Example
country = "AFG"
country_data = HapiClass(country)
# visualization.plot_humanitarian_needs(country_data)
# visualization.plot_conflict_events(country_data)
visualization.plot_funding(country_data)