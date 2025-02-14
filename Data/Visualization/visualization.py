from . import visual_helper
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
        plot = visual_helper.line_bar_plot(x, y, title='Conflict Events Fatalities Trend', y_label='Fatalities Count')
    return plot


def plot_funding(country_data):
    """
    Plots the funding trend
    """
    if not country_data.funding_data:
        country_data.get_funding_data()
    df = country_data.funding_data

    # Add a column of year
    df['reference_period_start'] = pd.to_datetime(df['reference_period_start'])
    df['year'] = df['reference_period_start'].dt.year

    # Plot a bar and line plot, where x-axis is year, and y-axis is funding received
    funding_per_year = df.groupby('year')['funding_usd'].sum().reset_index()
    x = funding_per_year['year']
    y = funding_per_year['funding_usd']
    plot = visual_helper.line_bar_plot(x, y, title='Funding Trend', y_label='Amount (billion USD)', unit='billion',save_path='./funding')
    return plot

def plot_population(country_data):
    if not country_data.population_data:
        country_data.get_population_data()
    df = country_data.population_data

    df = df[df['age_range'] !='all']
    
    def merge_age_range(age):
        try:
            if age == '80+':
                return '60+'
            start_age = int(age.split('-')[0])
            if start_age >= 60 :
                return '60+'
            else:
                return age
        except ValueError:
            return age

    df.loc[:, 'age_range'] = df['age_range'].apply(merge_age_range)
    # print(df.columns)
    
    aggregated_data = df.groupby('age_range', as_index=False)['population'].sum()
    # print(aggregated_data)

    data = aggregated_data['population'].values 
    labels = aggregated_data['age_range'].values

    plot = visual_helper.pie_chart(data, labels, title='Population age range in AFG',save_path='./population')
    return plot

def plot_events(country_data):
    """
    Process data for bar chart.

    :param country_data: DataFrame containing the data
    :return: processed x and y data for plotting
    """
    # Optional data filtering based on condition
    if not country_data.conflict_event_data:
        country_data.get_conflict_event_data()
    df = country_data.conflict_event_data

    df['reference_period_start'] = pd.to_datetime(df['reference_period_start'])
    df['year'] = df['reference_period_start'].dt.year
    
    # Group by 'year' and 'admin1_name' and sum the 'events'
    aggregated_data = df.groupby(['year', 'admin1_name'])['events'].sum().unstack(fill_value=0)

    # Call bar_chart for visualization
    plot = visual_helper.bar_chart(aggregated_data, 
                     title="Conflict Events Over Years in AFG", 
                     x_label="Year", 
                     y_label="Number of Events", 
                     save_path='./conflict_events2', 
                     color='skyblue', 
                     alpha=0.7, 
                     stacked=False)
    
    return plot