
# Filter a GeoDataFrame to a specific county
# Returns GeoDataFrame with filtered data
def filter_county(gdf, state_fp, county_fp):
    return gdf[
        (gdf["STATEFP"] == state_fp) &
        (gdf["COUNTYFP"] == county_fp)
    ].copy()