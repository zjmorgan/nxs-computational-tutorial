
import glob
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Find all files starting with 'data' and ending with '.csv'
file_list = glob.glob('data*.csv')

for file_path in file_list:
    # Read the data from the CSV file
    data = pd.read_csv(file_path)
    x = data['x']
    y = data['y']

    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    r_squared = r_value**2

    # Create the plot
    plt.figure()
    plt.scatter(x, y, label='Data')
    plt.plot(x, intercept + slope*x, 'r', label='Fitted line')

    # Add R-squared value to the plot
    plt.text(0.05, 0.95, f'$R^2 = {r_squared:.2f}$', transform=plt.gca().transAxes,
             fontsize=12, verticalalignment='top')

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Linear Fit for {file_path}')
    plt.legend()

    # Save the plot to a file
    output_filename = file_path.replace('.csv', '.png')
    plt.savefig(output_filename)
    plt.close()

print(f"Processed {len(file_list)} files and saved the plots.")
