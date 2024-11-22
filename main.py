from Data.HAPI.hapi_class import HapiClass
import Data.Visualization.visualization as visual
import Card_Generation.card_generation as cg


# Example
country = "AFG"
country_data = HapiClass(country)
# plot1 = visual.plot_humanitarian_needs(country_data)
# plot2 = visual.plot_conflict_events(country_data)
plot3 = visual.plot_funding(country_data)
plots = [plot3]
title = "AFG Humanitarian Crisis"
description = "asidjgviasnvboawh4ugaopjsj gapisjdgoiahsiohga[osdhiuno saoifhopeuhgiuadfiovuoziuhdcv aspodaouipshvu"

# cg.create_card(plots, title, description)