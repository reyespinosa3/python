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
                if self.type == 'navel':
                    orange = NavelOrange(diameter, ripeness)
                elif self.type == 'valencia':
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
		print("ripeness is now {}".format(self.ripeness))



myTree = OrangeTree("Navel")
myTree.grow_oranges()
print(myTree.oranges)
