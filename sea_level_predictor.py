import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Data', color='blue')


    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)
    sea_level_extended = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_level_extended, label='Best Fit Line (All Data)', color='red')

    # Create second line of best fit
    data_recent = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)  # Only consider years from 2000 to 2050
    sea_level_extended_recent = [slope_recent * year + intercept_recent for year in years_recent]
    plt.plot(years_recent, sea_level_extended_recent, label='Best Fit Line (2000-2050)', color='green')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    plt.grid(True)
    
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__ == '__main__':
    draw_plot()
    plt.show()