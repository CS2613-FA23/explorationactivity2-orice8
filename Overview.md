# Overview
## 1. Which package or library did you select?
I selected the [Matplotlib Python Library](https://matplotlib.org/) with help from the [Pandas Python Library](https://pandas.pydata.org/docs/) for Exploration Activity 2.

## 2. What is the package or library?
### What purpose does it serve?
The purpose of the Matplotlib library is to provide tools that create static, animated, and interactive visuals in Python. According to the official [Matplotlib Website](https://matplotlib.org/):
> "A large number of third party packages extend and build on Matplotlib functionality, including several higher-level plotting interfaces (seaborn, HoloViews, ggplot, ...), and a projection and mapping toolkit (Cartopy)."

### How do you use it?
In my sample program I use it to plot and store previosuly calculated manipulations and calculations from star data. For example, I wanted to calculate the distance from the earth to different stars and then plot their locations based on earth's position, I had to get the [parallax distance](https://skyserver.sdss.org/dr1/en/proj/advanced/hr/hipparcos2.asp#:~:text=d%20%3D%201%2Fp%2C,parallax%20angle%20in%20arc%20seconds.) which uses parsec units, and then convert that distance to [light-years](https://skyserver.sdss.org/dr1/en/proj/advanced/hr/hipparcos2.asp#:~:text=d%20%3D%201%2Fp%2C,parallax%20angle%20in%20arc%20seconds.). In addition, I had to feed the data of multiple star data requests (using a dataframe) into a plotting function. The matplotlib package has many uses in data science and data manipulation sectors. I also used [this](https://gist.github.com/elnjensen/ce2367faf0d876def1ff68b6154e102b) tutorial to help me calculate some of the distances.

## 3. What are the functionalities of the package or library?
The [functionalities](https://matplotlib.org/stable/users/index) of the Matplotlib library includes:
### [Figures & Backends](https://matplotlib.org/stable/users/explain/figure/index.html)
  ```
  fig = plt.figure(figsize=(4, 2), facecolor='lightskyblue', layout='constrained')
  fig.suptitle('A nice Matplotlib Figure')
  ax = fig.add_subplot()
  ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')
  ```
  ![Screenshot (4)](https://github.com/CS2613-FA23/explorationactivity1-orice8/assets/114359587/0a9247c0-948d-4e46-be0a-0741aa3650e2)
### [Axes & Subplots](https://matplotlib.org/stable/users/explain/axes/index.html)
  ```
  import matplotlib.pyplot as plt
  import numpy as np
  
  fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(3.5, 2.5),
                          layout="constrained")
  # for each Axes, add an artist, in this case a nice label in the middle...
  for row in range(2):
      for col in range(2):
          axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                              transform=axs[row, col].transAxes,
                              ha='center', va='center', fontsize=18,
                              color='darkgrey')
  fig.suptitle('plt.subplots()')
  ```
  ![Screenshot (5)](https://github.com/CS2613-FA23/explorationactivity1-orice8/assets/114359587/dacf3f1e-d252-4dfb-bf88-6df4e0ee4aec)
### [Artists](https://matplotlib.org/stable/users/explain/artists/index.html)
Artists are subclasses of the artist class and generally contain data or information. Pretty much everything oyu interact with in this library is an Artist of some kind.
```
  import matplotlib.pyplot as plt
  import matplotlib.artist as martist
  import numpy as np

  fig, ax = plt.subplots()
  x, y = np.random.rand(2, 100)
  lines = ax.plot(x, y, '-', label='example')
  print(lines)
  ```
 "plot" would be the artist in this scenario.
### [Customizing Style Sheets and Runtime Configuration Parameters](https://matplotlib.org/stable/users/explain/customizing.html)
  ```
  from cycler import cycler
  import matplotlib.pyplot as plt
  import numpy as np
  import matplotlib as mpl
  
  mpl.rcParams['lines.linewidth'] = 2
  mpl.rcParams['lines.linestyle'] = '--'
  data = np.random.randn(50)
  plt.plot(data)
  ```
 rcParams are being changed in this scenario.
### [Colors](https://matplotlib.org/stable/users/explain/colors/index.html)
According to the official documentation for matplotlib, the library has support for a wide array of colors and colormaps. 

### [Text](https://matplotlib.org/stable/users/explain/text/index.html)
According to the official documentation for matplotlib, the library has support for mathematical expressions, rasters & vectors, newline seperated text, and unicode. 

### [Animations](https://matplotlib.org/stable/users/explain/animations/index.html)
According to the official documentation for matplotlib, the library has support for animation generation which demonstrates data over time in a sequence of frames. 

## 4. When was it created?
Matplotlib was [initially released](https://commons.wikimedia.org/wiki/File:Created_with_Matplotlib-logo.svg) in 2003.

## 5. Why did you select this package or library?
I selected this library because I wanted people to use my original code for querying star data to be visualized. I wanted to learn about some of the ways distances between celestial bodies could be shown given the many variables given for each star from the Simbad database. This exploration activity also gave me the chance to research some variables I may have missed in my intial exploration.
  
## 6. How did learning the package or library influence your learning of the language?
This package taught me to plot data and use data frames instead of timeseries. In addition, I also learned how to use and read "dataframe" data on a single program run basis. 

## 7. How was your overall experience with the package/library?
### When would you recommend this package or library to someone?
As previously stated, I would recommend this library to someone working in data science or a quick way to visualize data. 

### Would you continue using this package or library? Why or why not?
I would continue using this package. I think the library could come in handy for live sensor readings (I have a project this term in a class that has a similar requirement).
