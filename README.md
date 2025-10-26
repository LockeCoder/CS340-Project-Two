# CS 340 – Project Two: Grazioso Salvare Dashboard

# Overview
This dashboard filters and maps Austin Animal Center data to find dogs suited for specific rescue profiles. Pick a profile (Water, Mountain/Wilderness, Disaster/Individual), the table repopulates, the pie chart summarizes the current view, and the map centers on the selected row.

# Screenshots

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



##How to Run (Codio / Jupyter)
- Open `code_files/ProjectTwoDashboard.ipynb`.
- Update credentials at the top if needed (username/password/host/port).
- **Run All**. App renders inline via JupyterDash.  
- If port 8050 is busy:  
  ```python
  app.run_server(mode="inline", port=8051)  # or 8052
