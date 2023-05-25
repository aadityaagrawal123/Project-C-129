import pandas as pd

stars_data_file = pd.read_csv("stars_scraped_data.csv")

new_stars_datafile = stars_data_file.dropna()

new_stars_datafile["Radius"] = new_stars_datafile["Radius"].astype(float)
new_stars_datafile["Mass"] = new_stars_datafile["Mass"].astype(float)

new_stars_datafile["Radius"] = (new_stars_datafile["Radius"]*0.102763)
new_stars_datafile["Mass"] = (new_stars_datafile["Mass"]*0.000954588)

headers = ["Star_names", "Radius", "Mass", "Distance"]
new_stars_data_file = pd.DataFrame(new_stars_datafile, columns=headers)
new_stars_data_file.to_csv('dwarf_stars_data.csv', index=True, index_label="id")

dwarf_stars = pd.read_csv("brown_dwarfs_data.csv")
bright_stars = pd.read_csv("bright_stars_data.csv")

stars_merged_file = pd.merge(dwarf_stars, bright_stars, on="id")
stars_merged_file.to_csv("final_merged_stars.csv")
