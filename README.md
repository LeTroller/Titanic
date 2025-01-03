# Titanic
Hi guys, I'm back again with another one of my personal projects! Now you guys might be wondering: what could be the significance of this dashboard? Well, considering that the Titanic embarked on its first AND last voyage more than 100 years ago, I wanted to see how significant were the losses with respect to today's prices and showcase the magnitude of the Titanic's sinking on today's economy (if it sunk in the present age instead of 100+ years ago). One new challenge that I encountered with this dataset compared to the one in my previous project was that I had empty cells and data of incorrect formats in this dataset while my previous dataset was already relatively clean. Hence, on top of visualising the data, I now had to clean the entire dataset first before any analysis could be done. Here's what I did from start to finish:

# Data Cleaning (Tools used: Excel)
Original Dataset: https://docs.google.com/spreadsheets/d/1SF7_RQi8nxf6ppd8cp2ZYh-BCwGVqp4QKf0ze0eUyT8/edit?ref=hackernoon.com&gid=116838508#gid=116838508 (Cleaned Dataset will be included in the repository)

When I first downloaded the dataset, I noticed immediately that:
1) There were some empty cells in the 'Age', 'Cabin' and 'Embarked' Columns
2) The values in the 'Survived' Column were in 0s and 1s instead of 'Yes' or 'No' which could be ambiguous when visualized on a dashboard (same for 'Embarked' column where all the port names were in single letters instead of their full names)

Solution: Find & Replace
1) Empty cells
- Age: For rows with no specific age identified, ages are labelled as 0 so that their ages will not affect the calculation of average age of all passengers.
- Cabin: If a passenger does not have a cabin, the cell value is listed as 'No Cabin' instead (For standardization; this column was not used in the dashboard)
- Embarked: For passengers with empty cell values under this column, their boarding locations were classified as 'Unidentified'.

2) Ambiguous Data Types
- Survived: Instead of 0s and 1s, I replaced the values with 'Yes' or 'No'. E.g. A value of 1 means that the passenger survived while a value of 0 means that the passenger died.
- Embarked: I used the full name of the starting location instead of the short letter abbreviation.

After cleaning the dataset, I proceeded with the data visualization on Power BI.

# Data Visualization (Tools used: Power BI)
Since I had an initial idea of analysing the losses and casualties, I had a couple of visuals planned out in advance when creating the dashboard. The main ones include:
1) Average Fare (2024 USD): Displays average ticket price for each class adjusted for inflation to 2024 USD. This allows us to get a rough inference of the wealth status of each passenger with respect to their passenger class.
2) Passenger Demographics by Class and Gender: Shows the breakdown of passengers by gender within each class. From this visual, one can infer the chance of survival for each passenger class and gender (i.e. whether being a female grants a higher chance of survival, if a better passenger class has higher chance of survival, etc.). I also added slicers for additional filtering for this visual to filter by survival status to additionally show the survivors and casualties for each passenger class.
3) Embarkation Point Distribution: Shows the number and proportion of passengers who boarded the Titanic at each port.
4) Passengers Travelling with Family: Shows the distribution of passengers based on the number of siblings/spouses and parents/children travelling with them. We can observe whether passengers opted to travel alone or with their loved ones from this visual group (there are two graphs for this section: one for siblings/spouses and one for parents/children).
5) Average Age: Shows the average age of all passengers on board the Titanic.
6) Losses Incurred (2024 USD): Shows the financial losses incurred when the Titanic sank adjusted to inflation to 2024 USD.

Slicers used: Survival (Filtering out survivors and casualties), Passenger Class (Visualise data individually by passenger class)

# Additional Information / Tools
- Source for cost calculation of losses incurred:
1) https://www.history.com/news/titanic-facts-construction-passengers-sinking-discovery (Calculating losses incurred)
2) https://www.officialdata.org/us/inflation/1912?endYear=2024&amount=1 (Calculating Average Fare (2024 USD))
- Additional tools used: Pandas (Python file will be included in the repository)

Before finalising the report, I wanted to find out whether the number of family members and age affected a passenger's survival rate (i.e. a correlation between both of the variables mentioned and survival rate). For this, I filtered out the required columns in my test and made use of the correlation feature in Pandas to run the correlation test between my variables. Here are the results:

        |  Survived|     SibSp|     Parch|       Age|
Survived|  1.000000| -0.035322|  0.081629|  0.010539|  <-- Row used to infer results

SibSp   | -0.035322|  1.000000|  0.414838| -0.184664|

Parch   |  0.081629|  0.414838|  1.000000| -0.048786|

Age     |  0.010539| -0.184664| -0.048786|  1.000000|

Based on the correlation test results, when looking at the 'Survived' row, all independent variables (SibSp, Parch, Age) have an absolute correlation of less than 0.1 (i.e. |Correlation| < 0.1). Hence, we can conclude here that the number of family members and passenger age has almost no relation to a passenger's survival rate. 

# Conclusion
Compared to my first dashboard, I felt more satisfied with this work, despite it being a meme-worthy dashboard, as I has incorporated more techniques into this self-directed project like data cleansing and use of Python libraries (Pandas). To be honest, I chose this particular topic on a whim as I was scrolling through Kaggle and other websites for datasets to work on and I just came across the Titanic, and yeah I kind of let my intrusive thoughts win here (haha). Nonetheless, I enjoyed every step of this project as I felt myself learning and picking up more skills that could be used in the future. For subsequent projects, I aim to start incorporating business logic into my dashboards to bring some real-world relevance to my dashboards. Can't wait to get started on my next project soon!

Wishing everyone a Happy New Year and a successful 2025!
