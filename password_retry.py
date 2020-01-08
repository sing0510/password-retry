password = ('singsing')
i = 3
while i > 0:
	i = i - 1
	pwd = input ('請輸入密碼')
	if pwd == password:
		print('登入成功')
		break
	else:
		if i > 0:
			print('錯誤,還有',i,'機會')
		else:
			print('沒機會了')





	

