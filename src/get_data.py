import requests
from bs4 import BeautifulSoup

# Fetch the HTML content
url = 'https://en.wikipedia.org/wiki/List_of_South_Korean_girl_groups'
response = requests.get(url)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Function to extract table data for a given generation
def extract_generation_data(header_id):
    header = soup.find('span', {'id': header_id})
    if header:
        section = header.find_parent('h2')
        next_elements = section.find_next_siblings()
        generation_data = []
        for element in next_elements:
            if element.name == 'h2':
                break  # Stop if the next generation section is reached
            if element.name == 'table':
                # Extract table data
                table_data = []
                rows = element.find_all('tr')
                for row in rows:
                    cols = row.find_all(['th', 'td'])
                    cols = [ele.text.strip() for ele in cols]
                    table_data.append(cols)
                generation_data.append(table_data)
        return generation_data
    else:
        return []

# Extract data for Generations 2, 3, and 4
generation_data = {}
for gen in range(2, 5):  # Adjust range as needed for different generations
    header_id = f'Generation_{gen}'
    generation_data[f'Generation {gen}'] = extract_generation_data(header_id)

# Now `generation_data` contains the data from the tables for Generations 2, 3, and 4
# You might want to print it or process it further depending on your needs

for generation, tables in generation_data.items():
    print(f"{generation}:")
    for table in tables:
        for row in table:
            print(row)
        print("-----")  # Separator for tables
    print("==========")  # Separator for generations

# import pandas as pd
# headers = ["Generation"] + generation_data["Generation 2"][0][0]  # Assuming the first row of Generation 2 table contains headers
# print(headers)
# # Initialize an empty DataFrame
# df = pd.DataFrame(columns=headers)
# # Function to add data to the DataFrame
# def add_data_to_df(generation, tables):
#     for group_data in tables[1:]:  # Skip headers
#         # Prepend generation to data
#         row_data = [generation] + group_data
#         df.loc[len(df)] = row_data
#
# # Add data for each generation
# for generation, tables in generation_data.items():
#     add_data_to_df(generation, tables[0])
#
# df.to_csv("test.csv")
