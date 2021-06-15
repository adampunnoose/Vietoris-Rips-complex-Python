# Vietoris-Rips-complex-Python
Vietoris-Rips complex algorithm coded in the Python language

# Vietrois-Rips complex description 
  The Vietoris-Rips complex is an abstract simplicial complex used in topological studies to help better characterize large datasets. This description will explain the basics of this concept. The user inputs a dataset (X) and a radius value (R). 

  A simplicial complex is a collection of points and simplexes in space. A simplex is a connection of points and faces. A single point is considered a 0-simplex, 2 points connected by a line is a 1-simplex, and collection of 3 points and the face that fills in that space is considered a 2-simplex and a collection of 5 points and the tetrahedral associated made by those points is a 3-simplex. For the purposes of this program, we will only be looking at the 0 to 3 simplicial complexes made by given datasets.

  When constructing these simplicial complexes, connecting multiple points together does not automatically lead a new simplex. The shape within these points must be explicitly filled in in order to be considered a simplex. Distances between points are also not considered when making these complexes, this is where the Vietoris-Rips complex comes in. The Vietoris-Rips complex creates circles of radius R around each point, if a point is within another points circle, the points are connected and make a 1 simplex. If multiple points are connected is such a way that make a simplex higher than a one simplex, the space within is filled in automatically and considered another simplex. This program simulates this process with a user entered dataset and a user entered radius R value, and gives the user a list of all complexes found within this dataset using the Vietoris rips complex. 

# Program Operation 
  The whole program is contained in the file “VRC.py”. This file reads its data from the file “Points Template.csv”, an example of this file’s operation is located in the file “Points Template Example.csv”. This program requires the “pandas” package to run. The user needs to call the VRC class and input the data file path, and then the user needs to call the “calculateVRC()” function within the class and input the desired radius value. The program then outputs all the points used and the simplexes found. 

