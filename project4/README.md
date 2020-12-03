# Project 4: Visualizing NBA Player Dataset Statistics.

Contributors: Eric Chu, Frank Kim, Isaac Santamaria, Nabil Siddiqui 

## Description
 This project focuses on data analysis about each NBA players’ statistics in the league during the 2017-2018 season. Those who would want to use this project would be NBA scouts, NBA fans, fantasy basketball players, basketball lovers, etc. In terms of needs this project would fulfill, the goal of this project is to present users a certain player/list of player suggestions that best fit their needs as well as receive player statistics and position statistics. Users would be able to input multiple aspects such as age, position, true shooting percentage, player efficiency rating, etc. in order to find the player that best fits their statistical needs. The user may be presented a list of multiple players that fit their needs or just one. Along with a suggestion based on data analysis, this project is also able to calculate minimum, maximum, median, mean, standard deviation of statistics such as: True Shooting, 3 Point Attempt rate, Minutes per game for any player they may input. All in all, this project aims to be the ultimate guide for NBA fans to gain insight into each players’ statistics and find what they need in terms of data.


## Update #1: 

### Functions Descriptions:
### main()
  When main is run it acts as an interface to run a requested method given the user input.

### find_a_player()
  This function acts finds multiple players depending on factors a user would input. For example: If I want a player that shoots >30% from the 3 point line, 20% fg percentage, this function would return all the players that meet this requirement. Potentially useful for NBA scouts to create a versatile yet functional team. 

### get_player_position_stat()
The function allows users to input a certain position and will be returned with the avg minutes per game, avg true shooting, and avg 3 point attempt rate in which the position is.

### retrieve_playerstat()
This function allows users to input a certain players name as well as input a certain statistic they would like to retrieve. Statistics include minimum points (min), maximum points (max), median points for the season(median), average amount of  points for the season(avg), standard deviation of True Shooting(True Shooting), average 3 Point Attempt rate(avg 3PA), and average minutes per game (avg MPG).

### Get_team_avg()
This function enables users to get the average minutes per game, true shooting, and 3 point attempts rate per game for a specific team as opposed to a specific position.

## Update #2: 

### main()
  The main method now takes user input to determine which function should be called. Also the data file is parsed and passed to respective function. 

### find_a_player()
   When this function is called it can either do a thorough player search or a customized user input player find. The thorough player search ask questions on all aspects regarding ability;  player position, minutes played, player efficiency rating, true shooting percentage, 3 Point attempt percentage to find a set of player with matching abilities. The customized user input takes as many reqs or as little requirements the user wants to find his player. 

### get_player_position_stat()

####COMMENTS####

The game dataset will be retrieved from a website that contains all the statistics and in order to do that we need to import some packages for example the panda library 
import pandas as pd. After that we will find the mean for minutes per game, true shooting, and 3-point attempt rate by looking at the position of each player. 

### retrieve_playerstat()
This function allows users to input a certain players name, then input a certain statistic they would like to retrieve, and retrieve said statistic.

Statistics include: games played (G), minutes played (MP), player efficiency rating (PER), true shooting percentage (TS%), 3 point attempt rate (3PAr), free throw rate (FTr), offensive rebound percentage (ORB%), defensive rebound percentage (DRB%), total rebound percentage (TRB%), assist percentage (AST%), block percentage (BLK%), steal percentage (STL%), and turnover percentage (TOV%)

### Get_team_avg
This function enables users to get the average minutes per game, true shooting, and 3 point attempts rate per game for a specific team as opposed to a specific position.
This function gets the average or mean for avg mpg, true shooting, abd 3 point attempts column featured in the data set for a specific team. When the function is called a user is asked if they want to get the avg mpg, true shooting, and 3 point shooting for each team. The function will then provide the avg of the specified data for a specific team.



## Final Submission: 
