from random import randint

print ("Welcome to Battleships online game")

# funcion needed to validate inputs

name = "Ty"
size = 8
num_ships = 3

class Board:
    """
    Class to hold the details relevant to setting a game board.
    This is used for the computer and game board.
    Will hold the list of guesses made and ship positions.
    Function to print the board for each round based on the information
    held in the class.
    """
    def __init__(self, name, size, num_ships):
        self.name = name
        self.size = size
        self.num_ships = num_ships

    def build_board():
            # prepare the empty content
        rows = size
        cols = size
        content = [["."]*cols for _ in range(rows)]

        # assign values at coordinates as needed (based on your grid)
        grid = [(1,1,"@"),(2,3,"@"),(5,2,"@"),(4,6,"R"),(7,4,"L"),(6,6,"W"),(3,6,"L"),(2,6,"D"),(5,6,"O")]
        for (y,x,c) in grid: content[y][x] = c

        # build frame
        width       = len(str(max(rows,cols)-1))
        content_line = "# | values |"

        dashes      = "-".join("-"*width for _ in range(cols))
        frame_line   = content_line.replace("values",dashes)
        frame_line   = frame_line.replace("#"," "*width)
        frame_line   = frame_line.replace("| ","+-").replace(" |","-+")

        # print grid
        print(frame_line)
        for i,row in enumerate(reversed(content),1):
            values = " ".join(f"{v:{width}s}" for v in row)
            line   = content_line.replace("values",values)
            line   = line.replace("#",f"{rows-i:{width}d}")
            print(line)
        print(frame_line)

        # x-axis numbers
        num_line = content_line.replace("|"," ")
        num_line = num_line.replace("#"," "*width)
        col_nums = " ".join(f"{i:<{width}d}" for i in range(cols))
        num_line = num_line.replace("values",col_nums)
        print(num_line)
   


def main():
    Board.build_board()

main()