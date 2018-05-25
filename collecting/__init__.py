from collecting import collect
import re

# Open in write mode. This will clear the file of it's contents.
data_file = open('../data.csv', 'w')

# CSV headers.
data_file.write("time,value\n")

# Fetch the data from the Arduino
data = collect.collect_raw_data(300)
print(str(data))

# Get rid of unnecessary formatting; convert to CSV-compatible format.
data = re.sub('[\[\]\' ]', '', str(data))
data = re.sub(',', '\n', data)
data = re.sub(':', ',', data)

# Write data to file
data_file.write(data)
