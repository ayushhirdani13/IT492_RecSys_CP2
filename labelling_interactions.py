import csv

filePath = 'D:\IT492_CP2\GoodReads_Recommendation_System\\rated_interactions.csv'

user_map = {}
book_map = {}

user_count = 0
book_count = 0

with open(filePath, 'r') as f:
    rd = csv.reader(f)

    next(rd)
    # print(header)
    # print(f'Columns: {header}')

    for row in rd:
        user = int(row[0])
        book = int(row[1])
        if user not in user_map.keys():
            user_map[user] = user_count
            user_count += 1

        if book not in book_map.keys():
            book_map[book] = book_count
            book_count += 1

with open('./user_map.csv', 'w', newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['user_id', 'user_id_mapped'])

    # wr.writerows([key, value] for key, value in user_map.items())
    for key, value in user_map.items():
        wr.writerow([key, value])

with open('./book_map.csv', 'w', newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['book_id', 'book_id_mapped'])

    # wr.writerows([key, value] for key, value in book_map.items())
    for key, value in book_map.items():
        wr.writerow([key, value])
