import Visualization.visualization as vis
from HAPI.hapi_class import HapiClass

class HAPIVisualizer:
    HAPI_columns = [
        'Humanitarian Need',
        'Refugee',
        'Returnee',
        'Operational Presence',
        'Funding',
        'Conflict Event',
        'National Risk',
        'Food Price',
        'Food Security',
        'Population',
        'Poverty Rate'
    ]
    def __init__(self, country, columns, output_number):
        self.columns = columns
        self.country_data = HapiClass(country)
        self.output_number = output_number
        
    def generate_plots(self):
        for col in self.columns:
            if col not in self.HAPI_columns:
                raise ValueError("Invalid Column Name!")
            if col == 'Humanitarian Need':
                plot = vis.plot_humanitarian_needs(self.country_data)
            
            elif col == "Refugee":
                pass
            
            elif col == 'Returnee':
                pass
            
            elif col == 'Operational Presence':
                pass
            
            elif col == 'Funding':
                plot = vis.plot_funding(self.country_data)
                
            elif col == 'Conflict Event':
                plot = vis.plot_events(self.country_data)
                
            elif col == 'Food Price':
                pass
            
            elif col == 'Food Security':
                pass
            
            elif col == 'Population':
                plot = vis.plot_population(self.country_data)
                
            elif col == 'Poverty Rate':
                plot = vis.plot