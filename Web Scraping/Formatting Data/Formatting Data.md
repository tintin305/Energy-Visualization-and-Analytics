# Required

* 3 sets of data:
    * One .csv with all of the data combined
    * Multiple .csv files, each with a single channel's reading for the whole time span
    * Multiple .csv files, each with a single sensor's readings (two channels: kVah and kWh)

## Processing things to do

* For each file:
    * Read in timestamp as a datetime object
    * Check first reading's timestamp, find date in 6 months time. Remove all readings after 6 months (extra day of repeated data)
    * Save as file indicating the range of sensors and the date range
* For stitching together files for the same sensors
    * append()
* For stitching together files for different sensors
    * extend()
* For splitting columns
    * ?  