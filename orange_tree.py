# Orange Tree Lab

class OrangeTree():
    def __init__(self, type):
        super().__init__()
        self.oranges = []
        self.type = type
        self.grow_oranges()
        print('You created a {} tree with {} oranges'.format(self.type, len(self.oranges)))


    def grow_oranges(self):
        for num in range(1, 10):
                diameter = 10
                ripeness = 1
                if self.type == 'Navel':
                    orange = NavelOrange(diameter, ripeness)
                elif self.type == 'Valencia':
                    orange = ValenciaOrange(diameter, ripeness)
                else:
                    orange = Orange(diameter, ripeness)
                self.oranges.append(orange)


class Orange():
	def __init__(self, diameter, ripeness):
		self.diameter = diameter
		self.ripeness = ripeness

	def ripen(self):
		self.ripeness += 1
		print("ripeness is now {} out of 5".format(self.ripeness))


class ValenciaOrange(Orange):
    def __init__(self, diameter, ripeness):
        Orange.__init__(self, diameter, ripeness)

    def juice(self):
        print('Now you can make tasty orange juice')

class NavelOrange(Orange):
    def __init__(self, diameter, ripeness):
        Orange.__init__(self, diameter, ripeness)

    def remove_lint(self):
        print('Please shave this orange before eating')



myTree = OrangeTree('Valencia')
myTree.grow_oranges()
print(myTree.oranges[0].ripen())
print(myTree.oranges[0].juice())
print(type(myTree.oranges[0]))

myTree = OrangeTree('Navel')
myTree.grow_oranges()
print(myTree.oranges[0].ripen())
print(myTree.oranges[0].remove_lint())
print(type(myTree.oranges[0]))
