# volume-delay-curves
Data and code to build volume-delay curves for selected locations in London.

### Data Inputs

1. [DfT/DfT.csv](DfT/DfT.csv): Vehicle passage data from the UK Department for Transport (DfT) Automatic Traffic Counter (ATC) sensors.
2. [Google/Google.csv](Google/Google.csv): Travel speed data for corresponding road links at the ATC locations from the [Google Directions Application Programming Interface (API)](https://developers.google.com/maps/documentation/directions/overview).

### Analysis code
[merged_data.ipynb](merged_data.ipynb): (Python) jupyter nodebook to combine the DfT ATC traffic volume and Google travel time data to build the volume-delay curves.
