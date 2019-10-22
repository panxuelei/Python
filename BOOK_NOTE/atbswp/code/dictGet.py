picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

#get()方法 有两个参数：要取得其值的键，以及如果该键
#不存在时返回的备用值。
