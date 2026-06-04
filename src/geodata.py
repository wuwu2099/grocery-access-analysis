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

    # 1. CRS (IMPORTANT: must assign back)
    gdf = gdf.to_crs(target_crs)

    # 2. Clean geometry
    gdf = gdf[gdf.geometry.notna()].copy()

    # 3. Convert to point representation (centroid)
    gdf["geometry"] = gdf.geometry.centroid

    # 4. Coordinates (optional but fine)
    # gdf["x"] = gdf.geometry.x
    # gdf["y"] = gdf.geometry.y

    # 5. Initialize
    gdf["nearest_same_name_m"] = pd.NA

    # 6. Group-based distance search
    for name, group in gdf.groupby("name"):
        if len(group) < 2:
            continue

        for idx in group.index:
            current_geom = gdf.loc[idx, "geometry"]
            others = group.drop(index=idx)

            distances = others.geometry.distance(current_geom)

            gdf.loc[idx, "nearest_same_name_m"] = distances.min()

    # 7. FIXED: boolean condition (this was correct now)
    gdf["is_duplicate"] = gdf["nearest_same_name_m"] < distance_threshold

    # 8. review table
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

        
