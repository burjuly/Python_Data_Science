We are confident that you understand that this is not everything that Pandas can do
for you. Let us go deeper and wider.
In this exercise, you will work with a single log of users who visited a page, including
their timestamps.
+ create a dataframe views with two columns: datetime and user by reading feedviews.
log
  + convert the datetime to the datetime64[ns] Dtype
  + extract the year, month, day, hour, minute, and second from the values of that
column to the new columns
+ create the new column daytime
  + you need to assign the particular time of day value if an hour is within a
particular interval, for example, afternoon if the hour is larger than 11 and
less or equal to 17
  + 0.00 – 03.59 night, 04.00 – 06.59 early morning, 07.00 – 10.59 morning, 11.00
– 16.59 afternoon, 17.00 – 19.59 early evening, 20.00 – 23.59 evening
  + use the method cut to solve this subtask
  + assign the column user as the index
+ calculate the number of elements in your dataframe
  + use the method count()
  + calculate the number of elements in each time of day category using the method
value_counts()
+ sort values in your dataframe by hour, minute, and second in ascending order
(simultaneously and not one by one)
+ calculate the minimum and maximum for the hours and the mode for the daytime
categories
  + calculate the maximum of hour for the rows where the time of day is night
  + calculate the minimum of hour for the rows where the time of day is morning
  + In addition to this, find out who visited the page at those hours (make one
example from that)
  + calculate the mode for the hour and daytime
+ show the 3 earliest hours in the morning and the corresponding usernames and the
3 latest hours and the usernames using nsmallest() and nlargest()
+ use the method describe() to get the basic statistics for the columns
  + to find out what the most popular interval for visiting the page is, calculate
the interquartile range for the hour by extracting values from the result of the
describe() method and store it in the variable iqr
