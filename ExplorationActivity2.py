from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord, get_icrs_coordinates
from astropy.coordinates.name_resolve import NameResolveError
import astropy.units as u
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

def get_star_info(s_StarName):
    Simbad.add_votable_fields('main_id', 'plx', 'distance') 

    try:
        coordinates = SkyCoord.from_name(s_StarName)
    except NameResolveError as e:
        print("NameResolveError:", e)
        coordinates = None

    try:
        coords = get_icrs_coordinates(s_StarName)
        coords_str = f"Right Ascension: {coords.ra.deg}, Declination: {coords.dec.deg}"
    except NameResolveError as e:
        print("NameResolveError:", e)
        coords = None
        coords_str = None

    try:
        star_info = Simbad.query_object(s_StarName)
    except NameResolveError as e:
        print("NameResolveError:", e)
        star_info = None 

    print(f"\n{s_StarName}:") 
    print(f"Coordinates: {coords_str}")

    try:
        if star_info is not None:
            if not star_info['PLX_VALUE'].mask[0]:
                print("Distance from earth is {:0.1f} lightyears.".format((1000./star_info['PLX_VALUE'][0]) * 3.262)) 
            else: 
                print("No distance available in Simbad.")
        else:
            print("Unable to resolve astronomical coordinates for the given name.\n")
    except NameResolveError as e:
        print("NameResolveError:", e)

    try:
      if star_info is not None:
          if not star_info['MAIN_ID'].mask[0]:  
              print(f"Main Identifier: {star_info['MAIN_ID'][0]}")  
          else:
              print("No ID available in Simbad.")
      else:
          print("Unable to resolve main identifier for the given name.\n")
    except NameResolveError as e:
      print("NameResolveError:", e)

    star_data = {
        'Name': s_StarName,
        'Right_Asc': coords.ra.deg if coords is not None else None,
        'Dec': coords.dec.deg if coords is not None else None,
        'Distance': (
            (1000. / star_info['PLX_VALUE'][0]) * 3.262
            if star_info is not None and not star_info['PLX_VALUE'].mask[0]
            else None
        ),
        'Main_ID': star_info['MAIN_ID'][0] if star_info is not None and not star_info['MAIN_ID'].mask[0] else None
    }
    return star_data

def plot_star_positions(star_data):
    if not star_data.empty:
        f_EarthRA = 0.0
        f_EarthDec = 0.0
        fig, ax = plt.subplots(figsize=(8, 6))

        for index, row in star_data.iterrows():
            x = row['Right_Asc']
            y = row['Dec']
            ax.scatter(x, y, marker='*', s=100, label=row['Name'])

        ax.scatter(f_EarthRA, f_EarthDec, marker='o', s=200, c='Blue', label='Earth')
        ax.set_xlabel('Right Ascension (degrees)')
        ax.set_ylabel('Declination (degrees)')
        ax.set_title('Star Positions Relative to Earth')
        ax.legend()
        ax.grid(True)
        plt.show()
    else:
        print("No star data available for plotting.")

def main():
    df_StarData = pd.DataFrame(columns=['Name', 'Right_Asc', 'Dec', 'Distance', 'Main_ID']) 

    while True:
        s_UserInput = input("\nPick an option:\n1. Get new star data\n2. Print star data\n3. Plot stars relative to earth\n4. Quit program\n")

        if s_UserInput == '1':
            star_name = input("\nEnter the name of a star (use underscores if the name has spaces): ")
            star_data = get_star_info(star_name)

            if star_data:
                df_StarData = pd.concat([df_StarData, pd.DataFrame([star_data])], ignore_index=True)
        
        elif s_UserInput == '2':
            if not df_StarData.empty:
                print("All Star Data:")
                print(df_StarData.to_string(index=False) + "\n")
            else:
                print("No star data available.\n")

        elif s_UserInput == '3':
            plot_star_positions(df_StarData)
        
        elif s_UserInput == '4':
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4. \n")

if __name__ == "__main__":
    main()