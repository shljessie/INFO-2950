# Phase 1: Brainstorming

Repository link: <https://github.com/shljessie/INFO-2950>

## Dataset Ideas

### Idea 1 : Citybike Data Analysis

 **Citibike Station bike availability affected by time, location, weather**

**Explanation**
Citi Bike is a privately owned public bicycle sharing system serving the New York City boroughs of the Bronx, Brooklyn, Manhattan, and Queens, as well as Jersey City, New Jersey.
I seek to examine CitiBike ridership data, joined with daily NYC weather data, to study the impact of weather, time, location on shared bike usage and generate a predictive model which can estimate the number of trips that would be taken on each day.

**Data**
- Google geocoding API : To get the geolocations of the bike data and visualize them into classified location sections
 https://developers.google.com/maps/documentation/geocoding/overview
- citibike mobility survey : https://www1.nyc.gov/html/dot/html/about/citywide-mobility-survey.shtml
survey results of main reasons people use citibike
- citibike trips data : https://s3.amazonaws.com/tripdata/index.html
["tripduration","starttime","stoptime","start station id","start station name","start station latitude","start station longitude","end station id","end station name","end station latitude","end station longitude","bikeid","usertype","birth year","gender"]
-  daily weather data : https://rapidapi.com/community/api/open-weather-map
 use weather api to get access to newyork weather data. choose a location to represent all of newyork. such as central park.

**Things to Analyze**
- citibike trip data based on time (mornings, days ,evenings, based weekdays, weekends ....etc) time and trip duration, time and bike numbers in different stations, time and user types.
- weather : what weather impacts people riding citibikes? 
- number of people riding bikes : Do more people riding bikes influence people to ride bikes too? 
- coronavirus how did the coronavirus impact the number of people riding citibikes? 
- users of citibike what kind of users used citibike? 
- How fast do Citi Bike riders tend to travel? (travel time and distance)
- How accurate are Google Maps cycling time estimates? 
- How do age and gender impact biking speed?
- How did coronavirus impact citibike bike  trips?
- Gender? Age? 
- Korea bike share system. Comparision maybe

**Things to Consider**
- Period: What period should I set? Should I consider the coronavirus or do an analysis of a time before that? 
- Location : should I choose single location to represent all of newyork weather?
- Main Questions, Problems that might arise/ setting hypothesis.


### Idea 2:  Bird Migration Data
https://ebird.org/data/download
Cornell E-bird Migration Data

https://www.mbr-pwrc.usgs.gov/
For 434 species (82% of 529 species considered) we used trajectories from BBS data,
https://www.sciencebase.gov/catalog/item/52b1dfa8e4b0d9b325230cd9
follow through links to get more detailed info on bird data

-use with api 
- get sample data 

(might have to ask about which method preferred API, data)

what I can analyze
- bird migration patterns. which habitats do birds live in more 
which bird habitats should be better protected ...etc 

- past analysis have been done on :
 1. ground level pollution data, existing regulations vs bird watching
 2. . NEXRAD radar monitoring to calculate bird populations through biomass


### Idea 4 :  Consumption and Environment Analysis

Meat consumption data, carbon emission data. 
calculate individual meat consumption
compare amount of meat that is actually being produced. 
set hypothesis we are producing more meat than we can consume. 
take amount of meat that we are eating, look at data on where meat is being used.
yearly human consumptions. Calculate how much waste is actually being produced. 
individual carbon emission from a day's meal is ..
find carbon emission data for a individual meal. 
Set persona's if some one who eats .... much with processed foods.. 
their carbon emission could be ...etc

with organic choices we can reduce carbon emission by.. 


### Idea 5 :  Google QuickDraw Dataset Analyzing Human Drawing Patterns
https://github.com/googlecreativelab/quickdraw-dataset 

#### Project Idea
Using the Google Quickdraw Dataset to explore the different
variations of people's drawings. Stereotypes, culture influences,
cognitive processes of human drawing can be studied. I could analyze the
data and choose a certain drawing or a category of drawing to analyze the 
variations of drawings between people from different countries. 

#### About the DataSet
The Quick Draw Dataset is a collection of 50 million drawings across 345 categories, contributed by players of the game Quick, Draw!. The drawings were captured as timestamped vectors, tagged with metadata including what the player was asked to draw and in which country the player was located. You can browse the recognized drawings on https://quickdraw.withgoogle.com/data 
The data contains of the keyid, category of drawing, whether it was recognized by the game, country code, and strokes used in the drawing. 


### Questions for Reviewers