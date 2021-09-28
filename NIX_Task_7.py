"""
 Task_7:
Дан список из строк.
Используя join, соедините строки так, чтобы они были разделены через запятую.
На выходе должна получиться строка в виде "my_string1,my_string2,my_string3"
"""


def get_string_from_list(mlist):
	mstr = ','.join(mlist)
	return mstr


print(get_string_from_list(['my_string1', 'my_string2', 'my_string3']))
