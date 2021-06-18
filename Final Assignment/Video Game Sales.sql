# Using Video_Game_Sales Data
use video_game_sale;

# Basic Select Quieres  

# Q1 Find the Names of Each Game
select Name from video_game_sale.`video games sales`;
# Q2 Find the Platform for each Game
select Platform from video_game_sale.`video games sales`; 
# Q3 Find the Name and Platform for Each Video Game
select Name, Platform from `video games sales`;
# Q4 Find the Name and Year of the Video Game
select Name, Year from `video games sales`;
# Q5 Find all the information about each Video Game
select * from video_game_sale.`video games sales`;

## Where Clause Queries
# Q1 Find the game with the Rank of 234
select * from video_game_sale.`video games sales` where Rank = 234;
# Q2 Find the Video Game Sale between 2000 to 2010
select * from video_game_sale.`video games sales` where Year between 2000 and 2010;
# Q3 Find the Game not Realeased in the years betweeen 2000 and 2010
select * from video_game_sale.`video games sales` where Year not between 2000 and 2010;
# Q4 Find the first 5 Game Sales 
select * from video_game_sale.`video games sales` where Rank <= 5;
