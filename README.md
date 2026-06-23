# Network-Based Grocery Store Accessibility Analysis 

## Project Overview
This project evaluates grocery store accessibility across Kootenai County, Idaho using road-network analysis. Grocery store locations were collected from OpenStreetMap (OSM), cleaned, standardized, and analyzed using Python and GIS tools. Drive-time service areas representing 10-, 20-, and 30-minute travel times were generated for each grocery store using a road-network model.

The project provides both static and interactive visualizations to examine grocery access across the county, compare coverage among grocery chains, and identify areas with limited access to food retail services. 


## Study Area
Kootenai County is located in northern Idaho and contains a mix of urban, suburban, and rural communities. Accessibility to grocery stores varies considerably across the county due to differences in population density, transportation infrastructure, and store distribution.


## Objectives 
- Identify grocery store locations throughout Kootenai County
- Build a road-network model from OpenStreetMap data
- Generate 10-, 20-, and 30-minute drive-time service areas
- Compare accessibility among major grocery chains
- Explore geographic areas with limited grocery access
- Develop interactive tools for accessibility exploration


## Data Sources
| Dataset              | Source                             |
| -------------------- | ---------------------------------- |
| Grocery Stores       | OpenStreetMap                      |
| Road Network         | OpenStreetMap                      |
| City Boundaries      | Census Cartographic Boundary Files |
| County Census Tracts | Census Cartographic Boundary Files |


## Methodology

### Step 1: Store Collection and Cleaning
Grocery store locations were downloaded from OpenStreetMap using OSMnx. The dataset was reviewed to remove duplicate records, verify store classifications, and standardize store names.

store table + store map

### Step 2: Network Preparation
A drivable road network was downloaded from OpenStreetMap and converted into a graph structure suitable for network analysis. Each grocery store was connected to the nearest network node to enable travel-time calculations.

nearest node figure 

### Step 3: Service Area Generation
For each grocery store, network-based service areas representing 10-, 20-, and 30-minute driving times were generated. These service areas estimate the geographic extent reachable within each travel-time threshold using the road network.

single store 10/20/30 minute maps

## Results

### Countywide Coverage
Service areas from all grocery stores were combined to evaluate overall grocery accessibility throughout Kootenai County.

all stores 10/20/30 minute maps

### Grocery Chain Comparision
Accessibility patterns were compared between major grocery chains to evaluate differences in service coverage and geographic reach. Results illustrate how store location strategies influence accessibility and market coverage.

Warlmart vs Super One Food 

### Interactive Exploration
An interactive dashboard was developed using Jupyter widgets, allowing users to:

Select individual stores
Select multiple stores simultaneously
Toggle between 10-, 20-, and 30-minute service areas
Explore accessibility patterns dynamically

widget GIF

## Technologies Used
- Python
- Jupyter Notebook
- Git
- Pandas
- GeoPandas
- OSMnx
- Shapely
- Matplotlib
- ipywidgets

## Repository Structure
```
grocery_stores_access/
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│
├── outputs/
│
├── src/
│
├── README.md
└── requirements.txt
```
    

## Future Improvements
- Use actual speed-limit data
- Incorporate population and demographic data to identify underserved areas
- Compare accessbility changes over time
- Deploy as a Streamlit web application 




## Key Skills Demonstrated
- Python-based GIS workflows
- GIS and spatial analysis
- Network analysis
- OpenStreetMap data acquisition, cleaning and standardization
- Geospatial data processing
- Accessibility modeling
- Interactive visualization development
- Cartographic design