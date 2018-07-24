# Imports
from pygame import Color
import pygame


# Check if point is in polygon
def inside_poly(x, y, poly):
    num = len(poly)
    j = num - 1
    c = False
    for i in range(num):
        if ((poly[i][1] > y) != (poly[j][1] > y)) and \
                (x < poly[i][0] + (poly[j][0] - poly[i][0]) * (y - poly[i][1]) /
                                  (poly[j][1] - poly[i][1])):
            c = not c
        j = i
    return c


# Shogi program
def shogi_run():

    # Screen
    size = screen_width, screen_height = 1620, 900
    screen = pygame.display.set_mode(size)

    # Margins
    board_margin_top = 43
    board_margin_bottom = 43
    board_margin_right = 403
    board_margin_left = 403
    stand_margin = 43

    # Dimensions
    line_width = 4
    stand_size = 272
    board_size = screen_width - board_margin_right - board_margin_left
    square_size = int((board_size - 10 * line_width) / 9)

    # Other info
    font_height = 16

    # Load board
    board_image = pygame.image.load("Others//board.png").convert()

    # Surfaces
    board_surface = pygame.Surface((screen_width, screen_height))
    piece_surface = pygame.Surface((board_size, board_size), pygame.SRCALPHA, 32).convert_alpha()
    stand_surface_gote = pygame.Surface((stand_size, stand_size), pygame.SRCALPHA, 32).convert_alpha()
    stand_surface_sente = pygame.Surface((stand_size, stand_size), pygame.SRCALPHA, 32).convert_alpha()
    highlight_surface = pygame.Surface((board_size, board_size), pygame.SRCALPHA, 32).convert_alpha()

    # Background
    board_surface.blit(board_image, (0, 0))

    # Highlight
    highlight = dict()

    highlight['A'] = pygame.Surface((square_size, square_size), pygame.SRCALPHA)  # Attack
    highlight['S'] = pygame.Surface((square_size, square_size), pygame.SRCALPHA)  # Select
    highlight['M'] = pygame.image.load("Others//move.png").convert_alpha()  # Move

    highlight['A'].fill((255, 0, 0, 120))
    highlight['S'].fill((0, 255, 0, 120))

    # Pieces
    piece = dict()

    piece['SP0'] = pygame.image.load("Pieces//SP0.png")
    piece['SL0'] = pygame.image.load("Pieces//SL0.png")
    piece['SN0'] = pygame.image.load("Pieces//SN0.png")
    piece['SS0'] = pygame.image.load("Pieces//SS0.png")
    piece['SG0'] = pygame.image.load("Pieces//SG0.png")
    piece['SB0'] = pygame.image.load("Pieces//SB0.png")
    piece['SR0'] = pygame.image.load("Pieces//SR0.png")
    piece['SK0'] = pygame.image.load("Pieces//SK0.png")
    piece['SP1'] = pygame.image.load("Pieces//SP1.png")
    piece['SL1'] = pygame.image.load("Pieces//SL1.png")
    piece['SN1'] = pygame.image.load("Pieces//SN1.png")
    piece['SS1'] = pygame.image.load("Pieces//SS1.png")
    piece['SB1'] = pygame.image.load("Pieces//SB1.png")
    piece['SR1'] = pygame.image.load("Pieces//SR1.png")
    piece['GP0'] = pygame.image.load("Pieces//GP0.png")
    piece['GL0'] = pygame.image.load("Pieces//GL0.png")
    piece['GN0'] = pygame.image.load("Pieces//GN0.png")
    piece['GS0'] = pygame.image.load("Pieces//GS0.png")
    piece['GG0'] = pygame.image.load("Pieces//GG0.png")
    piece['GB0'] = pygame.image.load("Pieces//GB0.png")
    piece['GR0'] = pygame.image.load("Pieces//GR0.png")
    piece['GK0'] = pygame.image.load("Pieces//GK0.png")
    piece['GP1'] = pygame.image.load("Pieces//GP1.png")
    piece['GL1'] = pygame.image.load("Pieces//GL1.png")
    piece['GN1'] = pygame.image.load("Pieces//GN1.png")
    piece['GS1'] = pygame.image.load("Pieces//GS1.png")
    piece['GB1'] = pygame.image.load("Pieces//GB1.png")
    piece['GR1'] = pygame.image.load("Pieces//GR1.png")

    # Stand pieces
    stand_piece = dict()
    stand_image = dict()

    stand_piece['P'] = pygame.image.load("Pieces_tilted//SP0_tilt.png")
    stand_piece['L'] = pygame.image.load("Pieces_tilted//SL0_tilt.png")
    stand_piece['N'] = pygame.image.load("Pieces_tilted//SN0_tilt.png")
    stand_piece['S'] = pygame.image.load("Pieces_tilted//SS0_tilt.png")
    stand_piece['G'] = pygame.image.load("Pieces_tilted//SG0_tilt.png")
    stand_piece['B'] = pygame.image.load("Pieces_tilted//SB0_tilt.png")
    stand_piece['R'] = pygame.image.load("Pieces_tilted//SR0_tilt.png")

    stand_image['P'] = pygame.image.load("Pieces_tilted//SP0_tilt.png")
    stand_image['L'] = pygame.image.load("Pieces_tilted//SL0_tilt.png")
    stand_image['N'] = pygame.image.load("Pieces_tilted//SN0_tilt.png")
    stand_image['S'] = pygame.image.load("Pieces_tilted//SS0_tilt.png")
    stand_image['G'] = pygame.image.load("Pieces_tilted//SG0_tilt.png")
    stand_image['B'] = pygame.image.load("Pieces_tilted//SB0_tilt.png")
    stand_image['R'] = pygame.image.load("Pieces_tilted//SR0_tilt.png")

    # Corner info of tilted pieces
    corner_pos = dict()

    corner_pos['B1'] = (23, 6)
    corner_pos['B2'] = (40, 3)
    corner_pos['B3'] = (62, 11)
    corner_pos['B4'] = (62, 78)
    corner_pos['B5'] = (3, 69)

    corner_pos['R1'] = (4, 14)
    corner_pos['R2'] = (24, 5)
    corner_pos['R3'] = (44, 7)
    corner_pos['R4'] = (65, 72)
    corner_pos['R5'] = (5, 81)

    corner_pos['P1'] = (47, 3)
    corner_pos['P2'] = (71, 11)
    corner_pos['P3'] = (80, 26)
    corner_pos['P4'] = (50, 84)
    corner_pos['P5'] = (2, 48)

    corner_pos['L1'] = (33, 3)
    corner_pos['L2'] = (57, 5)
    corner_pos['L3'] = (70, 16)
    corner_pos['L4'] = (60, 80)
    corner_pos['L5'] = (4, 62)

    corner_pos['N1'] = (22, 13)
    corner_pos['N2'] = (42, 7)
    corner_pos['N3'] = (62, 13)
    corner_pos['N4'] = (72, 78)
    corner_pos['N5'] = (12, 78)

    corner_pos['S1'] = (3, 17)
    corner_pos['S2'] = (18, 6)
    corner_pos['S3'] = (41, 5)
    corner_pos['S4'] = (71, 65)
    corner_pos['S5'] = (13, 83)

    corner_pos['G1'] = (3, 29)
    corner_pos['G2'] = (15, 12)
    corner_pos['G3'] = (36, 6)
    corner_pos['G4'] = (81, 52)
    corner_pos['G5'] = (34, 86)

    # Stand piece positions
    stand_piece_pos = dict()
    stand_piece_pos['N'] = (stand_size / 2 - square_size / 2,
                            stand_size * 3/4 - square_size / 2)
    stand_piece_pos['L'] = (stand_piece_pos['N'][0] + corner_pos['N1'][0] - corner_pos['L3'][0],
                            stand_piece_pos['N'][1] + corner_pos['N1'][1] - corner_pos['L3'][1])
    stand_piece_pos['P'] = (stand_piece_pos['L'][0] + corner_pos['L1'][0] - corner_pos['P3'][0],
                            stand_piece_pos['L'][1] + corner_pos['L1'][1] - corner_pos['P3'][1])
    stand_piece_pos['S'] = (stand_piece_pos['N'][0] + corner_pos['N3'][0] - corner_pos['S1'][0],
                            stand_piece_pos['N'][1] + corner_pos['N3'][1] - corner_pos['S1'][1])
    stand_piece_pos['G'] = (stand_piece_pos['S'][0] + corner_pos['S3'][0] - corner_pos['G1'][0],
                            stand_piece_pos['S'][1] + corner_pos['S3'][1] - corner_pos['G1'][1])
    stand_piece_pos['R'] = (stand_size / 2 - corner_pos['R5'][0],
                            stand_size / 2 - corner_pos['R5'][1])
    stand_piece_pos['B'] = (stand_size / 2 - corner_pos['B4'][0],
                            stand_size / 2 - corner_pos['B4'][1])

    # States
    piece_state = [['GL0', '', 'GP0', '', '', '', 'SP0', '', 'SL0'],
                   ['GN0', 'GB0', 'GP0', '', '', '', 'SP0', 'SB0', 'SN0'],
                   ['GS0', '', 'GP0', '', '', '', 'SP0', '', 'SS0'],
                   ['GG0', '', 'GP0', '', '', '', 'SP0', '', 'SG0'],
                   ['GK0', '', 'GP0', '', '', '', 'SP0', '', 'SK0'],
                   ['GG0', '', 'GP0', '', '', '', 'SP0', '', 'SG0'],
                   ['GS0', '', 'GP0', '', '', '', 'SP0', '', 'SS0'],
                   ['GN0', 'GR0', 'GP0', '', '', '', 'SP0', 'SR0', 'SN0'],
                   ['GL0', '', 'GP0', '', '', '', 'SP0', '', 'SL0']]

    highlight_state = [[''] * 9,
                       [''] * 9,
                       [''] * 9,
                       [''] * 9,
                       [''] * 9,
                       [''] * 9,
                       [''] * 9,
                       [''] * 9,
                       [''] * 9]

    stand_value = dict()
    
    stand_value['SP'] = 0
    stand_value['SL'] = 0
    stand_value['SN'] = 0
    stand_value['SS'] = 0
    stand_value['SG'] = 0
    stand_value['SB'] = 0
    stand_value['SR'] = 0
    stand_value['GP'] = 0
    stand_value['GL'] = 0
    stand_value['GN'] = 0
    stand_value['GS'] = 0
    stand_value['GG'] = 0
    stand_value['GB'] = 0
    stand_value['GR'] = 0

    stand_active = dict()
    stand_active['SP'] = False
    stand_active['SL'] = False
    stand_active['SN'] = False
    stand_active['SS'] = False
    stand_active['SG'] = False
    stand_active['SB'] = False
    stand_active['SR'] = False
    stand_active['GP'] = False
    stand_active['GL'] = False
    stand_active['GN'] = False
    stand_active['GS'] = False
    stand_active['GG'] = False
    stand_active['GB'] = False
    stand_active['GR'] = False

    # Drawing the pieces
    def draw_pieces():

        # Refresh
        piece_surface.fill(Color(0, 0, 0, 0))

        # Draw piece onto piece_surface
        for column in range(len(piece_state)):
            for row in range(len(piece_state[column])):
                if piece_state[column][row] != '':
                    piece_surface.blit(piece[piece_state[column][row]],
                                       (line_width + column * (line_width + square_size),
                                        line_width + row * (line_width + square_size)))

    # Draw stand pieces
    def draw_stand():

        # Refresh
        stand_surface_sente.fill(Color(0, 0, 0, 0))
        stand_surface_gote.fill(Color(0, 0, 0, 0))

        for stand_piece_type in stand_value:
            if stand_value[stand_piece_type] != 0:
                if stand_piece_type[0] == 'S':
                    stand_surface_sente.blit(stand_image[stand_piece_type[1]],
                                             stand_piece_pos[stand_piece_type[1]])

                    display_quantity(stand_value[stand_piece_type],
                                     (stand_piece_pos[stand_piece_type[1]][0] + corner_pos[stand_piece_type[1]+'2'][0],
                                      stand_piece_pos[stand_piece_type[1]][1] + corner_pos[stand_piece_type[1]+'2'][1]
                                      - font_height), 'S')

                elif stand_piece_type[0] == 'G':
                    if stand_piece_type[0] == 'G':
                        stand_surface_gote.blit(stand_image[stand_piece_type[1]],
                                                stand_piece_pos[stand_piece_type[1]])

                        display_quantity(stand_value[stand_piece_type],
                                         (stand_piece_pos[stand_piece_type[1]][0] +
                                          corner_pos[stand_piece_type[1] + '2'][0],
                                          stand_piece_pos[stand_piece_type[1]][1] +
                                          corner_pos[stand_piece_type[1] + '2'][1]
                                          - font_height), 'G')

    # Display quantity
    def display_quantity(quantity, text_position, side):
        pygame.font.init()
        display_font = pygame.font.Font(None, 30)
        display_surf = display_font.render(str(quantity), 1, (0, 0, 0))

        if side == 'S':
            stand_surface_sente.blit(display_surf, text_position)

        elif side == 'G':
            stand_surface_gote.blit(display_surf, text_position)

    # Draw highlight
    def draw_highlight():
        highlight_surface.fill(Color(0, 0, 0, 0))

        for column in range(len(highlight_state)):
            for row in range(len(highlight_state[column])):
                if highlight_state[column][row] != '':
                    highlight_surface.blit(highlight[highlight_state[column][row]],
                                           (line_width + column * (line_width + square_size),
                                            line_width + row * (line_width + square_size)))

    # Draw the screen
    def draw_screen():

        # Update pieces and highlight
        draw_pieces()
        draw_stand()
        draw_highlight()

        # Blit to screen
        screen.blit(board_surface, (0, 0))
        screen.blit(stand_surface_sente, (screen_width - board_margin_top - stand_size,
                                          screen_height - board_margin_top - stand_size))
        flipped = stand_surface_gote
        flipped = pygame.transform.flip(flipped, True, True)
        screen.blit(flipped, (board_margin_top, board_margin_top))
        screen.blit(highlight_surface, (board_margin_left, board_margin_top))
        screen.blit(piece_surface, (board_margin_left, board_margin_top))

        pygame.display.flip()

    # Select square
    def square_select():
        x, y = position

        # Within the board
        if board_margin_left < x < screen_width - board_margin_right and \
                board_margin_top < y < screen_height - board_margin_bottom:

            x_index = int((x - board_margin_left - line_width) / (square_size + line_width))
            y_index = int((y - board_margin_top - line_width) / (square_size + line_width))

            if highlight_state[x_index][y_index] == '':
                clear_highlight()

                if piece_state[x_index][y_index] != '':
                    highlight_state[x_index][y_index] = 'S'

                # Move type
                piece_rules(x_index, y_index)

            elif highlight_state[x_index][y_index] == 'M':
                move_piece(x_index, y_index)

            elif highlight_state[x_index][y_index] == 'A':
                piece_add(piece_state[x_index][y_index])
                move_piece(x_index, y_index)

            elif highlight_state[x_index][y_index] == 'S':
                clear_highlight()

        # Sente stand
        elif screen_width - board_margin_right + 2 * stand_margin < x < screen_width - stand_margin and \
                screen_height - stand_size - stand_margin < y < screen_height - stand_margin:

            for piece_type in stand_value:
                if piece_type[0] == 'S':
                    if check_inside(piece_type[1], stand_piece_pos[piece_type[1]], 'S'):
                        print(piece_type[1])
                        if not stand_active[piece_type]:
                            stand_active[piece_type] = True
                            place_piece(piece_type)

                        else:
                            clear_highlight()

        # Gote stand
        elif stand_margin < x < stand_margin + stand_size and \
                stand_margin < y < stand_margin + stand_size:

            for piece_type in stand_value:
                if piece_type[0] == 'G':
                    if check_inside(piece_type[1], stand_piece_pos[piece_type[1]], 'G'):
                        print(piece_type[1])
                        if not stand_active[piece_type]:
                            stand_active[piece_type] = True
                            place_piece(piece_type)

                        else:
                            clear_highlight()

    # If the piece is clicked
    def check_inside(piece_type, piece_pos, side):
        if side == 'S':
            return inside_poly(position[0] - board_margin_left - board_size - 2 * stand_margin,
                               position[1] + stand_size + stand_margin - screen_height,
                               [(piece_pos[0] + corner_pos[piece_type + '1'][0],
                                 piece_pos[1] + corner_pos[piece_type + '1'][1]),
                                (piece_pos[0] + corner_pos[piece_type + '2'][0],
                                 piece_pos[1] + corner_pos[piece_type + '2'][1]),
                                (piece_pos[0] + corner_pos[piece_type + '3'][0],
                                 piece_pos[1] + corner_pos[piece_type + '3'][1]),
                                (piece_pos[0] + corner_pos[piece_type + '4'][0],
                                 piece_pos[1] + corner_pos[piece_type + '4'][1]),
                                (piece_pos[0] + corner_pos[piece_type + '5'][0],
                                 piece_pos[1] + corner_pos[piece_type + '5'][1])])
        elif side == 'G':
            centre = (stand_margin + stand_size / 2, stand_margin + stand_size / 2)
            return inside_poly(2 * centre[0] - position[0] - stand_margin,
                               2 * centre[1] - position[1] - stand_margin,
                               [(piece_pos[0] + corner_pos[piece_type + '1'][0],
                                 piece_pos[1] + corner_pos[piece_type + '1'][1]),
                                (piece_pos[0] + corner_pos[piece_type + '2'][0],
                                 piece_pos[1] + corner_pos[piece_type + '2'][1]),
                                (piece_pos[0] + corner_pos[piece_type + '3'][0],
                                 piece_pos[1] + corner_pos[piece_type + '3'][1]),
                                (piece_pos[0] + corner_pos[piece_type + '4'][0],
                                 piece_pos[1] + corner_pos[piece_type + '4'][1]),
                                (piece_pos[0] + corner_pos[piece_type + '5'][0],
                                 piece_pos[1] + corner_pos[piece_type + '5'][1])])

    # Place stand piece
    def place_piece(piece_type):
        if piece_type[0] == 'S':
            if piece_type[1] == 'P':
                pawn_on_column = []
                for column in range(len(piece_state)):
                    for row in range(len(piece_state[column])):
                        if piece_state[column][row] == 'SP0':
                            pawn_on_column.append(column)

                for column in range(len(piece_state)):
                    if column not in pawn_on_column:
                        for row in range(len(piece_state[column])):
                            if piece_state[column][row] == '':
                                highlight_state[column][row] = 'M'

            elif piece_type[1] == 'N':
                for column in range(len(highlight_state)):
                    for row in range(2, len(highlight_state[column])):
                        if piece_state[column][row] == '':
                            highlight_state[column][row] = 'M'

            else:
                for column in range(len(highlight_state)):
                    for row in range(1, len(highlight_state[column])):
                        if piece_state[column][row] == '':
                            highlight_state[column][row] = 'M'

        elif piece_type[0] == 'G':
            if piece_type[1] == 'P':
                pawn_on_column = []
                for column in range(len(piece_state)):
                    for row in range(len(piece_state[column])):
                        if piece_state[column][row] == 'GP0':
                            pawn_on_column.append(column)

                for column in range(len(piece_state)):
                    if column not in pawn_on_column:
                        for row in range(len(piece_state[column])):
                            if piece_state[column][row] == '':
                                highlight_state[column][row] = 'M'

            elif piece_type[1] == 'N':
                for column in range(len(highlight_state)):
                    for row in range(len(highlight_state[column]) - 2):
                        if piece_state[column][row] == '':
                            highlight_state[column][row] = 'M'

            else:
                for column in range(len(highlight_state)):
                    for row in range(len(highlight_state[column]) - 1):
                        if piece_state[column][row] == '':
                            highlight_state[column][row] = 'M'

    # Move piece
    def move_piece(x_index, y_index):
        active = False
        for column in range(len(highlight_state)):
            for row in range(len(highlight_state[column])):
                if highlight_state[column][row] == 'S':
                    x_active = column
                    y_active = row
                    active = True

        if active:
            piece_state[x_index][y_index], piece_state[x_active][y_active] = piece_state[x_active][y_active], ''

        else:
            for piece_active in stand_active:
                if stand_active[piece_active]:
                    piece_state[x_index][y_index] = piece_active + '0'
                    stand_value[piece_active[:2]] -= 1

        clear_highlight()

    # Add piece
    def piece_add(piece_taken):
        if piece_taken[0] == 'G':
            stand_value['S' + piece_taken[1]] += 1

        elif piece_taken[0] == 'S':
            stand_value['G' + piece_taken[1]] += 1

    # Possible piece rules
    def piece_rules(x_index, y_index):

        # Sente Pawn
        if piece_state[x_index][y_index] == 'SP0':
            piece_move_highlight([[(x_index, y_index - 1)]], 'S')

        # Sente Rook
        elif piece_state[x_index][y_index] == 'SR0':
            rule_left = []
            rule_right = []
            rule_up = []
            rule_down = []

            x_move = x_index
            y_move = y_index

            while x_move > 0:
                x_move -= 1
                rule_left.append((x_move, y_move))

            x_move = x_index
            y_move = y_index

            while x_move < 8:
                x_move += 1
                rule_right.append((x_move, y_move))

            x_move = x_index
            y_move = y_index

            while y_move < 8:
                y_move += 1
                rule_down.append((x_move, y_move))

            x_move = x_index
            y_move = y_index

            while y_move > 0:
                y_move -= 1
                rule_up.append((x_move, y_move))

            piece_move_highlight([rule_left, rule_right, rule_down, rule_up], 'S')

        # Sente Bishop
        elif piece_state[x_index][y_index] == 'SB0':
            rule_left_up = []
            rule_right_up = []
            rule_left_down = []
            rule_right_down = []

            x_move = x_index
            y_move = y_index

            while x_move > 0 and y_move > 0:
                x_move -= 1
                y_move -= 1
                rule_left_up.append((x_move, y_move))

            x_move = x_index
            y_move = y_index

            while x_move < 8 and y_move > 0:
                x_move += 1
                y_move -= 1
                rule_right_up.append((x_move, y_move))

            x_move = x_index
            y_move = y_index

            while x_move > 0 and y_move < 8:
                x_move -= 1
                y_move += 1
                rule_left_down.append((x_move, y_move))

            x_move = x_index
            y_move = y_index

            while x_move < 8 and y_move < 8:
                x_move += 1
                y_move += 1
                rule_right_down.append((x_move, y_move))

            piece_move_highlight([rule_left_up,
                                  rule_right_up,
                                  rule_left_down,
                                  rule_right_down], 'S')

        # Sente Lance
        elif piece_state[x_index][y_index] == 'SL0':

            rule_up = []

            y_move = y_index

            while y_move > 0:
                y_move -= 1
                rule_up.append((x_index, y_move))

            piece_move_highlight([rule_up], 'S')

        # Sente Knight
        elif piece_state[x_index][y_index] == 'SN0':

            piece_move_highlight([[(x_index - 1, y_index - 2)],
                                  [(x_index + 1, y_index - 2)]], 'S')

        # Sente Silver
        elif piece_state[x_index][y_index] == 'SS0':

            piece_move_highlight([[(x_index - 1, y_index - 1)],
                                  [(x_index, y_index - 1)],
                                  [(x_index + 1, y_index - 1)],
                                  [(x_index - 1, y_index + 1)],
                                  [(x_index + 1, y_index + 1)]], 'S')

        # Sente Gold
        elif piece_state[x_index][y_index] == 'SG0':

            piece_move_highlight([[(x_index - 1, y_index - 1)],
                                  [(x_index, y_index - 1)],
                                  [(x_index + 1, y_index - 1)],
                                  [(x_index - 1, y_index)],
                                  [(x_index + 1, y_index)],
                                  [(x_index, y_index + 1)]], 'S')

        # Sente King
        elif piece_state[x_index][y_index] == 'SK0':

            piece_move_highlight([[(x_index - 1, y_index - 1)],
                                  [(x_index, y_index - 1)],
                                  [(x_index + 1, y_index - 1)],
                                  [(x_index + 1, y_index)],
                                  [(x_index, y_index + 1)],
                                  [(x_index + 1, y_index + 1)],
                                  [(x_index, y_index + 1)],
                                  [(x_index - 1, y_index + 1)],
                                  [(x_index - 1, y_index)]], 'S')

        # Gote Pawn
        if piece_state[x_index][y_index] == 'GP0':
            piece_move_highlight([[(x_index, y_index + 1)]], 'G')

        # Gote Rook
        elif piece_state[x_index][y_index] == 'GR0':
            rule_left = []
            rule_right = []
            rule_up = []
            rule_down = []

            x_move = x_index
            y_move = y_index

            while x_move > 0:
                x_move -= 1
                rule_left.append((x_move, y_move))

            x_move = x_index
            y_move = y_index

            while x_move < 8:
                x_move += 1
                rule_right.append((x_move, y_move))

            x_move = x_index
            y_move = y_index

            while y_move < 8:
                y_move += 1
                rule_down.append((x_move, y_move))

            x_move = x_index
            y_move = y_index

            while y_move > 0:
                y_move -= 1
                rule_up.append((x_move, y_move))

            piece_move_highlight([rule_left, rule_right, rule_down, rule_up], 'G')

        # Gote Bishop
        elif piece_state[x_index][y_index] == 'GB0':
            rule_left_up = []
            rule_right_up = []
            rule_left_down = []
            rule_right_down = []

            x_move = x_index
            y_move = y_index

            while x_move > 0 and y_move > 0:
                x_move -= 1
                y_move -= 1
                rule_left_up.append((x_move, y_move))

            x_move = x_index
            y_move = y_index

            while x_move < 8 and y_move > 0:
                x_move += 1
                y_move -= 1
                rule_right_up.append((x_move, y_move))

            x_move = x_index
            y_move = y_index

            while x_move > 0 and y_move < 8:
                x_move -= 1
                y_move += 1
                rule_left_down.append((x_move, y_move))

            x_move = x_index
            y_move = y_index

            while x_move < 8 and y_move < 8:
                x_move += 1
                y_move += 1
                rule_right_down.append((x_move, y_move))

            piece_move_highlight([rule_left_up,
                                  rule_right_up,
                                  rule_left_down,
                                  rule_right_down], 'G')

        # Gote Lance
        elif piece_state[x_index][y_index] == 'GL0':

            rule_down = []

            y_move = y_index

            while y_move < 9:
                y_move += 1
                rule_down.append((x_index, y_move))

            piece_move_highlight([rule_down], 'G')

        # Gote Knight
        elif piece_state[x_index][y_index] == 'GN0':

            piece_move_highlight([[(x_index - 1, y_index + 2)],
                                  [(x_index + 1, y_index + 2)]], 'G')

        # Gote Silver
        elif piece_state[x_index][y_index] == 'GS0':

            piece_move_highlight([[(x_index - 1, y_index + 1)],
                                  [(x_index, y_index + 1)],
                                  [(x_index + 1, y_index + 1)],
                                  [(x_index - 1, y_index - 1)],
                                  [(x_index + 1, y_index - 1)]], 'G')

        # Gote Gold
        elif piece_state[x_index][y_index] == 'GG0':

            piece_move_highlight([[(x_index - 1, y_index + 1)],
                                  [(x_index, y_index + 1)],
                                  [(x_index + 1, y_index + 1)],
                                  [(x_index - 1, y_index)],
                                  [(x_index + 1, y_index)],
                                  [(x_index, y_index - 1)]], 'G')

        # Gote King
        elif piece_state[x_index][y_index] == 'GK0':

            piece_move_highlight([[(x_index - 1, y_index - 1)],
                                  [(x_index, y_index - 1)],
                                  [(x_index + 1, y_index - 1)],
                                  [(x_index + 1, y_index)],
                                  [(x_index, y_index + 1)],
                                  [(x_index + 1, y_index + 1)],
                                  [(x_index, y_index + 1)],
                                  [(x_index - 1, y_index + 1)],
                                  [(x_index - 1, y_index)]], 'G')

    # Highlight possible moves
    def piece_move_highlight(possible_moves, turn):
        for path in possible_moves:
            for pos in path:
                if -1 < pos[1] < 9 and -1 < pos[0] < 9:
                    if piece_state[pos[0]][pos[1]] == '':
                        highlight_state[pos[0]][pos[1]] = 'M'

                    elif piece_state[pos[0]][pos[1]][0] != turn:
                        highlight_state[pos[0]][pos[1]] = 'A'
                        break

                    elif piece_state[pos[0]][pos[1]][0] == turn:
                        break

    # Clear highlight
    def clear_highlight():
        nonlocal highlight_state
        nonlocal stand_active

        highlight_state = [[''] * 9,
                           [''] * 9,
                           [''] * 9,
                           [''] * 9,
                           [''] * 9,
                           [''] * 9,
                           [''] * 9,
                           [''] * 9,
                           [''] * 9]

        for state in stand_active:
            stand_active[state] = False

    draw_screen()

    # Running program
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                square_select()

                draw_screen()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


# Run shogi
if __name__ == "__main__":
    shogi_run()
