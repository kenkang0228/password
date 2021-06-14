# 密碼 password='1234'
# 讓使用者最多輸入3次
# 不對的話 印出'密碼錯誤' 還有_次機會
# 對的話 '登入成功'

password = '1234'
i = 3 # 剩餘機會
while i > 0:
	i = i - 1
	pwd = input('Please key in your password: ')
	if pwd == password:
		print('Success ! ')
		break # escape loop
	else:
		print('Wrong ! ')
		if i > 0:
			print('You only have' , i , 'chance !')
		else:
			print('Sorry ! Please change your password !')