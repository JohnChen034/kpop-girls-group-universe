# Kpop Girl Group Universe

The rise of K-pop has contributed significantly to the global society, drawing in an increased number of enthusiasts. As K-pop fans, we aim to analyze the popularity of various K-pop girl groups from 2010-2024 to explore the trend in their frame. 

To achieve this, we developed an interactive visualization using Svelte and D3. This visualization includes three components, a dot plot illustrating the debut date of each girl group, basic group information, and the popularity changes from 2010-2024.

The upper graph represents a dot plot in which each dot is positioned based on its debut year and year on the x-axis. We replaced dots with group logos and drew generational boundaries with three lines, spanning generations. Each dot functions as a button. When the mouse is on the button, the button will amplify and display group details including the name, debut date, and the generation affiliation of the group. Clicking the button will reveal further information and the line graph of the popularity trend graph for the selected group. The reason that we chose the dot plot to represent the debut date of each girl group is that the viewers can easily see when one girl group debuts and know which groups are in the same generation. The middle one is the basic information such as group name, debut year, single titles, and album titles are presented. The data from the debut year chart and the information box are both collected from the list of South Korean girl groups on Wikipedia(https://en.wikipedia.org/wiki/List_of_South_Korean_girl_groups). The bottom part features a line chart of popularity trends of the selected girl group from 2010-2024 with girl group name buttons above the line chart. As we mentioned above, by Clicking the group’s logo button, the popularity trend line of the selected girl group will be displayed, and the girl name button of the selected group will turn to the color of the corresponding line. The x-axis of the line chart is the year and the y-axis represents the popularity trend, ranging from 0 to 100, where 0 represents no interest in this topic, while 100 represents most interest in this topic. The data for this chart was collected from Google Trends. The reason that we chose the line chart is that we would like to show the continuous change in popularity over time. The best method to show it is using the line chart. Viewers can easily explore the changes in popularity. Especially, for K-pop fans, they can check when their favorite group becomes more popular.

Work distribution involves one member working on creating the dot plot, the information box in the middle, write-ups for these two parts, and uploading the project to the respiratory. The other member worked on creating the line chart, write-up for this part, and editing the whole write-up. Both members did the integration of these three parts of the visualization together. It took us a week to work on this project and we spent most of the time cleaning the data and building the graphs.
