from EntityClass import Entity
from Enums import EntType
from Misc import moveCursor


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid_to_print = []

    def is_point_wall(self, ent, entities) -> bool:
        for ett in entities:
            if ett.type == EntType.WALL:
                if ett.collides(ent) and ent.type != EntType.WALL:
                    return True
        return False

    def is_out_of_bounds(self, ent: Entity):
        for xy in ent.pos:
            if xy[0] < 0 or xy[1] < 0 or xy[0] > self.height - 1 or xy[1] > self.width - 1:
                return True

    def update_grid(self, player, entities):
        _grid = []
        for row in range(self.height + 1):
            row_char_list = []
            for col in range(self.width + 1):
                row_char_list.append(' ')
            row_char_list.append('\n')
            _grid.append(row_char_list)

        if self.is_point_wall(player, entities):
            player.illegal_move()

        for ent in entities:
            if self.is_out_of_bounds(ent):
                entities.remove(ent)
                continue
            for xy in ent.pos:
                try:
                    _grid[xy[0]][xy[1]] = ent.symbol
                except IndexError as e:
                    if ent.type == EntType.WALL:
                        entities.remove(ent)
                    print(e)

        for pxy in player.pos:
            _grid[pxy[0]][pxy[1]] = player.symbol

        self.grid_to_print = _grid

    def print_grid(self, player):
        # clearConsole(self.width)
        """ flush and move cursor to 0,0 so no screen tear """
        moveCursor()
        for row in self.grid_to_print:
            for col in row:
                print(col, sep='', end='')
        print(
            f'[ Exit:l Move:awsd   hp:{player.hp} ${player.coin} xy:{player.pos}]')