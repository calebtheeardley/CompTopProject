from cmath import inf
import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use("QtAgg")

def low(matrix: np.matrix, collumn: int):
    rows: int = matrix.shape[0]

    for i in range(rows-1, -1, -1):
        if(matrix[i,collumn] != 0):
            return i
        
    return(-1)

def add_collums(matrix:np.matrix, collumn1:int, collumn2:int):
    rows: int = matrix.shape[0]

    for i in range(rows):
        matrix[i,collumn2] = (matrix[i,collumn1]+matrix[i,collumn2]) % 2

def filtration_to_matrix(filtration: list[set]) -> np.matrix:
    n: int = len(filtration)
    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if(len(filtration[i])+1 == len(filtration[j])):
                i_in_j: bool = True
                for v in filtration[i]:
                    if(v not in filtration[j]):
                        i_in_j = False
                        break
                if(i_in_j):
                    matrix[i,j] = 1

    return matrix


def compute_persistence(matrix: np.matrix):
    print("computing persistence")
    rows: int = matrix.shape[0]
    collumns: int = matrix.shape[1]

    lowOf: list = []

    i=0
    for j in range(collumns):
        lowOf.append(low(matrix=matrix, collumn=j))
        print(str(j*100/collumns)+"%")


        done: bool = False
        j2: int = 0
        while(not done):
            if(j == j2):
                done = True
            elif(lowOf[j] == lowOf[j2] and lowOf[j]>=0):
                add_collums(matrix=matrix, collumn1=j2, collumn2=j)
                lowOf[j] = low(matrix=matrix, collumn=j)
                j2 = 0
            else:
                j2 += 1

def generate_persistence_diagram(matrix:np.matrix, threshold_dict: dict, title: str="Persistence Diagram"):
    plt.close()
    collumns: int = matrix.shape[1]

    x: list[int] = []
    y: list[int] = []

    for j in range(collumns):
        collumn_low: int = low(matrix=matrix, collumn=j)
        if(collumn_low >= 0):
            x.append(threshold_dict[collumn_low])
            y.append(threshold_dict[j])

    points = list(zip(x, y))
    unique_points = set(points)
    counts = [points.count(p) for p in unique_points]

    # Plot scatter plot with circles around replicated points
    plt.figure(figsize=(8, 6))

    for p, count in zip(unique_points, counts):
        if count > 1:
            circle = plt.Circle(p, count * 0.01, color='red', fill=False)
            plt.gca().add_patch(circle)

    plt.scatter(x,y)
    
    plt.xlabel('Birth')
    plt.ylabel('Death')
    plt.title(title)
    # plt.xlim(0, max(x))  # Example for setting x-axis limits
    # plt.ylim(0, max(x))
    # plt.xticks(np.arange(0, collumns-1, 1))  # Set tick positions at integers from 0 to 4
    # plt.yticks(np.arange(0, collumns-1, 1))

    plt.show()

def generate_H0_Barcode(matrix: np.matrix, filtration: list[set], threshold_dict: dict, title:str = "Persistence Barcode"):
    plt.close()
    collumns: int = matrix.shape[1]
    start: list = [0]
    end: list = [inf]
    homology: list = [-1]

    for j in range(collumns):
        collumn_low: int = low(matrix=matrix, collumn=j)
        if(collumn_low >= 0 and len(filtration[collumn_low])==1):
            start.append(threshold_dict[collumn_low])
            end.append(threshold_dict[j])
            homology.append(threshold_dict[j])

    # Plot persistence barcode
    plt.barh(homology, end, left=start, height=3)

    # Add labels and title
    plt.xlabel('Threshold')
    plt.ylabel('H_0')
    plt.yticks([])
    plt.title(title)
    plt.show()

def generate_H1_Barcode(matrix: np.matrix, filtration: list[set], threshold_dict: dict, title:str = "Persistence Barcode"):
    plt.close()
    collumns: int = matrix.shape[1]
    start: list = [0]
    end: list = [inf]
    homology: list = [-1]

    for j in range(collumns):
        collumn_low: int = low(matrix=matrix, collumn=j)
        if(collumn_low >= 0 and len(filtration[collumn_low])==2):
            start.append(threshold_dict[collumn_low])
            end.append(threshold_dict[j])
            homology.append(threshold_dict[j])

    # Plot persistence barcode
    plt.barh(homology, end, left=start, height=.5)

    # Add labels and title
    plt.xlabel('Threshold')
    plt.ylabel('H_1')
    plt.yticks([])
    plt.title(title)
    plt.show()