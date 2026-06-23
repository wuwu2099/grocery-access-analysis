import geopandas as gpd
import pandas as pd 


# Filter a GeoDataFrame to a specific county
# Returns GeoDataFrame with filtered data
def filter_county(gdf, state_fp, county_fp):
    return gdf[
        (gdf["STATEFP"] == state_fp) &
        (gdf["COUNTYFP"] == county_fp)
    ].copy()



# Identify potential duplicate stores using: name and distance
# Return a DataFrame of review table for potential duplicates
def find_possible_duplicates(stores_gdf, distance_threshold=50, target_crs=26911):

    gdf = stores_gdf.copy()
    gdf = gdf.to_crs(target_crs)
    gdf = gdf[gdf.geometry.notna()].copy()

    # Convert to point representation (centroid)
    gdf["geometry"] = gdf.geometry.centroid

    gdf["nearest_same_name_m"] = pd.NA

    # Group-based distance search
    for name, group in gdf.groupby("name"):
        if len(group) < 2:
            continue
        for idx in group.index:
            current_geom = gdf.loc[idx, "geometry"]
            others = group.drop(index=idx)

            distances = others.geometry.distance(current_geom)

            gdf.loc[idx, "nearest_same_name_m"] = distances.min()

    # boolean condition 
    gdf["is_duplicate"] = gdf["nearest_same_name_m"] < distance_threshold

    review_cols = [
        col for col in [
            "name",
            "addr:city",
            "addr:street",
            "geometry",
            "nearest_same_name_m",
            "is_duplicate"
        ]
        if col in gdf.columns
    ]

    review_table = (
        gdf[gdf["nearest_same_name_m"].notna()]
        .sort_values("nearest_same_name_m")
        [review_cols]
    )

    return review_table



# Clean store data,
# after reviewing manually 
def clean_grocery_stores(stores_gdf):
    gdf = stores_gdf.copy()

    # Remove bad records
    exclude_names = [
        "Lake Village Farmers Market",
        "Luxury Homes | North Idaho"
    ]
    gdf = gdf[~gdf["name"].isin(exclude_names)]

    # Standardize names
    gdf.loc[
        gdf["name"] == "Super 1 Foods",
        "name"
    ] = "Super One Foods"

    gdf.loc[
        gdf["name"] == "Super 1 Foods Rathdrum",
        ["name", "addr:city"]
    ] = [
        "Super One Foods",
        "Rathdrum"
    ]

    gdf.loc[
        gdf["name"] == "Super One Foods - Athol",
        ["name", "addr:city"]
    ] = [
        "Super One Foods",
        "Athol"
    ]

    return gdf