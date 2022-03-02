import random
top = 100
bot = 1
password = int(random.randint(bot, top))
print('歡迎來到終極密碼遊戲')
while True:
	pwd = int(input('請猜數字'))
	if pwd == password:
		print('恭喜你猜中了')
		break
	elif pwd > password:
		top = pwd
	else:
		bot = pwd
	print('密碼在', bot,'與', top, '之間')