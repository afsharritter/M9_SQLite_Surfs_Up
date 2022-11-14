# Module 11: Surfs Up! with SQLite

## Overview of the Analysis

Climate data was collected from numerous weather stations on the Island of Oahu. The purpose of this analysis is to use temperature data to determine whether a Surf & Ice Cream Shop in Hawaii will be sustainable year around.

## Results

In this analysis, we used Python's SQLAlchemy library to connect to an SQLite database containing weather data from the Island of Oahu. Specifically, we aim to compare temperatures for the months of June and December from 2010 to 2017. 

### June Summary Statistics

The data was first queried to reflect temperature data for the month of June from 2010 to 2017. See Figure 1

![Figure 1](/analysis/June_Statistics.png "Figure 1: June Summary Statistics")

The Summary Statistics for June show 1700 weather recordings, with an average of 74.9 degrees and a median of 75.0 degrees. The highest recorded temperature in June was 85 degrees, while the lowest recorded temperature was 64 degrees. The standard deviation for this sample was 3.25. The proximity between the mean and median implies a normal distribution.

### December Summary Statistics

The data was then queried to reflect temperature data for the month of December from 2010 to 2017. See figure 2.

![Figure 2](/analysis/December_Statistics.png "Figure 2: December Summary Statistics")

The Summary Statistics for December show 1517 weather recordings, with an average of 71.04 and median of 71.0 degrees. The highest recorded temperature in December was 83 degrees, while the lowest recorded temperature was 56 degrees. The standard deviation for this sample was 3.75. The proximity between the mean and median implies a normal distribution. 

### Differences between June and December

The data indicates that June and December exhibit a high level of similarity in the temperature patterns.Key differences include:

* June has a higher average temperature (75 degrees in June vs 71 degrees in December)
* December has a lower minimum temperature (56 degrees in December vs. 64 degrees in June)
* December has a greater range of temperatures than June (27 degrees in December vs 21 degrees in June)

## Data Summary and Recommendations

Overall, June and December have similar temperature patterns, differing slightly in average and range. December is somewhat colder, with a lower minimum and average temperature but highs comparable to June. 

Given Oahu's tropical climate and proximity to the equator, we expect the temperature to remain relatively consistent throughout the year. 

In addition, we recommend performing the same queries above but filtering by the weather station closest to the Surf & Ice Cream shop. This would give stakeholders a better idea of the specific micro-climate that may affect the shop's sustainability. 

We also recommend gathering summary statistics based on precipitation in the months of June and December. Precipitation may have a greater impact on a surf shop's sustainability. According to GoHawaii.com, Hawaii's rainy season falls between November and March.[[1]](#1) Thus, we would expect a significant increase in precipitation in December, as compared to June. 


## References

<a id="1">[1]</a>
Hawai'i Tourism. (2022, March 16). Hawaii Weather. Go Hawaii. Retrieved November 14, 2022, from https://www.gohawaii.com/trip-planning/weather#:~:text=The%20wettest%20months%20are%20from,be%20found%20around%20the%20coast. 