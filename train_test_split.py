import csv

filePath = 'D:\IT492_CP2\GoodReads_Recommendation_System\\rated_interactions.csv'
trainFile = 'D:\IT492_CP2\GoodReads_Recommendation_System\\train.csv'
testFile = 'D:\IT492_CP2\GoodReads_Recommendation_System\\train.csv'

with open(trainFile, 'w') as tf:
    tf.write('user_id,book_id,rating\n')

with open(testFile, 'w') as tf:
    tf.write('user_id,book_id,rating\n')

# def train_append(data: list):
#     with open(trainFile, 'a', newline='') as tf:
#         wr = csv.writer(tf)
#         # for row in data:
#         #     wr.writerow(row)
#         wr.writerows(data)

# def test_append(data: list):
#     with open(testFile, 'a', newline='') as tf:
#         wr = csv.writer(tf)
#         # for row in data:
#         #     wr.writerow(row)
#         wr.writerows(data)
    
def write_to_file(file_path, data):
    with open(file_path, 'a', newline='') as tf:
        wr = csv.writer(tf)
        wr.writerows(data)

user_map = {}
user_map_rev = {}
book_map = {}

with open('D:\IT492_CP2\GoodReads_Recommendation_System\\user_map.csv', 'r') as f:
    rd = csv.reader(f)
    next(rd)

    for row in rd:
        user_map[row[0]] = row[1]
        user_map_rev[row[1]] = row[0]

with open('D:\IT492_CP2\GoodReads_Recommendation_System\\book_map.csv', 'r') as f:
    rd = csv.reader(f)
    next(rd)

    for row in rd:
        book_map[row[0]] = row[1]

print('Book and User Maps ready.')

count = 0
with open(filePath, 'r') as f:
    rd = csv.reader(f)
    next(rd)
    
    curr_user_data = []
    curr = user_map_rev['0']
    for row in rd:
        # print(row)
        if row[0] == curr:
            curr_user_data.append([user_map[row[0]], book_map[row[1]], row[2]])
        else:
            size = len(curr_user_data)
            # train_append(curr_user[:int(0.8 * size)])
            # test_append(curr_user[int(0.8 * size):])
            split_index = int(0.8 * size)
            write_to_file(trainFile, curr_user_data[:split_index])
            write_to_file(testFile, curr_user_data[split_index:])
            curr = row[0]
            curr_user_data = [[user_map[row[0]], book_map[row[1]], row[2]]]
            
        count += 1
        if (count % 1e7 == 0):
            print(f'{int(count/1e6)} M Rows Read.')