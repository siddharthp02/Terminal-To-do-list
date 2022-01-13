def get_notes():
	my_file = open('/home/siddharthp/Desktop/notes/to_do_list.txt','a+')
	my_file.seek(0)
	list1 = my_file.readlines()
	my_file.close()
	
	return list1

def display(notes_list):
	if len(notes_list) == 0:
		print('EMPTY')
	else:
		for i in notes_list:
			print(f'{notes_list.index(i)+1}. {i}')

def add_note():
	note = input('Note: ')
	note = '\n'+note
	notes.append(note)

def del_note():
	num = int(input('Delete note no: '))
	notes.pop(num-1)

def update_notes():
	
	my_file = open('/home/siddharthp/Desktop/notes/to_do_list.txt','w+')
	for line in notes:
		my_file.write(line)
	my_file.close()

def set_priority(notes_list):
	order = list(map(int,input('Set priority order with spaces in between: ').split()))
	temp = []
	if len(order)==len(notes_list):

		for n in order:
			temp.append(notes_list[n-1])
		return temp
	else:
		pass


on = True
notes = get_notes()
display(notes)

while on:
	
	answer = input('\nAdd note(a)/Delete note(d)/show notes(s)/set priority order(p)/quit(q) :')

	if answer == 'a':
		add_note()
	elif answer == 'd':
		del_note()
	elif answer == 's':
		display(notes)
	elif answer == 'c':
		clear_notes()
	elif answer == 'p':
		notes = set_priority(notes)
	elif answer == 'q':
		update_notes()
		on = False


