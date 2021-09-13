# Data Science CRS Score Analysis: Project Overview
* Performend analysis on CRS score trends to help potential international students immigrate to Canada
* Scraped CRA website to obtain information on the immigration program, CRS score, number of accepted applicants
* Performed EDA on the collected data and presented the findings to international students in a Zoom session

## Code and Resources Used 
**Python Version:** 3.7.6  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, BeautifulSoup 

## Web Scraping & Data Cleaning 
Scraped the CRA website using BeutifulSoup package to scrape entries starting from January 31st, 2015 - May 31, 2021. Got the following information:
*	Date of Draw 
*	Immigration program
*	CRS score
*	Programs covered 
*	Data cleaning: properly converting datatype of Invitations issued column to float

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 
![alt text](https://github.com/johny9887/ds_CRS_proj/blob/main/DS1.png)
![alt text](https://github.com/johny9887/ds_CRS_proj/blob/main/DS2.png)
![alt text](https://github.com/johny9887/ds_CRS_proj/blob/main/DS3.png)

Also, visualizations were created using Tableau: https://public.tableau.com/app/profile/john4847/viz/IRCCAnalysis/Dashboard1
