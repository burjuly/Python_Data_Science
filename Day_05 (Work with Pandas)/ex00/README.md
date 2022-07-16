In this exercise, you will need to load the log file (put it in the directory data in the
root directory of the day) into a dataframe, change the delimiter, and save it to another
file.
The task is:
+ read_csv:
  + filter the rows with index 2 and 3 using the argument skiprows, we know that
these observations were fake
  + filter the last 2 rows from the footer using the argument skipfooter, we know
that these observations were fake too
  + assign the following names to the column: datetime, user
  + use datetime as the index column
+ rename datetime to date_time
+ to_csv:
  + use ’;’ as the delimiter
  + save it to a file with the name feed-views-semicolon.log
As the result of read_csv, you need to achieve the following:
