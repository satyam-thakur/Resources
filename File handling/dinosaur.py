import csv
feet_data = {}
stride_data = {}
# Open and parse the required file1 content to dictionary
with open("file1.csv","r") as feet:
# with open("dataset1.csv","r") as feet:
    for row in csv.reader(feet):
        if len(row)>2 and row[0].strip() != "Dinosaur":
            # try:
            feet_data[row[0].strip()] = (row[1].strip(),float(row[2].strip()))
            # except ValueError:
            #     continue

# Open and parse the required file2 content to dictionary
with open("file2.csv", "r") as stride:
# with open("dataset2.csv", "r") as stride:
    for row in csv.reader(stride):
        if len(row)>2 and row[0].strip() != "Dinosaur":
            # try:
            stride_data[row[0].strip()] = float(row[1].strip())
            # except ValueError:
                # continue

speed = []
g = 9.8
# Fetch the file1 content and compare if exists in file2
for dinosaur, (pedal, feet_len) in feet_data.items():
    if dinosaur in stride_data:
        pedal_value = 2 if pedal.lower() == "bipedal" else 4
        speeds = ((feet_len*stride_data[dinosaur])/pedal_value)*g
        speed.append((dinosaur, speeds))

# Sort the list
speed.sort(key=lambda x:x[1])
# Print in the order as required
for s in speed:
    print (s)
