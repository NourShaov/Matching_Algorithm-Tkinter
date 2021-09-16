# this algorithm shows us that the man prefare a woman, but the woman does not prefare him(she prefare another one) so they will break up
def break_engagement(person):
	breakingWith = is_engaged_to(person)
	for m in males:
		if m["name"] == person:
			if m["engaged_to"] != "":
				m["engaged_to"] = ""
				m["is_free"] = True
				print("{} is breaking with {}.".format(person, breakingWith))
				str_out_2.append("{} is breaking with {}.".format(person, breakingWith))

	for f in females:
		if f["name"] == person:
			if f["engaged_to"] != "":
				f["engaged_to"] = ""
				m["is_free"] = True
				print("{} is breaking with {}.".format(person, breakingWith))
				str_out_2.append("{} is breaking with {}.".format(person, breakingWith))


# here we can know the name of person who engaged
def is_engaged_to(person):
	for m in males:
		if m["name"] == person:
			return m["engaged_to"]

	for f in females:
		if f["name"] == person:
			return f["engaged_to"]

	return False


# this algorithm show us if someone is engaged or not
def is_engaged(person):
	for m in males:
		if m["name"] == person:
			if m["engaged_to"] != "":
				return True

	for f in females:
		if f["name"] == person:
			if f["engaged_to"] != "":
				return True

	return False


# if the person is engaged it will show us if the partner is the beat choice or not
# candidate1 is current partner , candidate2 is the best choice
def best_coice(person, candidate1, candidate2):
	for m in males:
		if m["name"] == person:
			for x in range(0, len(males)):
				if candidate1 == m["preferences"][x]:
					return candidate1
				if candidate2 == m["preferences"][x]:
					return candidate2

	for f in females:
		if f["name"] == person:
			for x in range(0, len(males)):
				if candidate1 == f["preferences"][x]:
					return candidate1
				if candidate2 == f["preferences"][x]:
					return candidate2


# here we put two partner in engagement, and we add them to non free
def engage(male, female):
	for m in males:
		if m["name"] == male:
			m["engaged_to"] = female
			m["is_free"] = False

	for f in females:
		if f["name"] == female:
			f["engaged_to"] = male
			f["is_free"] = False


def get_name_from_ranking(male, rank):
	for m in males:
		if m["name"] == male:
			return m["preferences"][rank]


def main():
	while (True):
		numberOfPairs = len(males)
		nop = 1
		for m in males:
			male = m["name"]
			if (m["is_free"] == False) and (len(m["proposed_to"]) != numberOfPairs):
				nop += 1
				if nop == numberOfPairs:
					print("\n\n\nSuccess!")
					return

			for x in range(0, numberOfPairs):
				if not is_engaged(male):
					if x not in m["proposed_to"]:  # we can know who proposed
						m["proposed_to"].append(x)

						woman = get_name_from_ranking(male, x)

						if is_engaged(woman):
							currentManOfTheEngaged = is_engaged_to(woman)

							betterChoice = best_coice(
								woman, currentManOfTheEngaged, male)

							engage(betterChoice, woman)

							if betterChoice != currentManOfTheEngaged:
								break_engagement(currentManOfTheEngaged)
						else:
							engage(male, woman)


def results():
	global str_out
	print("Resolution:\n")
	str_out = ["\nSuccess!", "Resolution:\n", ]
	for m in males:
		male = m["name"]
		female = m["engaged_to"]
		print("{} <---> {}".format(male, female))
		str_out.append("{} <---> {}".format(male, female))


from tkinter import *
from tkinter import messagebox

males = [
	{
		"name": "A",
		"is_free": True,
		"gender": "male",
		"preferences": ["1", "2", "3", "4", "5", "6"],
		"engaged_to": "",
		"proposed_to": [],
	},
	{
		"name": "B",
		"is_free": True,
		"gender": "male",
		"preferences": ["2", "3", "5", "1", "4", "6"],
		"engaged_to": "",
		"proposed_to": [],
	},
	{
		"name": "C",
		"is_free": True,
		"gender": "male",
		"preferences": ["2", "3", "1", "5", "4", "6"],
		"engaged_to": "",
		"proposed_to": [],
	},
	{
		"name": "D",
		"is_free": True,
		"gender": "male",
		"preferences": ["2", "3", "1", "5", "4", "6"],
		"engaged_to": "",
		"proposed_to": [],
	},
	{
		"name": "E",
		"is_free": True,
		"gender": "male",
		"preferences": ["1", "3", "2", "5", "4", "6"],
		"engaged_to": "",
		"proposed_to": [],
	},
	{
		"name": "F",
		"is_free": True,
		"gender": "male",
		"preferences": ["2", "3", "1", "5", "4", "6"],
		"engaged_to": "",
		"proposed_to": [],
	},
]

females = [
	{
		"name": "1",
		"is_free": True,
		"gender": "female",
		"preferences": ["A", "B", "C", "E", "D", "F"],
		"engaged_to": "",
		"proposed_to": [],
	},
	{
		"name": "2",
		"is_free": True,
		"gender": "female",
		"preferences": ["C", "A", "B", "D", "E", "F"],
		"engaged_to": "",
		"proposed_to": [],
	},
	{
		"name": "3",
		"is_free": True,
		"gender": "female",
		"preferences": ["C", "A", "B", "D", "E", "F"],
		"engaged_to": "",
		"proposed_to": [],
	},
	{
		"name": "4",
		"is_free": True,
		"gender": "female",
		"preferences": ["A", "B", "C", "E", "D", "F"],
		"engaged_to": "",
		"proposed_to": [],
	},
	{
		"name": "5",
		"is_free": True,
		"gender": "female",
		"preferences": ["A", "B", "C", "E", "D", "F"],
		"engaged_to": "",
		"proposed_to": [],
	},
	{
		"name": "6",
		"is_free": True,
		"gender": "female",
		"preferences": ["B", "A", "C", "D", "F", "E"],
		"engaged_to": "",
		"proposed_to": [],
	},
]


