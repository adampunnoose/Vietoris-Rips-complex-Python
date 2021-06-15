#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:50:30 2021

@author: adam
"""

#This program calculates the Vietoris-Rips Complex for 2 and 3 
#dimensional points
import pandas as pd

class VRC: 
    
    
    
    def __init__(self, path):
        #read template and import data into project space
        data = pd.read_csv(path)
        self.numDimensions = int(data.values[0,0]);
        self.points = []
        self.numPoints = int(data.values[0,1]);
        if(self.numDimensions == 3 or self.numDimensions == 2):
            self.points = self.ExtractPoints(self.numPoints, self.numDimensions, data)
        else: 
            print("Please pick either 2 or 3 dimensions")
            
        
        
    def ExtractPoints(self, numPoints,dimensions, data):
        output = []
        if dimensions == 3:
           for i in range(numPoints):
               insert = [data.values[i,2], data.values[i,3], data.values[i,4]]
               output.append(insert)
        elif dimensions == 2:
            for i in range(numPoints):
               insert = [data.values[i,2], data.values[i,3], 0]
               output.append(insert)
        return output
        
    def distP(self, p1, p2):
        #input: 2 arrays of size = 3
        #output: distance between points
        distance = ( ((p1[0] - p2[0])**2) + 
                     ((p1[1] - p2[1])**2) +
                     ((p1[2] - p2[2])**2)  )**(.5)
        return distance;
    def maxDist(self):
        #intput: list of points
        #output: array: [max distance, point1, point2]
        maxD = 0
        point1 = -1
        point2 = -1
        distance = -1
        
        for x in range(len(self.points)):
            for y in range(x + 1, len(self.points)):
                distance = self.distP(self.points[x], self.points[y])
                if distance > maxD:
                    maxD = distance
                    point1 = x
                    point2 = y
        ans = [maxD, point1, point2]
        return ans
    
    def minDist(self):
        #intput: list of points
        #output: array: [minimum distance, point1, point2]
            
        minD = 11.7e308
        point1 = -1
        point2 = -1
        distance = -1
        
        for x in range(len(self.points)):
            for y in range(x + 1, len(self.points)):
                distance = self.distP(self.points[x], self.points[y])
                if distance < minD:
                    minD = distance
                    point1 = x
                    point2 = y
        ans = [minD, point1, point2]
        return ans
    
    def edges(self, points, R):
        #input: points list and R
        #output: List of all edges 
        
        group1 = []
        
        for x in range(len(points)):
            group2 = []
            for y in range(x + 1, len(points)):
                if self.distP(points[x], points[y]) <= R:
                    group2.append(y)
            
            group1.append(group2)
            
        return group1
    
    def edgeTable(self, edgeList):
        #input: edge list from "edges" function
        #output: n by n table displaying all connected edges
            #n = number of points in the list of points 
        
        
        table = [[False]*len(edgeList) for _ in range(len(edgeList))]
        
        for x in range(len(edgeList)):
            for y in range(len(edgeList[x])):
                
                table[x][edgeList[x][y]] = True
        return table
    
    def tableSimplexComparison(self, array, table,  tableColumn):
        #intput: 
            #array = simplex to be tested 
            #table = n by n table of edges
            #tableColumn = point to be checked if it is connected to simplicie in array
        #output: boolean, true if point is connected to inputted simplicie
        
        output = True
        for i in range(len(array)):
            if(table[tableColumn][array[i]] != True):
                output = False
        return output
    
    def insertionArray(self, array, j):
        insertion = []
        insertion.append(j)
        
        for i in range(len(array)):
            insertion.append(array[i])
        return insertion
    
    
    def zeroSimplex(self, edgeList):
        output = []
        for x in range(len(edgeList)):
            output.append(x)
        return output
    
    def oneSimplex(self, edgeList):
        output = [];
        
        for x in range(len(edgeList)):
            if len(edgeList[x]) != 0:
                for y in range(len(edgeList[x])):
                    insertion = [];
                    insertion.append(x)
                    insertion.append(edgeList[x][y])
                    output.append(insertion)
        return output
    
    def twoPlusSimplex(self, simplexList, EdgeTable, simplex):
        output = []
        if simplex < 2:
            print("Must input a simplex value of 2 or more")
        else:
            for i in range(len(simplexList)): #iterated for every simplex in inputted list
                for j in range(simplexList[i][0], -1, -1):
                    if self.tableSimplexComparison(simplexList[i], EdgeTable, j) == True:
                        output.append(self.insertionArray(simplexList[i], j))
        
        return output
    
    def printResults(self):
        #print initial points
        print("list of Points: ")
        
        for i in range(len(self.points)):
            print("Point " , i ,": " , self.points[i])
        print("\n Simplicies: ")
        for i in self.allSimplex:
            print(i)
                
        
    def calculateVRC(self, radius):
        #calulate Veitoris-Rips complex with the inputted value of radius
        maxList = self.maxDist()
        minList = self.minDist()
        maxD = maxList[0]
        minD = minList[0]
        self.allSimplex = []
        
        if radius >  minD:
            
        
            self.edgeList = self.edges(self.points, radius)
            self.edgeTable = self.edgeTable(self.edgeList)
            
            self.zeroSimplexV = self.zeroSimplex(self.edgeList)
            self.oneSimplexV = self.oneSimplex(self.edgeList)
            self.twoSimplex = self.twoPlusSimplex(self.oneSimplexV, self.edgeTable, 2)
            self.threeSimplex = self.twoPlusSimplex(self.twoSimplex, self.edgeTable, 3)
            
            #combine all simplicies into one 
            self.allSimplex = self.zeroSimplexV + self.oneSimplexV + self.twoSimplex + self.threeSimplex
            self.printResults()
            
            
        else: 
            print("Please use a radius that is bigger that ", minD)
        
        
        
        
        
path= "/Users/adam/Desktop/JAVA Book/VRC Project/Points Template Example.csv"
Complex = VRC(path) #read from Template
Complex.calculateVRC(12) #calculate Vietoris-Rips Complex with a Radisu value of 12




