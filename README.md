# CS-340 Project Two: Grazioso Salvare Dashboard

## Overview

This dashboard filters and maps Austin Animal Center data to find dogs suited for specific rescue profiles. Pick a profile (Water, Mountain/Wilderness, Disaster/Individual), the table repopulates, the pie chart summarizes the current view, and the map centers on the selected row.

The project demonstrates a full dashboard workflow using a MongoDB CRUD module, Dash/Plotly interface components, interactive filtering, data-table updates, pie chart summaries, and map-based visualization.

## Project Features

- Filters animal shelter records by rescue profile
- Displays matching records in an interactive data table
- Updates a pie chart based on the current filtered data
- Centers the map on the selected table row
- Uses a reusable MongoDB CRUD module for database operations
- Supports reset functionality to return the dashboard to the starting state

## Screenshots

1. **Starting state (Reset)**

<img width="623" height="317" alt="Picture1" src="https://github.com/user-attachments/assets/3d789747-d0d1-4e90-bafe-4138a67d4762" />

2. **Water Rescue applied**

<img width="624" height="318" alt="Picture2" src="https://github.com/user-attachments/assets/1149f054-0fba-4891-a9df-8e678daefc95" />

3. **Mountain/Wilderness applied**

<img width="622" height="321" alt="Picture3" src="https://github.com/user-attachments/assets/05083794-aa32-4064-80ee-9c77617c0670" />

4. **Disaster/Individual applied**

<img width="623" height="320" alt="Picture4" src="https://github.com/user-attachments/assets/1327ee0c-d5cc-498a-abfd-69b84d03ce80" />

5. **Reset again**

<img width="623" height="321" alt="Picture5" src="https://github.com/user-attachments/assets/54d5c956-5671-4ae3-81eb-1b63a279a40c" />

## Technologies Used

- Python
- MongoDB
- PyMongo
- Dash
- Plotly
- Jupyter Notebook
- JupyterDash
- Pandas
- Leaflet/map visualization
- Data filtering and visualization

## Repository Contents

- `ProjectTwoDashboard.ipynb`: Main dashboard notebook
- `CRUD_Python_Module.py`: Reusable MongoDB CRUD module
- `Grazioso Salvare Logo.png`: Dashboard logo asset
- `Project Two.docx`: Project documentation/write-up
- `README.md`: Repository documentation
- `.gitignore`: Git ignore configuration

## How to Run (Codio / Jupyter)

1. Open `ProjectTwoDashboard.ipynb`.
2. Update credentials at the top if needed, including username, password, host, and port.
3. Run all notebook cells.
4. The app renders inline through JupyterDash.

If port `8050` is busy, use another port:

```python
app.run_server(mode="inline", port=8051)  # or 8052
```

## MongoDB / CRUD Module

The project uses a reusable MongoDB CRUD module to separate database logic from dashboard logic. The CRUD module supports database connection handling and basic create, read, update, and delete operations against the animal shelter dataset.

This separation makes the dashboard easier to maintain because the user interface, filtering logic, and database access are not all mixed into one file.

## Skills Demonstrated

- Python dashboard development
- MongoDB CRUD operations
- PyMongo database integration
- Interactive data filtering
- Dash and Plotly visualization
- Data-table, pie chart, and map updates
- Jupyter Notebook workflow
- UI-to-database integration
- Technical documentation
- Requirements-based implementation

## Project Value

This project shows the ability to connect a database-backed Python module to an interactive dashboard. It demonstrates practical experience with MongoDB queries, dashboard callbacks, data filtering, and visualizing records in multiple formats for a specific user need.

The project is strongest for roles involving software engineering, data dashboards, database-backed applications, QA/testing, application support, and Python-based development.

## Future Improvements

- Add a `requirements.txt` file for easier setup
- Add clearer MongoDB import/setup instructions
- Move supporting files into folders such as `notebooks/`, `src/`, `docs/`, and `assets/`
- Add a short demo video or GIF showing the dashboard filters in use
- Add more validation around missing or incomplete latitude/longitude data
