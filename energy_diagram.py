import matplotlib.pyplot as plt
from energydiagram import ED

diagram = ED()
diagram.add_level(0, 'Separated Reactants')
diagram.add_level(-5.4, 'mlC1')
diagram.add_level(-15.6, 'mlC2', 'last', )  # Using 'last'  or 'l' it will be together with the previous level
diagram.add_level(28.5, 'mTS1', color='g')
diagram.add_level(-9.7, 'mCARB1')
diagram.add_level(-19.8, 'mCARB2', 'l')
diagram.add_level(20, 'mCARBX', 'last')
diagram.plot(show_IDs=True)

diagram.add_link(0, 1)
diagram.add_link(0, 2)
diagram.add_link(2, 3)
diagram.add_link(1, 3)
diagram.add_link(3, 4)
diagram.add_link(3, 5)
diagram.add_link(0, 6)
diagram.plot(ylabel="Energy / $kcal$ $mol^{-1}$")  # this is the default ylabel
plt.show()
