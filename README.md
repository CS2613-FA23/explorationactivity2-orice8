# Exploration Activity 2
Language: Python
<br>Library: AstroPy, Pandas, Matplotlib

## Which package or library does the sample program demonstrate?
This sample program demonstrates the AstroPy python library with the help of AstroQuery which allows access to online databases (sample data). This program takes user input to get star data for as many stars as requested, gives their information and has the ability to plot their position relative to the earth using Matplotlib.

## How does someone run your program? 
To run this program ensure that AstroQuery is installed. In VSCode this can be done by opening a new powershell terminal and typing: <i>pip install [package_name]</i>. For this exercise run the following:
```
pip install astroquery
pip install astropy
pip install pandas
pip install matplotlib
pip install numpy
```

## What purpose does your program serve?
My program's purposes is to demonstrate data calculation, plotting, data organization/manipulation, and coordinate capabilities of the AstroPy, Matplotlib, and Pandas Libraries in Python. In particular, this program can return data when given the name of a star, a full list of all star data from the current program run, and a plot of star positions relative to the earth.

## What would be some sample input/output?
### Example
```
Pick an option:
1. Get new star data
2. Print star data
3. Plot stars relative to earth
4. Quit program
1

Enter the name of a star (use underscores if the name has spaces): Rigel

Rigel:
Coordinates: Right Ascension: 78.634467067, Declination: -8.201638365
Distance from earth is 863.0 lightyears.
Main Identifier: * bet Ori

Pick an option:
1. Get new star data
2. Print star data
3. Plot stars relative to earth
4. Quit program
1

Enter the name of a star (use underscores if the name has spaces): Betelgeuse

Betelgeuse:
Coordinates: Right Ascension: 88.792938991, Declination: 7.407063995
Distance from earth is 498.0 lightyears.
Main Identifier: * alf Ori

Pick an option:
1. Get new star data
2. Print star data
3. Plot stars relative to earth
4. Quit program
3
Output:
```
![Screenshot (3)](https://github.com/CS2613-FA23/explorationactivity2-orice8/assets/114359587/13740265-68ba-431b-9a87-10e5bf79078e)

```
Pick an option:
1. Get new star data
2. Print star data
3. Plot stars relative to earth
4. Quit program
4
```
