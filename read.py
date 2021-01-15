data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: # 一行一行讀取
		data.append(line)
		count += 1 
		if count % 1000 == 0: # 求1000餘數
		    print(len(data)) # 讀取進度
print(len(data)) # 印出幾筆資料(長度)

# print(data) # 印出資料全部資料
print(data[0]) # 印出特地資料
print('------------------')
print(data[1]) 