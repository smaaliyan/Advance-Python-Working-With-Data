import csv
import pprint

result = []
with open("larger_Quake.csv", "r") as CSVFile:
    reader = csv.reader(CSVFile)
    sniffer = csv.Sniffer()
    sample = CSVFile.read(1024)
    CSVFile.seek(0)

    if (sniffer.has_header(sample)):
        next(reader)
    for i in reader:
        if len(i) < 4:
            continue    # Skipping rows that don't have enough columns
        result.append({
            "place": i[0],
            "magnitude": i[1],
            "link": i[2],
            "date": i[3]
        })

pprint.pp(result)