# Day 6 Part 1
import pandas as pd
import sys

sys.setrecursionlimit(10000)

# Read the input file
with open('2024-12-06/input6.txt', 'r') as f:
    lines = f.readlines()

map_df = pd.DataFrame([list(line) for line in lines])
map_df = map_df.drop(map_df.columns[130], axis = 1)

stack_loc = map_df.isin(["^"]).stack()
start_loc = stack_loc[stack_loc].index.tolist()
start_orientaion = "up"

# make class to keep track of piece
class Piece:
    def __init__(self, row_start, column_start, orientation):
        self.row = row_start
        self.column = column_start
        self.next_row = None
        self.next_column = None
        self.orientation = orientation
        self.locs = set([])

    def get_next_move(self):
        if self.orientation == "up":
            self.next_row = self.row - 1
            self.next_column = self.column
        elif self.orientation == "down":
            self.next_row = self.row + 1
            self.next_column = self.column
        elif self.orientation == "left":
            self.next_column = self.column - 1
            self.next_row = self.row
        elif self.orientation == "right":
            self.next_column = self.column + 1
            self.next_row = self.row
        # test if new_loc on map
        if 0 > self.next_column or self.next_column > map_df.shape[1] - 1 or 0 > self.next_row or self.next_row > map_df.shape[0] - 1:
            return "done"
        # test if obstacle in new_loc
        elif map_df.iloc[self.next_row, self.next_column] == "#":
            return "obstacle"
        elif map_df.iloc[self.next_row, self.next_column] == ".":
            return "advance"
    
    def turn(self):
        if self.orientation == "up":
            self.orientation = "right"
        elif self.orientation == "right":
            self.orientation = "down"
        elif self.orientation == "down":
            self.orientation = "left"
        elif self.orientation == "left":
            self.orientation = "up"
        
        return self


    def move(self):
        self.locs.add((self.row, self.column))
        next_move = self.get_next_move()
        if next_move == "done":
            print(len(self.locs))
            return self.locs # len(self.locs)
        elif next_move == "obstacle":
            self.turn()
            next_move = self.get_next_move()
            self.move()
        elif next_move == "advance":
            self.column = self.next_column
            self.row = self.next_row
            print(self.row, self.column, self.orientation)
            self.move()
            

test = Piece(row_start=start_loc[0][0], column_start=start_loc[0][1], orientation=start_orientaion)

test.move()
