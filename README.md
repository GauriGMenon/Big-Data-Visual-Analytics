# Big-Data-Visual-Analytics
A github repository for all the assignments and project done in the course(CS661A) in the even semester of 2022-2023 in IIT Kanpur

## Project for Crop Data Visualisation
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://crop-analysis-gaurigmenon.streamlit.app/)

### Data
We have used the following datasets for our analysis
1. India's 1998-2017 crop production statistics by state and district showing annual production of more than fifty crops 
2. Rainfall statistics of India from 1998 to 2017, categorised by district, state and sub-division
3. India district-wise geojson (epsg:4326) created from India shape-file using QGIS software.

### Execution commands
For installing the dependencies, use: \
`pip install requirements.txt`\
For executing the script and hosting the dashboard locally, use: \
`sreamlit run final.py`

### Tasks
We have implemented the following tasks in our dashboard:
1. **Task 1:** To analyze crop production statistics across the nation (district-wise)  
2. **Task 2:** To analyze trends in crop production over the years
3. **Task 3:** To correlate rainfall pattern with crop production trends

#### Task 1 Analysis
1. Punjab, Haryana, and Uttar Pradesh were the first Indian states to cultivate wheat.
2. Today, Madhya Pradesh and Rajasthan have joined the list of the largest Wheat-producing states. 
3. Govt. policies and missions like NFSM, RKVY, PMFBY, subsidies, and farmer knowledge caused the change.

<!-- ![preview](https://raw.githubusercontent.com/GauriGMenon/Big-Data-Visual-Analytics/main/assets/wheat_indo.png) -->
<p align = "center">
<img src="https://raw.githubusercontent.com/GauriGMenon/Big-Data-Visual-Analytics/main/assets/wheat_indo.png" width="400"/>
</p>

<!-- 4. Bajra was produced the most in Maharashtra during the early years. In recent years, production has dropped significantly. -->
<!-- ![preview](https://raw.githubusercontent.com/GauriGMenon/Big-Data-Visual-Analytics/main/assets/bajra_old.png) ![preview](https://raw.githubusercontent.com/GauriGMenon/Big-Data-Visual-Analytics/main/assets/bajra_new.png) -->
<!-- <p><img src="https://raw.githubusercontent.com/GauriGMenon/Big-Data-Visual-Analytics/main/assets/bajra_old.png" width="300"/> <img src="https://raw.githubusercontent.com/GauriGMenon/Big-Data-Visual-Analytics/main/assets/bajra_new.png" width="300"/></p> -->

#### Task 2 Analysis

##### Cereals
- Rice and Wheat were cultivated most, over all the years
- Bajra production peaked in 2012 and decreased henceforth
- Jowar production decreased overall, and consistently after 2008
- Millet production has decreased over the years, especially since 2010. The proportion of other crops(crop diversity) has decreased

##### Pulses
- Proportion of moong has decreased over the years
- Moth and Horse-gram production has decreased

#### Task 3 Analysis(Rainfall correlation)
- Bajra, and Gram are dry land crops and are hence, most grown in Rajasthan and Madhya Pradesh(low rainfall).
<p align = "center">
<img src="https://raw.githubusercontent.com/GauriGMenon/Big-Data-Visual-Analytics/main/assets/rainfall.png" width="400"/>
</p>

- Rice cultivation is also concentrated to high rainfall areas(like the East coast) owing to its water requirements
- The extensive rice cultivation in the Punjab-Haryana region in the absence of sufficient rainfall explains the rainfall issues faced there
<p align = "center">
<img src="https://raw.githubusercontent.com/GauriGMenon/Big-Data-Visual-Analytics/main/assets/rice.png" width="400"/>
</p>

## Assignments for Big Data Visual Analytics
- **Assignment 1:** Familiarised with VTK package and Paraview software for data visualisation
- **Assignment 2:** Implemented the marching squares and volume rendering algorithm
- **Assignment 3:** Build interactive interface for isosurface and frequency histogram visualization using ipywidgets and plotly
- **Assignment 4:** Random sampling and reconstruction of 3D dataset using vtk and scipy
