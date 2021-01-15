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


# 清單篩選
new = []
for d in data: #把清單中的東西一筆一筆呼叫出來
# 每一個d 就是一個單獨留言 d == 字串
# data 是裝著全部資料清單(100萬筆)
    if len(d) < 100:
        new.append(d) #小於100裝進清單
print('共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])   







# print(data) # 印出資料全部資料
# print(data[0]) # 印出特地資料
# print('------------------')
# print(data[1]) 