import random
import pygame
from pygame.locals import *
# import statistics
# import sys
import argparse



def bubbleSortV1(given_list):
    n = 0
    for i in range(1, len(given_list)):
        for j in range(0, len(given_list) - 1):
            if given_list[j] > given_list[j + 1]:
                temp = given_list[j + 1]
                given_list[j + 1] = given_list[j]
                given_list[j] = temp
            update(given_list, (j, j+1))

            n += 1
    print(f"Time: {n}")
    return given_list

# Extra optimisation that stops the algorithm if no swaps are made
def bubbleSortV2(given_list):
    n = 0
    swapped = True
    while swapped:
        swapped = False 
        for j in range(0, len(given_list) - 1):
            if given_list[j] > given_list[j + 1]:
                temp = given_list[j + 1]
                given_list[j + 1] = given_list[j]
                given_list[j] = temp
                swapped = True
            update(given_list, (j, j+1))
            n += 1
    print(f"Time: {n}")
    return given_list

# Another optimisation that doesn't consider the sorted sublist at the end
def bubbleSortV3(given_list):
    n = 0
    swapped = True
    pass_num = 1
    while swapped:
        swapped = False
        for j in range(0, len(given_list) - pass_num):
            if given_list[j] > given_list[j + 1]:
                temp = given_list[j + 1]
                given_list[j + 1] = given_list[j]
                given_list[j] = temp
                swapped = True
            update(given_list, (j, j+1))
            n += 1
        pass_num += 1
    print(f"Time: {n}")
    return given_list



def quickSort(items, start, end):
    # The recursion will stop when the partition contains a single item
    if start >= end:
        return

    # Otherwise recursively call the function
    else:
        pivot_value = items[start]
        # (statistics.median(items[start:end]))
        
        
        low_mark = start + 1
        high_mark = end
        finished = False

        # Repeat until the low and high values have been swapped
        while not finished:

            # Moving left pivot
            while low_mark <= high_mark and items[low_mark] <= pivot_value:
                low_mark += 1
                update(items, (low_mark, high_mark, pivot_value))
            # Moving right pivot
            while low_mark <= high_mark and items[high_mark] >= pivot_value:
                high_mark -= 1
                update(items, (low_mark, high_mark, pivot_value))

            
            # Checking that the markers don't overlap
            if low_mark < high_mark:
                # Swap the values at low and high
                temp = items[low_mark]
                items[low_mark] = items[high_mark]
                items[high_mark] = temp
                update(items, (low_mark, high_mark, pivot_value))

            # If they do then end the loop
            else:
                finished = True

        temp = items[high_mark]
        items[high_mark] = items[start]
        items[start] = temp

        quickSort(items, start, high_mark - 1)
        quickSort(items, high_mark + 1, end)
    return items


def bubbleSort(given_list):
    swapped = True
    num = 1
    while swapped:
        swapped = False
        for i in range(len(given_list) - num):
            if given_list[i] > given_list[i + 1]:
                temp = given_list[i]
                given_list[i] = given_list[i + 1]
                given_list[i + 1] = temp
                swapped = True
                update(given_list, (i, i+1))
                
        num += 1
    return given_list

def insertionSort(given_list):
    index = 0
    for i in range(1, len(given_list)):
        index = i
        temp = given_list[i]
        while index > 0 and temp < given_list[index-1]:
            given_list[index] = given_list[index - 1]
            index -= 1
            update(given_list,(index, -1))
        given_list[index] = temp


# Iterative merge sort solution
def mergeSort(a):
    # start with least partition size of 2^0 = 1
    width = 1   
    n = len(a)                                         
    # subarray size grows by powers of 2
    # since growth of loop condition is exponential,
    # time consumed is logarithmic (log2n)
    while (width < n):
        # always start from leftmost
        l=0;
        while (l < n):
            r = min(l+(width*2-1), n-1)        
            m = min(l+width-1,n-1)
            # final merge should consider
            # unmerged sublist if input arr
            # size is not power of 2             
            merge(a, l, m, r)
            l += width*2
        # Increasing sub array size by powers of 2
        width *= 2
    return a
   
# Merge Function
def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]
 
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
            update(a, (-1, k))
            
        else:
            a[k] = R[j]
            j += 1
            update(a, (-1, k))

        k += 1
 
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
        update(a, (-1, k))

 
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
        update(a, (-1, k))



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1920


algorithms = ["bubble_sort1", "bubble_sort2", "bubble_sort3", "insertion_sort", "quick_sort", "merge_sort"]


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--algorithm', required=True, type=str, help="Name of algorithm you want to use", choices=algorithms)

parser.add_argument('-f', '--framerate', required=False, type=int, help="Maximum number of frames per second for sorting algorithm")

parser.add_argument('-s', '--size', required=False, type=int, help="Size of array to be sorted")


updates = 0


def update(list, highlight):
    global updates
    updates += 1
    running = True
    time = 0
    while running:
        x = 0
        screen.fill(BLACK)
        for i in range(len(list)):
            if i in highlight:
                colour = RED
            else:
                colour = WHITE
            pygame.draw.rect(screen, (colour), (x, 1000 - (list[i] * 1000/list_size), width, list[i] * 1000/list_size), 0)
            x += width + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
        pygame.display.flip()
        clock.tick(fps)
        time += 1
        # if time >= 0:
        running = False




if __name__ == "__main__":
    args = parser.parse_args()

    rn = random.Random()
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(BLACK)
    pygame.display.set_caption("sort")
    clock = pygame.time.Clock()

    if args.framerate:
        fps = args.framerate
    else:
        fps = 1000
        

    if args.size:
        list_size = int(args.size)
    else:
        list_size = int(960)

    list = []
    width = SCREEN_WIDTH // list_size - 1
    for i in range(list_size):
        # list.append(rn.randint(0, list_size))
        list.append(i)
    # print(list)
    rn.shuffle(list)
    print("\n\n")
    match args.algorithm:
        case "bubble_sort1":
            bubbleSortV1(list)
        case "bubble_sort2":
            bubbleSortV2(list)
        case "bubble_sort3":
            bubbleSortV3(list)
        case "insertion_sort":
            insertionSort(list)
        case "quick_sort":
            quickSort(list, 0, len(list)-1)
        case "merge_sort":
            mergeSort(list)
    print(f"\n\nNumber of updates: {updates}")
    pygame.quit()


        




