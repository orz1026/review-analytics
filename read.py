import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
for i in bar(range(100)):
         # Code that you want to run
        time.sleep(0.02)
with open('reviews.txt', 'r') as f:
	for line in f: # 一行一行讀取
		data.append(line)
		count += 1
		bar.update(count) 
		# if count % 1000 == 0: # 求1000餘數
		#     print(len(data)) # 讀取進度
print('檔案讀取完畢， 總共有', len(data), '筆資料')

print(data[0])


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

# 留言裡面有幾筆提到good
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('共有', len(good), '筆留言提到good')
print(good[0])

#文字計數
start_time = time.time()
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典
for word in wc:
	if wc[word] > 1000000:
	    print(word, wc[word])
end_time = time.time()  #紀錄時間
print('花了', end_time - start_time, 'seconds')
print(len(wc))
print(wc['alpha'])

while True:
	word = input('請問你要查甚麼字: ')
	if word == 'q':
		break
	if word in wc:
	    print(word, '出現過的次數: ', wc[word])
	else:
		print('這個字沒有出現過!')


print('感謝使用查詢功能')


# 清單快寫法 
# good = [d for d in data if 'good' in d]
# pront(god889)
# print(data) # 印出資料全部資料
# print(data[0]) # 印出特地資料
# print('------------------')
# print(data[1]) 






