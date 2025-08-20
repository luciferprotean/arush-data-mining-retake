import numpy as np
import pandas as pd

cab_df=pd.read_csv("cab_rides.csv")
weather_df=pd.read_csv("weather.csv")

cab_df['datetime']=pd.to_datetime(cab_df['time_stamp']/1000, unit="s")
weather_df['datetime']=pd.to_datetime(weather_df['time_stamp'], unit="s")

cab_df=cab_df.drop('time_stamp', axis=1)
weather_df=weather_df.drop('time_stamp', axis=1)

cab_df['datetime']=cab_df['datetime'].dt.strftime('%d-%m-%Y %H:%M:%S')
weather_df['datetime']=weather_df['datetime'].dt.strftime('%d-%m-%Y %H:%M:%S')
#cab_df.to_csv("cabdata_updated.csv", index=False, encoding='utf-8-sig')
#weather_df.to_csv("weatherdata_updated.csv", index=False, encoding='utf-8-sig')

matching_df = pd.merge(
    cab_df,
    weather_df,
    left_on=['datetime', 'source'],
    right_on=['datetime', 'location'],
    how='inner'  # inner join -> keeps only matching datetime values
)

matching_df.to_csv("matched_records_filteredLoc.csv", index=False, encoding='utf-8-sig')
#matching_100 = matching_df.head(100)
#print(matching_100)


