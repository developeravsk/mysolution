import pandas as pd
from math import dist, sqrt
import os, sys

#Add parent dir and sub dirs to the python path for importing the modules from different directories
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
rootdir = os.path.dirname(parentdir)
sys.path.extend([rootdir, parentdir])

class Calculation():
    def __init__(self):
        """Reading co-ordinates.csv and cewntroids.csv inside data folder
        """
        self.coordinates=pd.read_csv("data/coordinates.csv")
        self.centroids=pd.read_csv("data/centroids.csv")
    
    def calculate(self, K, N, measure):
        """This function calculates the number of points which are 
        within certain meters of at least one of the centroid

        Args:
            K (int): Number of centroids to be considered (Max K = 1000)
            N (int): Numner of co-ordinates to be considered (Max N = 1,000,000)
            measure (int): radius (in meters)

        Returns:
            int: Count of co-ordinates which are within certain distance of at least
            one of the centroid
        """
        cent_df=self.centroids[:K]
        points_df=self.coordinates[:N]
        count=0
        for index1, value1 in cent_df.iterrows():
            for index2,value2 in points_df.iterrows():
                if(dist(value2, value1)<=measure):
                    count=count+1
                    points_df.drop([index2])
                    break
        return count

    def minimum_radius(self,K, N):
        """This function calculates the minimum radius such that 80% of the provided number of coordinates are within 
        calculated radius metres of at leas one of K provided centroids

        Args:
            K (int): Number of centroids to be considered (Max K = 1000)
            N (int): Numner of co-ordinates to be considered (Max N = 1,000,000)

        Returns:
            int: minimum radius such that 80% of the provided number of coordinates are within 
        calculated radius metres of at leas one of K provided centroids
        """
        cent=self.centroids[:K]
        points=self.coordinates[:N]
        k=int(N*0.8)
        dis=[0]*N
        for index0, value0 in cent.iterrows():
            for index1, value1 in points.iterrows():
                dis[index1]=sqrt((value1[0]-value0[0])**2+(value1[1]-value0[1])**2)
            dis.sort()
        print(dis)
        return dis[k-1]