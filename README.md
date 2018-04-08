# YouTube_VideosAnalysis_Northwest
This project is a part of the course 44564-Data Intensive Systems at Northwest for Spring 2018 semester. This is being implemented by the group 2C of that course. This group has 4 develpors in total, which is a collaboration of two teams comprising of 2 members each. 

Teams Members:

Group 2C-Team 1: Vineeth Agarwal & Durga Charan Potukuru

Group 2C-Team 2: Ashok Atkuri & Raja Srikar Karthik Chinta

## Project Source Links
Repository: https://github.com/Vineeth-Agarwal/YouTube_VideosAnalysis_Northwest

Issue Tracker: https://github.com/Vineeth-Agarwal/YouTube_VideosAnalysis_Northwest/issues/1

## Introduction
The dataset includes data gathered from videos on YouTube that are contained within the trending category each day. This would help us make som analysis on the videos, channels, comments, likes vews & more to extract important information.

## Data Source
The data source contains two kinds of data files, one includes comments and the other includes video statistics. They are linked by the unique video_id field. It has category classification in .json and comments and videos list in .csv file formats.
The size of the data source is 148MB and it contains structured data.

## Data Source Link
https://www.kaggle.com/datasnaek/youtube

## Big Data Qualifications
### Volume : 
This data set contains huge set of comments and likes count and replies for each video in dataset and its size is about 148MB after decompressing the file.

### Variety: 
The data is all in text and special characters. Also there is a variety of languages involved in the comments. 

### Velocity: 
The dataset has the videos that are added to youtube every day with different tags and the number of views, and likes come to each video everyday. The other data set contains the comments that are posted every day for each video.

### Veractiy: 
There is no way to know if the data about comments or likes is authenticate because there is no check on a user profile that comments or likes.

### Value:
We can work on category based on tags and find the popular channel and trending topics in youtube. We have data for Great Britan and United States thus, we can find the sentiment analysis in a variety of forms, categorising YouTube videos based on their comments and statistics.

## Big Data Questions
1) For each category id, find the number of videos uploaded everyday to determine the top 5 trending video categories. (Ashok)

2) For each video, find the number of likes and views it gets to determine the likeliness of a video by taking the ratio of views to likes. Goal is to find relation between number of views and likes(Srikar Karthik).

3) For each video, find the sentiment of people for a video based on the emotions used in comments. The goal is to determine top 10 positive, negative or neutral commented videos. (Durga Charan)

4) For each channel-id tagged with Android, find number of views each video gets, to determine the top 5 trending channels in android. (Vineeth)

## Big Data Solutions
1)
Mapper input: EVp4-qjWVJE,	Chargers vs. Broncos, | NFL, Week 1 Game Highlights	NFL	17,	NFL|Football|offense|defense|afc|nfc|American, 743947,	6126,	352,	2438.	https://i.ytimg.com/vi/EVp4-qjWVJE/default.jpg,	13.09
Mapper Output/Reducer input: Entertainment, 09/13/2018
Reducer output: Entertainment 38 09/13/2018

2)
Mapper input: QBGaO89cBMI	Radiohead - Lift,	Radiohead,	10,	radiohead|lift|ok computer|oknotok	752844	42290	359	3250	https://i.ytimg.com/vi/QBGaO89cBMI/default.jpg	13.09
Mapper Output/Reducer input: XpVt6Z1Gjjo	46245 21122
Reducer output: jt2OHQh0HoQ America's Got Talent, 50%

3)
Mapper input: 
1)XpVt6Z1Gjjo	#1 trending!!!!!!!!!	3	0 
2)QBGaO89cBMI	Radiohead - Lift	Radiohead	10	radiohead|lift|ok computer|oknotok	752844	42290	359	3250	https://i.ytimg.com/vi/QBGaO89cBMI/default.jpg	13.09
Mapper Output/Reducer input: XpVt6Z1Gjjo,	1 on trending good job
Reducer output: jt2OHQh0HoQ ATTACKED BY A POLICE DOG!!, Negative


4)
Mapper input: EVp4-qjWVJE,	Chargers vs. Broncos, | NFL, Week 1 Game Highlights	NFL	17,	NFL|Football|offense|defense|afc|nfc|American, 743947,	6126,	352,	2438.	https://i.ytimg.com/vi/EVp4-qjWVJE/default.jpg,	13.09
Mapper Output/Reducer input:Chargers vs. Broncos, NFL|Football|offense|defense|afc|nfc|American, 473691
Reducer output: Chargers vs. Broncos


## Language:  
Python 

## chart:
Bar charts and scattered plots.
