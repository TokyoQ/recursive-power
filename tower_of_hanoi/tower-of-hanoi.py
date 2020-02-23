class TowerOfHanoi:
    """
    Recursive Towers of Hanoi
    It codes exactly how you think about the problem.
        - Move everything above the nth disc to the temporary tower
        - Move the nth disc to the desired tower
        - Move all of the other discs back on top of the one you just moved
    """    
    def __init__(self, num_discs):
        self.num_discs = num_discs
        self.moves = []
        self.num_moves = 0
    
    def add_move(self, move):
        self.moves.append(move)
        print(move)

    def move(self, num_discs, from_tower, to_tower, using_tower):
        if (num_discs == 1):
            self.num_moves += 1
            move = f"Moved disc from {from_tower} to {to_tower} via {using_tower}"
            self.add_move(move)
        else:
            self.move(num_discs-1, from_tower, using_tower, to_tower)
            self.move(1, from_tower, to_tower, using_tower)
            self.move(num_discs-1, using_tower, to_tower, from_tower)
        return self.moves


if __name__ == '__main__':
    num_discs = int(input("How many starting discs? "))
    
    toh = TowerOfHanoi(num_discs)
    toh.move(num_discs, "A", "C", "B")

    print(f"Total moves: {toh.num_moves}")