data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: # 一行一行讀取
		data.append(line)
		count += 1 
		if count % 1000 == 0: # 求1000餘數
		    print(len(data)) # 讀取進度
print('檔案讀取完畢， 總共有', len(data), '筆資料')
# print(len(data)) # 印出幾筆資料(長度)
sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #n算留言長度
	#print(sum_len)

print('平均是', sum_len / len(data)) # 留言平均長度







# print(data) # 印出資料全部資料
# print(data[0]) # 印出特地資料
# print('------------------')
# print(data[1]) 