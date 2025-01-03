# Titanic
Hi guys, I'm back again with another one of my personal projects! Now you guys might be wondering: what could be the significance of this dashboard? Well, considering that the Titanic embarked on its first AND last voyage more than 100 years ago, I wanted to see how significant were the losses with respect to today's prices and showcase the magnitude of the Titanic's sinking on today's economy (if it sunk in the present age instead of 100+ years ago). One new challenge that I encountered with this dataset compared to the one in my previous project was that I had empty cells and data of incorrect formats in this dataset while my previous dataset was already relatively clean. Hence, on top of visualising the data, I now had to clean the entire dataset first before any analysis could be done. Here's what I did from start to finish:

# Data Cleaning (Tools used: Excel)
Original Dataset: https://docs.google.com/spreadsheets/d/1SF7_RQi8nxf6ppd8cp2ZYh-BCwGVqp4QKf0ze0eUyT8/edit?ref=hackernoon.com&gid=116838508#gid=116838508 (Cleaned Dataset will be included in the repository)

When I first downloaded the dataset, I noticed immediately that:
1) There were some empty cells in the Age, Cabin and Embarked Columns
2) The values in the Survived Column were in 0s and 1s instead of Yes or No which could be ambiguous when visualized on a dashboard (same for Embarked column where all the port names were in single letters instead of their full names)

Solution: Find & Replace
1) Empty cells
- Age: For rows with no specific age identified, ages are labelled as 0 so that their ages will not affect the calculation of average age of all passengers.
- Cabin: If a passenger does not have a cabin, the cell value is listed as '-' instead (For standardization; this column was not used in the dashboard)
- Embarked: For passengers with empty cell values under this column, their boarding locations were classified as 'Unidentified'.

2) Ambiguous Data Types
- Survived: Instead of 0s and 1s, I replaced the values with 'Yes' or 'No'. E.g. A value of 1 means that the passenger survived while a value of 0 means that the passenger died.
- Embarked: I used the full name of the starting location instead of the short letter abbreviation.

After cleaning the dataset, I proceeded with the data visualization on Power BI.

# Data Visualization (Tools used: Power BI)
Since I had an initial idea of analysing the losses and casualties, 
