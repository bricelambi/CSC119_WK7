
import pandas as pd

"""
  Exercise 0:
  Create a class that will be used for storing the data we
  read in from the CSV file.  The constructor should take
  one argument that is the csv filename to read
"""

"""
  Exercise 0.1:
  Extend the class defintion to have a function that will read
  the CSV data from the file provided to the constructor
"""

"""
  Exercise 0.2:
  Create an instance of the class and call the load_csv_data function
"""

#Exercise 0
class WeatherData:
  def __init__(self, filename):
    self.filename = filename #set the argument to the constructor on self so it will be saved for later use

  #Exercise 0.1
  def load_csv_data(self):
    self.data = pd.read_csv(self.filename)


#Exercise 0.2
weatherData = WeatherData('US_points_hourly_CST.csv')
weatherData.load_cst_data()
