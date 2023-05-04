import numpy as np

ev2kjmol = 96.485
ha2kjmol = 2625.4996
kjmol2v = 1000 / 96485.33289
rhe = 3.43


def electrochem_potential(reactant, product):
    return (product - reactant) * ha2kjmol * kjmol2v - rhe


def chemical_energy(reactant, product):
    return (product - reactant) * ha2kjmol


a1_fe2 = -1112.410183
a2_fe3 = -1112.234986
b1_fe2_oh = -1188.377225
b2_fe3_oh = -1188.239690
b3_fe4_oh = -1188.070549
c2_fe3_o = -1187.743472
c3_fe4_o = -1187.626556
c4_fe5_o = -1187.432984
d3_fe2_ooh = -1263.531771
d4_fe3_ooh = -1263.396082
d5_fe4_ooh = -1263.221059
e4_fe3_oo = -1262.925779
e5_fe4_oo = -1262.785617
e6_fe5_oo = -1262.627127
oh = -75.977708
h2o = -76.448791
o2 = -150.311825

a1a2 = electrochem_potential(a1_fe2, a2_fe3)
b1b2 = electrochem_potential(b1_fe2_oh, b2_fe3_oh)
b2b3 = electrochem_potential(b2_fe3_oh, b3_fe4_oh)
c2c3 = electrochem_potential(c2_fe3_o, c3_fe4_o)
c3c4 = electrochem_potential(c3_fe4_o, c4_fe5_o)
d3d4 = electrochem_potential(d3_fe2_ooh, d4_fe3_ooh)
d4d5 = electrochem_potential(d4_fe3_ooh, d5_fe4_ooh)
e4e5 = electrochem_potential(e4_fe3_oo, e5_fe4_oo)
e5e6 = electrochem_potential(e5_fe4_oo, e6_fe5_oo)

horizon = [a1a2, b1b2, b2b3, c2c3, c3c4, d3d4, d4d5, e4e5, e5e6]
print("a1a2, b1b2, b2b3, c2c3, c3c4, d3d4, d4d5, e4e5, e5e6")
# keep 2 decimal places
print(np.round(horizon, 2))

a1b2 = electrochem_potential(a1_fe2+oh, b2_fe3_oh)
b2c3 = electrochem_potential(b2_fe3_oh+oh, c3_fe4_o+h2o)
c3d4 = electrochem_potential(c3_fe4_o+oh, d4_fe3_ooh)
d4e5 = electrochem_potential(d4_fe3_ooh+oh, e5_fe4_oo+h2o)
a2b3 = electrochem_potential(a2_fe3+oh, b3_fe4_oh)
b3c4 = electrochem_potential(b3_fe4_oh+oh, c4_fe5_o+h2o)
c4d5 = electrochem_potential(c4_fe5_o+oh, d5_fe4_ooh)
d5e6 = electrochem_potential(d5_fe4_ooh+oh, e6_fe5_oo+h2o)

diagonal = [a1b2, b2c3, c3d4, d4e5, a2b3, b3c4, c4d5, d5e6]
print("a1b2, b2c3, c3d4, d4e5, a2b3, b3c4, c4d5, d5e6")
# keep 2 decimal places
print(np.round(diagonal, 2))

a1b1 = chemical_energy(a1_fe2+oh, b1_fe2_oh)
b2c2 = chemical_energy(b2_fe3_oh+oh, c2_fe3_o+h2o)
c3d3 = chemical_energy(c3_fe4_o+oh, d3_fe2_ooh)
d4e4 = chemical_energy(d4_fe3_ooh+oh, e4_fe3_oo+h2o)
a2b2 = chemical_energy(a2_fe3+oh, b2_fe3_oh)
b3c3 = chemical_energy(b3_fe4_oh+oh, c3_fe4_o+h2o)
c4d4 = chemical_energy(c4_fe5_o+oh, d4_fe3_ooh)
d5e5 = chemical_energy(d5_fe4_ooh+oh, e5_fe4_oo+h2o)

vertical = [a1b1, b2c2, c3d3, d4e4, a2b2, b3c3, c4d4, d5e5]
print("a1b1, b2c2, c3d3, d4e4, a2b2, b3c3, c4d4, d5e5")
# keep 0 decimal places
print(np.round(vertical))

a1b2freee = a1b2 * ev2kjmol
b2c3freee = b2c3 * ev2kjmol + a1b2freee
c3d4freee = c3d4 * ev2kjmol + b2c3freee
d4e5freee = d4e5 * ev2kjmol + c3d4freee
e5a1freee = chemical_energy(e5_fe4_oo, a1_fe2+o2) + d4e5freee
e5b2freee = chemical_energy(e5_fe4_oo+oh, b2_fe3_oh+o2) + d4e5freee
a2b3freee = a2b3 * ev2kjmol
b3c4freee = b3c4 * ev2kjmol + a2b3freee
c4d5freee = c4d5 * ev2kjmol + b3c4freee
d5e6freee = d5e6 * ev2kjmol + c4d5freee
e6a2freee = chemical_energy(e6_fe5_oo, a2_fe3+o2) + d5e6freee
e6b3freee = chemical_energy(e6_fe5_oo+oh, b3_fe4_oh+o2) + d5e6freee

diagonalfreee = [a1b2freee, b2c3freee, c3d4freee, d4e5freee, e5a1freee, e5b2freee,
                 a2b3freee, b3c4freee, c4d5freee, d5e6freee, e6a2freee, e6b3freee]
print("a1b2freee, b2c3freee, c3d4freee, d4e5freee, e5a1freee, e5b2freee,"
      "a2b3freee, b3c4freee, c4d5freee, d5e6freee, e6a2freee, e6b3freee")
# keep 2 decimal places
print(np.round(diagonalfreee, 2))

applied_potential = 1.23
applied_energy = applied_potential*ev2kjmol
a1b2chem_ae = a1b2freee - applied_energy
b2c3chem_ae = b2c3freee - applied_energy*2
c3d4chem_ae = c3d4freee - applied_energy*3
d4e5chem_ae = d4e5freee - applied_energy*4
e5a1chem_ae = e5a1freee - applied_energy*4
e5b2chem_ae = e5b2freee - applied_energy*4
a2b3chem_ae = a2b3freee - applied_energy
b3c4chem_ae = b3c4freee - applied_energy*2
c4d5chem_ae = c4d5freee - applied_energy*3
d5e6chem_ae = d5e6freee - applied_energy*4
e6a2chem_ae = e6a2freee - applied_energy*4
e6b3chem_ae = e6b3freee - applied_energy*4


diagonalchem_ae = [a1b2chem_ae, b2c3chem_ae, c3d4chem_ae, d4e5chem_ae, e5a1chem_ae, e5b2chem_ae,
                   a2b3chem_ae, b3c4chem_ae, c4d5chem_ae, d5e6chem_ae, e6a2chem_ae, e6b3chem_ae]
print("a1b2chem_ae, b2c3chem_ae, c3d4chem_ae, d4e5chem_ae, e5a1chem_ae, e5b2chem_ae,"
      "a2b3chem_ae, b3c4chem_ae, c4d5chem_ae, d5e6chem_ae, e6a2chem_ae, e6b3chem_ae")
# keep 2 decimal places
print(np.round(diagonalchem_ae, 2))

