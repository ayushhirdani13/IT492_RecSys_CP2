import csv

filePath = 'D:\IT492_CP2\GoodReads_Recommendation_System\goodreads_interactions.csv'
writeFile = 'D:\IT492_CP2\GoodReads_Recommendation_System\\rated_interactions.csv'

with open(filePath, 'r') as rf, open(writeFile, 'w', newline='') as wf:
    reader = csv.reader(rf)
    writer = csv.writer(wf)

    header = next(reader)
    writer.writerow([header[0], header[1], header[3]])

    for row in reader:
        if int(row[2]) == 1 and int(row[3]) > 0:
            writer.writerow([row[0], row[1], row[3]])