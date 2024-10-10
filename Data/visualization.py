from HAPI.hapi_class import HapiClass
import visual_helper
import pandas as pd


def plot_humanitarian_needs(country_data):
    '''
    This function will plot the trend of humanitarian needs for a given country, takes HapiClass object as input
    :param country_data: a HapiClass object
    :return: None
    '''

    # In case the object has not obtained humanitarian data
    if not country_data.humanitarian_data:
        country_data.get_humanitarian_needs_data()

    df = country_data.humanitarian_data
    intersector_df = df[df['sector_name']=='Intersectoral']

    # Find population in need
    intersector_df = intersector_df[intersector_df['population_status']=='INN']

    # Disregard Whether refugee or not
    intersector_df = intersector_df[intersector_df['population_group']=='all']

    # Disregard Age
    intersector_df = intersector_df[intersector_df['age_range'] == 'ALL']

    # Disregard Disabled
    intersector_df = intersector_df[intersector_df['disabled_marker'] == 'all']

    # Visualization currently unavailable (Not time series data, only 2024)
    pass


def plot_conflict_events(country_data, event_type='all'):
    """
    This function will plot the conflict events for a given country, takes HapiClass object as input
    :param country_data: a HapiClass object
    :return: None
    """
    # Retrieve Data
    if not country_data.conflict_event_data:
        country_data.get_conflict_event_data()
    df = country_data.conflict_event_data

    # Add a column of year
    df['reference_period_start'] = pd.to_datetime(df['reference_period_start'])
    df['year'] = df['reference_period_start'].dt.year

    # Plot
    if event_type == 'all':
        # Create bar and line plot
        events_per_year = df.groupby('year')['events'].sum().reset_index()
        x = events_per_year['year']
        y = events_per_year['events']
        visual_helper.line_bar_plot(x, y, title='Conflict Events Count Trend', y_label='Event Count')
        casualties_per_year = df.groupby('year')['fatalities'].sum().reset_index()
        x = casualties_per_year['year']
        y = casualties_per_year['fatalities']
        visual_helper.line_bar_plot(x, y, title='Conflict Events Fatalities Trend', y_label='Fatalities Count')

