# Project 4: Visualizing NBA Player Dataset Statistics.

## Description
 This project focuses on data analysis about each NBA players’ statistics in the league during the 2017-2018 season. Those who would want to use this project would be NBA scouts, NBA fans, fantasy basketball players, basketball lovers, etc. In terms of needs this project would fulfill, the goal of this project is to present users a certain player/list of player suggestions that best fit their needs. Users would be able to input multiple aspects such as age, position, true shooting percentage, player efficiency rating, etc. in order to find the player that best fits their statistical needs. The user may be presented a list of multiple players that fit their needs or just one. Along with a suggestion based on data analysis, this project is also able to calculate minimum, maximum, median, mean, standard deviation of statistics such as: True Shooting, 3 Point Attempt rate, Minutes per game for any player they may input. All in all, this project aims to be the ultimate guide for NBA fans to gain insight into each players’ statistics and find what they need in terms of data.


## Functions Descriptions:

### main()
  When main is run it acts as an interface to run a requested method given the user input.

### find_a_player()
  This function acts finds multiple players depending on factors a user would input. For example: If I want a player that shoots >30% from the 3 point line, 20% fg percentage, this function would return all the players that meet this requirement. Potentially useful for NBA scouts to create a versatile yet functional team. 

### get_NBA_stats()
The function won't take any boundaries however rather will have the avg minutes per game, avg true shooting, and avg 3 point attempt rate in which the program prompts for the year and the players'position for which to return per-game insights.
