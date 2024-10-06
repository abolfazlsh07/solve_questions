# CodeCup City: Minimum Time for Cars to Reach Parking

This project solves a problem from CodeCup where the goal is to calculate the minimum time required for all cars to reach their respective parking spots in a grid of horizontal and vertical streets.

## Problem Description

In CodeCup City, there are `n` horizontal streets and `m` vertical streets. Each horizontal and vertical street intersects at a crossroad. 
- A car is placed at the top of each vertical street, moving downward, and there is a parking spot at the bottom.
- Another car is placed at the right end of each horizontal street, moving leftward, and there is a parking spot at the left end.

All cars start moving simultaneously at a constant speed. It takes exactly one minute for a car to move between two intersections, and half a minute for a car to reach the first intersection or to park. When two cars reach the same intersection at the same time, one of them has to wait an extra minute.

The objective is to determine the minimum time for all cars to reach their parking spots for each scenario.

## Input

- The first line of input contains an integer `t`, the number of test cases.
- Each test case consists of two integers `n` and `m`:
  - `n`: the number of horizontal streets.
  - `m`: the number of vertical streets.

## Output

For each test case, print the minimum time (in minutes) needed for all cars to reach their parking spots.



### Algorithm

1. Read the number of test cases `t`.
2. For each test case, read the values `n` and `m`.
3. For each test case, calculate `max(n, m)` and print the result.


## Example

### Input:
    3

    2 3 

    4 1

    5 5

### Output

    3    
    4
    6