# المدخلات من النيمز و البريف
class Create_entries:
	def __init__(self, root, row, col, txt):
		self.root, self.row, self.col, self.txt = root, row, col, txt
		Label(self.root, text=self.txt, bg='White', fg='Black', font=('verdana', 10)).place(x=self.row, y=self.col)
		self.e = Entry(self.root)
		self.e.place(x=(self.row + 70), y=self.col)

	def give_text(self):
		self.out = self.e.get()
		return self.out


def make(root, text, initial, specify):
	col = initial
	for i in range(6):
		if specify == True:
			lis_main_male.append(Create_entries(root, 2, col, text + str(i)))
		if specify == False:
			lis_main_female.append(Create_entries(root, 2, col, text + str(i)))
		col += 25


class Pref_wind:
	def __init__(self, male_names, female_names):
		self.male_names, self.female_names = male_names, female_names
		self.pref = Tk()
		self.pref.title("Matching Alogrithm")
		self.pref.geometry('500x500')
		Label(self.pref, text='Prefrences', bg='White', fg='Black', font=('verdana', 20)).pack()
		Label(self.pref, text='Initiator pref: ', bg='White', fg='Black', font=('verdana', 15)).place(x=0, y=30)

		self.str = ''
		for i in pref_male:
			self.str = self.str + i + ' , '

		Label(self.pref, text='Options:  ' + self.str, bg='White', fg='Black', font=('verdana', 10)).place(x=0, y=55)
		Label(self.pref, text='Reciver pref:  ', bg='White', fg='Black', font=('verdana', 15)).place(x=0, y=240)

		self.str = ''
		for i in pref_female:
			self.str = self.str + i + ' , '

		Label(self.pref, text='Options:  ' + self.str, bg='White', fg='Black', font=('verdana', 10)).place(x=0, y=265)

		make(self.pref, 'Initiator ', 85, True)
		make(self.pref, 'Reciver ', 290, False)

		Button(self.pref, text='STATUS', bg='Gold', fg='black', font=('verdana', 12), command=self.pop_up).place(x=200,
		                                                                                                         y=460)
		self.pref.mainloop()

	def pop_up(self):
		self.a = [i.give_text() for i in lis_main_male]
		self.b = [i.give_text() for i in lis_main_female]

		self.a_2 = [i.split(',') for i in self.a]
		self.b_2 = [i.split(',') for i in self.b]

		self.m = list(zip(self.male_names, self.a_2))
		self.f = list(zip(self.female_names, self.b_2))
		self.m_counter, self.f_counter = False, False

		for i in self.a_2:
			if len(i) != 6:
				self.m_counter = True
				break
			for j in i:
				if j not in self.female_names:
					self.m_counter = True
					break
		for i in self.b_2:
			if len(i) != 6:
				self.f_counter = True
				break
			for j in i:
				if j not in self.male_names:
					self.f_counter = True
					break
		if self.m_counter != True and self.f_counter != True:
			if '' not in self.a and '' not in self.b:
				self.counter = 0
				for k in males:
					k['name'] = self.m[self.counter][0]
					k['preferences'] = self.m[self.counter][-1]
					self.counter += 1
				self.counter = 0
				for k in females:
					k['name'] = self.f[self.counter][0]
					k['preferences'] = self.f[self.counter][-1]
					self.counter += 1

				self.pop = Toplevel(self.pref)
				self.pop.title("Results")
				self.pop.geometry('400x400')
				Label(self.pop, text='Matching Results', bg='White', fg='Black', font=('verdana', 20)).pack()
				run()
				self.str = ''
				for i in str_out_2:
					self.str = self.str + i + '\n'
				for i in str_out:
					self.str = self.str + i + '\n'
				Label(self.pop, text=self.str, bg='White', fg='Black', font=('verdana', 15)).place(x=60, y=50)
			else:
				messagebox.showinfo('Warning', 'Prefrences Missing , Kindly enter all of them ! ')

		else:
			messagebox.showinfo('Warning',
			'The Credentials entered are not in prefrences' + '\n' + 'OR you entered less preferences for some character !!')
			self.m_counter, self.f_counter = False, False


def run():
	main()
	results()


def new_class(main_root):
	global pref_male, pref_female
	pref_male = [i.give_text() for i in lis_main_female]
	pref_female = [j.give_text() for j in lis_main_male]

	if '' not in pref_female and '' not in pref_male:
		main_root.destroy()
		lis_m, lis_f = pref_female, pref_male
		lis_main_female.clear()
		lis_main_male.clear()
		p = Pref_wind(lis_m, lis_f)
	else:
		messagebox.showinfo('Warning', 'Credentials Missing , Kindly enter all of them ! ')


lis_main_male, lis_main_female = [], []
str_out_2 = []
app = Tk()
app.title("Matching Algorithm")
app.geometry('500x500')
Label(app, text='Matching App', bg='White', fg='Black', font=('verdana', 20)).pack()
Label(app, text='Initiator names:   ', bg='White', fg='Black', font=('verdana', 15)).place(x=0, y=40)
Label(app, text='Reciver names:   ', bg='White', fg='Black', font=('verdana', 15)).place(x=0, y=225)

make(app, 'Reciver ', 255, False)
make(app, 'Initiator ', 70, True)

Button(app, text='Prefrence', bg='Gold', fg='black', font=('verdana', 12), command=lambda: new_class(app)).place(x=200,
                                                                                                                 y=450)

app.mainloop()