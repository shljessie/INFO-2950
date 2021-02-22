# Phase 1: Brainstorming

Repository link: <https://github.com/shljessie/INFO-2950>

## Dataset Ideas

### Idea 1 : Did Coronavirus have an impact on people riding Citibike? 

 **Citibike Station bike availability affected by time, location, weather**

**Explanation**
Citi Bike is a privately owned public bicycle sharing system serving the New York City boroughs of the Bronx, Brooklyn, Manhattan, and Queens, as well as Jersey City, New Jersey.
We seek to examine CitiBike ridership data, joined with daily NYC weather data, to study the impact of weather, time, location on shared bike usage and generate a predictive model which can estimate the number of trips that would be taken on each day.

**Data**
1.  Citibike Trips Data : https://s3.amazonaws.com/tripdata/index.html

- Period : Monthly data. After we choose the period length we can download data accordingly
- Location: NYC 
- Provider : Citibike ( Provided by Lyft )

This data has been processed to remove trips that are taken by staff as they service and inspect the system, trips that are taken to/from any of our “test” stations (which we were using more in June and July 2013), and any trips that were below 60 seconds in length (potentially false starts or users trying to re-dock a bike to ensure it's secure).

- Columns: ["tripduration","starttime","stoptime","start station id","start station name","start station latitude","start station longitude","end station id","end station name","end station latitude","end station longitude","bikeid","usertype","birth year","gender"]
 
2. Coronavirus Data: https://data.cityofnewyork.us/Health/COVID-19-Daily-Counts-of-Cases-Hospitalizations-an/rc75-m7u3

- Period : 02.29.2020 - 12.16.2020
- Location: NYC 
- Provider : Department of Health and Mental Hygiene (DOHMH)

: This dataset has 39 columns describing different statistics relating to the coronavirus such as the number of people hospitalized, new infections, and deaths. This dataset reports coronavirus conditions of each day. 

Daily count of NYC residents who tested positive for SARS-CoV-2, who were hospitalized with COVID-19, and deaths among COVID-19 patients.


**Things to Analyze**
- citibike trip data based on time (mornings, days ,evenings, based weekdays, weekends ....etc) time and trip duration, time and bike numbers in different stations, time and user types.
- number of people riding bikes : Do more people riding bikes influence people to ride bikes too? 
- coronavirus how did the coronavirus impact the number of people riding citibikes? Comparing 
- users of citibike what kind of users used citibike? 
- How fast do Citi Bike riders tend to travel? (travel time and distance)
- How accurate are Google Maps cycling time estimates? 
- How do age and gender impact biking speed?
- How did coronavirus impact citibike bike  trips?


**Things to Consider**
- Period: What period should I set? Should I consider the coronavirus or do an analysis of a time before that? 
- Prediction Problem. If we are trying to do some sort of prediction in the end, 
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


### Idea 3: What is the impact of Weather on Citibike Usage?

On this topic we plan to explore the effect of weather on citibike usage. 

**Data**
1.  Citibike Trips Data : https://s3.amazonaws.com/tripdata/index.html

- Period : Monthly data. After we choose the period length we can download data accordingly
- Location: NYC 
- Provider : Citibike ( Provided by Lyft )

This data has been processed to remove trips that are taken by staff as they service and inspect the system, trips that are taken to/from any of our “test” stations (which we were using more in June and July 2013), and any trips that were below 60 seconds in length (potentially false starts or users trying to re-dock a bike to ensure it's secure).

- Columns: ["tripduration","starttime","stoptime","start station id","start station name","start station latitude","start station longitude","end station id","end station name","end station latitude","end station longitude","bikeid","usertype","birth year","gender"]



### Questions for Reviewers

1. It was mentioned in the student guidebook that there was caution for using COVID-19 data in our project. Would it be okay to select a period of time were unchangeable COVID data was provided
2. 
3. 