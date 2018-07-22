# Imports
from pygame import Color
import pygame


def t_maths(a, b, type):
    if type == 'add':
        return a[0] + b[0], a[1] + b[1]

    elif type == 'subtract':
        return a[0] - b[0], a[1] - b[1]

    elif type == 'scalar':
        return b[0] * a, b[1] * a


# Tuple addition
def add_tuple(a, b):
    return a[0] + b[0], a[1] + b[1]

def subtract_tuple(a, b):
    return a[0] - b[0], a[1] - b[1]

def multiply_tuple(a, b):
    return b[0] * a, b[1] * a


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

    stand_piece['P'] = pygame.image.load("Pieces_tilted//SP0_tilt.png")
    stand_piece['L'] = pygame.image.load("Pieces_tilted//SL0_tilt.png")
    stand_piece['N'] = pygame.image.load("Pieces_tilted//SN0_tilt.png")
    stand_piece['S'] = pygame.image.load("Pieces_tilted//SS0_tilt.png")
    stand_piece['G'] = pygame.image.load("Pieces_tilted//SG0_tilt.png")
    stand_piece['B'] = pygame.image.load("Pieces_tilted//SB0_tilt.png")
    stand_piece['R'] = pygame.image.load("Pieces_tilted//SR0_tilt.png")

    sp = pygame.image.load("Pieces_tilted//SP0_tilt.png")
    sl = pygame.image.load("Pieces_tilted//SL0_tilt.png")
    sn = pygame.image.load("Pieces_tilted//SN0_tilt.png")
    ss = pygame.image.load("Pieces_tilted//SS0_tilt.png")
    sg = pygame.image.load("Pieces_tilted//SG0_tilt.png")
    sb = pygame.image.load("Pieces_tilted//SB0_tilt.png")
    sr = pygame.image.load("Pieces_tilted//SR0_tilt.png")

    # Corner info of tilted pieces
    corner_pos = dict()

    corner_pos['Bishop 1'] = (23, 6)
    corner_pos['Bishop 2'] = (40, 3)
    corner_pos['Bishop 3'] = (62, 11)
    corner_pos['Bishop 4'] = (62, 78)
    corner_pos['Bishop 5'] = (3, 69)

    corner_pos['Rook 1'] = (4, 14)
    corner_pos['Rook 2'] = (24, 5)
    corner_pos['Rook 3'] = (44, 7)
    corner_pos['Rook 4'] = (65, 72)
    corner_pos['Rook 5'] = (5, 81)

    corner_pos['Pawn 1'] = (47, 3)
    corner_pos['Pawn 2'] = (71, 11)
    corner_pos['Pawn 3'] = (80, 26)
    corner_pos['Pawn 4'] = (50, 84)
    corner_pos['Pawn 5'] = (2, 48)

    corner_pos['Lance 1'] = (33, 3)
    corner_pos['Lance 2'] = (57, 5)
    corner_pos['Lance 3'] = (70, 16)
    corner_pos['Lance 4'] = (60, 80)
    corner_pos['Lance 5'] = (4, 62)

    corner_pos['Knight 1'] = (22, 13)
    corner_pos['Knight 2'] = (42, 7)
    corner_pos['Knight 3'] = (62, 13)
    corner_pos['Knight 4'] = (72, 78)
    corner_pos['Knight 5'] = (12, 78)

    corner_pos['Silver 1'] = (3, 17)
    corner_pos['Silver 2'] = (18, 6)
    corner_pos['Silver 3'] = (41, 5)
    corner_pos['Silver 4'] = (71, 65)
    corner_pos['Silver 5'] = (13, 83)

    corner_pos['Gold 1'] = (3, 29)
    corner_pos['Gold 2'] = (15, 12)
    corner_pos['Gold 3'] = (36, 6)
    corner_pos['Gold 4'] = (81, 52)
    corner_pos['Gold 5'] = (34, 86)

    # Stand piece positions
    bishop_pos = (stand_size / 2 - corner_pos['Bishop 4'][0],
                  stand_size / 2 - corner_pos['Bishop 4'][1])

    rook_pos = (stand_size / 2 - corner_pos['Rook 5'][0],
                stand_size / 2 - corner_pos['Rook 5'][1])

    knight_pos = (stand_size / 2 - square_size / 2,
                  stand_size * 3/4 - square_size / 2)

    silver_pos = (knight_pos[0] + corner_pos['Knight 3'][0] - corner_pos['Silver 1'][0],
                  knight_pos[1] + corner_pos['Knight 3'][1] - corner_pos['Silver 1'][1])

    gold_pos = (silver_pos[0] + corner_pos['Silver 3'][0] - corner_pos['Gold 1'][0],
                silver_pos[1] + corner_pos['Silver 3'][1] - corner_pos['Gold 1'][1])

    lance_pos = (knight_pos[0] + corner_pos['Knight 1'][0] - corner_pos['Lance 3'][0],
                 knight_pos[1] + corner_pos['Knight 1'][1] - corner_pos['Lance 3'][1])

    pawn_pos = (lance_pos[0] + corner_pos['Lance 1'][0] - corner_pos['Pawn 3'][0],
                lance_pos[1] + corner_pos['Lance 1'][1] - corner_pos['Pawn 3'][1])

    # States
    piece_state = [['GL0', 'GN0', 'GS0', 'GG0', 'GK0', 'GG0', 'GS0', 'GN0', 'GL0'],
                   ['', 'GR0', '', '', '', '', '', 'GB0', ''],
                   ['GP0'] * 9,
                   [''] * 9,
                   ['', '', '', '', '', '', '', '', ''],
                   [''] * 9,
                   ['SP0'] * 9,
                   ['', 'SB0', '', '', '', '', '', 'SR0', ''],
                   ['SL0', 'SN0', 'SS0', 'SG0', 'SK0', 'SG0', 'SS0', 'SN0', 'SL0']]

    highlight_state = [[''] * 9,
                       [''] * 9,
                       [''] * 9,
                       [''] * 9,
                       [''] * 9,
                       [''] * 9,
                       [''] * 9,
                       [''] * 9,
                       [''] * 9]

    stand_state = [[0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0]]

    stand_active_state = [[False, False, False, False, False, False, False, False, False],
                          [False, False, False, False, False, False, False, False, False]]

    # Drawing the pieces
    def draw_pieces():
        piece_surface.fill(Color(0, 0, 0, 0))

        for row in range(len(piece_state)):
            for column in range(len(piece_state[row])):
                if piece_state[row][column] != '':
                    piece_surface.blit(piece[piece_state[row][column]],
                                       (line_width + column * (line_width + square_size),
                                        line_width + row * (line_width + square_size)))

    # Draw stand pieces
    def draw_stand():

        stand_surface_sente.fill(Color(0, 0, 0, 0))
        stand_surface_gote.fill(Color(0, 0, 0, 0))

        for sente_piece_index in range(len(stand_state[0])):
            if stand_state[0][sente_piece_index] != 0:
                if sente_piece_index == 6:
                    stand_surface_sente.blit(sr, rook_pos)

                    display_quantity(stand_state[0][sente_piece_index],
                                     add_tuple(add_tuple(corner_pos['Rook 2'], rook_pos), (0, - font_height)), 'S')

                elif sente_piece_index == 5:
                    stand_surface_sente.blit(sb, bishop_pos)

                    display_quantity(stand_state[0][sente_piece_index],
                                     add_tuple(add_tuple(corner_pos['Bishop 2'], bishop_pos), (0, - font_height)), 'S')


                elif sente_piece_index == 4:
                    stand_surface_sente.blit(sg, gold_pos)

                    display_quantity(stand_state[0][sente_piece_index],
                                     add_tuple(add_tuple(corner_pos['Gold 2'], gold_pos), (0, - font_height)), 'S')

                elif sente_piece_index == 3:
                    stand_surface_sente.blit(ss, silver_pos)

                    display_quantity(stand_state[0][sente_piece_index],
                                     add_tuple(add_tuple(corner_pos['Silver 2'], silver_pos), (0, - font_height)), 'S')

                elif sente_piece_index == 2:
                    stand_surface_sente.blit(sn, knight_pos)

                    display_quantity(stand_state[0][sente_piece_index],
                                     add_tuple(add_tuple(corner_pos['Knight 2'], knight_pos), (0, - font_height)), 'S')

                elif sente_piece_index == 1:
                    stand_surface_sente.blit(sl, lance_pos)

                    display_quantity(stand_state[0][sente_piece_index],
                                     add_tuple(add_tuple(corner_pos['Lance 2'], lance_pos), (0, - font_height)), 'S')

                elif sente_piece_index == 0:
                    stand_surface_sente.blit(sp, pawn_pos)

                    display_quantity(stand_state[0][sente_piece_index],
                                     add_tuple(add_tuple(corner_pos['Pawn 2'], pawn_pos), (0, - font_height)), 'S')

        for gote_piece_index in range(len(stand_state[1])):
            if stand_state[1][gote_piece_index] != 0:
                if gote_piece_index == 6:
                    stand_surface_gote.blit(sr, rook_pos)

                    display_quantity(stand_state[1][gote_piece_index],
                                     add_tuple(add_tuple(corner_pos['Rook 2'], rook_pos), (0, - font_height)), 'G')

                elif gote_piece_index == 5:
                    stand_surface_gote.blit(sb, bishop_pos)

                    display_quantity(stand_state[1][gote_piece_index],
                                     add_tuple(add_tuple(corner_pos['Bishop 2'], bishop_pos), (0, - font_height)), 'G')

                elif gote_piece_index == 4:
                    stand_surface_gote.blit(sg, gold_pos)

                    display_quantity(stand_state[1][gote_piece_index],
                                     add_tuple(add_tuple(corner_pos['Gold 2'], gold_pos), (0, - font_height)), 'G')

                elif gote_piece_index == 3:
                    stand_surface_gote.blit(ss, silver_pos)

                    display_quantity(stand_state[1][gote_piece_index],
                                     add_tuple(add_tuple(corner_pos['Silver 2'], silver_pos), (0, - font_height)), 'G')

                elif gote_piece_index == 2:
                    stand_surface_gote.blit(sn, knight_pos)

                    display_quantity(stand_state[1][gote_piece_index],
                                     add_tuple(add_tuple(corner_pos['Knight 2'], knight_pos), (0, - font_height)), 'G')

                elif gote_piece_index == 1:
                    stand_surface_gote.blit(sl, lance_pos)

                    display_quantity(stand_state[1][gote_piece_index],
                                     add_tuple(add_tuple(corner_pos['Lance 2'], lance_pos), (0, - font_height)), 'G')

                elif gote_piece_index == 0:
                    stand_surface_gote.blit(sp, pawn_pos)

                    display_quantity(stand_state[1][gote_piece_index],
                                     add_tuple(add_tuple(corner_pos['Pawn 2'], pawn_pos), (0, - font_height)), 'G')

    # Display number of pieces
    def display_quantity(quantity, position, side):
        pygame.font.init()
        display_font = pygame.font.Font(None, 30)
        display_surf = display_font.render(str(quantity), 1, (0, 0, 0))

        if side == 'S':
            stand_surface_sente.blit(display_surf, position)

        elif side == 'G':
            stand_surface_gote.blit(display_surf, position)

    # Drawing the highlight
    def draw_highlight():
        highlight_surface.fill(Color(0, 0, 0, 0))

        for row in range(len(highlight_state)):
            for column in range(len(highlight_state[row])):
                if highlight_state[row][column] != '':
                    highlight_surface.blit(highlight[highlight_state[row][column]],
                                           (line_width + column * (line_width + square_size),
                                            line_width + row * (line_width + square_size)))

    # Drawing the board
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

    # Highlight piece
    def square_select(position):
        x, y = position

        if board_margin_left < x < screen_width - board_margin_right and \
                board_margin_top < y < screen_height - board_margin_bottom:

            x_index = int((x - board_margin_left - line_width) / (square_size + line_width))
            y_index = int((y - board_margin_top - line_width) / (square_size + line_width))

            if highlight_state[y_index][x_index] == '':
                piece_select(x_index, y_index)

            elif highlight_state[y_index][x_index] == 'M':
                move_piece(x_index, y_index)

            elif highlight_state[y_index][x_index] == 'A':
                move_piece(x_index, y_index)

            elif highlight_state[y_index][x_index] == 'S':
                clear_highlight()

        elif screen_width - board_margin_right + 2 * stand_margin < x < screen_width - stand_margin and \
                screen_height - stand_size - stand_margin < y < screen_height - stand_margin:

            clear_highlight()

            if check_inside('Pawn', pawn_pos, 'S'):
                if stand_state[0][0] > 0:
                    print('Pawn')
                    if not stand_active_state[0][0]:
                        stand_active_state[0][0] = True
                        place_piece('Pawn', 'S')

                    else:
                        clear_highlight()

            elif check_inside('Lance', lance_pos, 'S'):
                if stand_state[0][1] > 0:
                    print('Lance')
                    if not stand_active_state[0][1]:
                        stand_active_state[0][1] = True
                        place_piece('Lance', 'S')

                    else:
                        clear_highlight()

            elif check_inside('Knight', knight_pos, 'S'):
                if stand_state[0][2] > 0:
                    print('Knight')
                    if not stand_active_state[0][2]:
                        stand_active_state[0][2] = True
                        place_piece('Knight', 'S')

                    else:
                        clear_highlight()

            elif check_inside('Silver', silver_pos, 'S'):
                if stand_state[0][3] > 0:
                    print('Silver')
                    if not stand_active_state[0][3]:
                        stand_active_state[0][3] = True
                        place_piece('Silver', 'S')

                    else:
                        clear_highlight()

            elif check_inside('Gold', gold_pos, 'S'):
                if stand_state[0][4] > 0:
                    print('Gold')
                    if not stand_active_state[0][4]:
                        stand_active_state[0][4] = True
                        place_piece('Gold', 'S')

                    else:
                        clear_highlight()

            elif check_inside('Bishop', bishop_pos, 'S'):
                if stand_state[0][5] > 0:
                    print('Bishop')
                    if not stand_active_state[0][5]:
                        stand_active_state[0][5] = True
                        place_piece('Gold', 'S')

                    else:
                        clear_highlight()

            elif check_inside('Rook', rook_pos, 'S'):
                if stand_state[0][6] > 0:
                    print('Rook')
                    if not stand_active_state[0][6]:
                        stand_active_state[0][6] = True
                        place_piece('Rook', 'S')

                    else:
                        clear_highlight()
        elif stand_margin < x < stand_margin + stand_size and \
                stand_margin < y < stand_margin + stand_size:

            clear_highlight()

            if check_inside('Pawn', pawn_pos, 'G'):
                if stand_state[1][0] > 0:
                    print('Pawn')
                    if not stand_active_state[1][0]:
                        stand_active_state[1][0] = True
                        place_piece('Pawn', 'G')

                    else:
                        clear_highlight()

            elif check_inside('Lance', lance_pos, 'G'):
                if stand_state[1][1] > 0:
                    print('Lance')
                    if not stand_active_state[1][1]:
                        stand_active_state[1][1] = True
                        place_piece('Lance', 'G')

                    else:
                        clear_highlight()

            elif check_inside('Knight', knight_pos, 'G'):
                if stand_state[1][2] > 0:
                    print('Knight')
                    if not stand_active_state[1][2]:
                        stand_active_state[1][2] = True
                        place_piece('Knight', 'G')

                    else:
                        clear_highlight()

            elif check_inside('Silver', silver_pos, 'G'):
                if stand_state[1][3] > 0:
                    print('Silver')
                    if not stand_active_state[1][3]:
                        stand_active_state[1][3] = True
                        place_piece('Silver', 'G')

                    else:
                        clear_highlight()

            elif check_inside('Gold', gold_pos, 'G'):
                if stand_state[1][4] > 0:
                    print('Gold')
                    if not stand_active_state[1][4]:
                        stand_active_state[1][4] = True
                        place_piece('Gold', 'G')

                    else:
                        clear_highlight()

            elif check_inside('Bishop', bishop_pos, 'G'):
                if stand_state[1][5] > 0:
                    print('Bishop')
                    if not stand_active_state[1][5]:
                        stand_active_state[1][5] = True
                        place_piece('Gold', 'G')

                    else:
                        clear_highlight()

            elif check_inside('Rook', rook_pos, 'G'):
                if stand_state[1][6] > 0:
                    print('Rook')
                    if not stand_active_state[1][6]:
                        stand_active_state[1][6] = True
                        place_piece('Rook', 'G')

                    else:
                        clear_highlight()

    def place_piece(piece_type, turn):
        if turn == 'S':
            if piece_type == 'Pawn':
                pawn_on_column = []
                pawn_free = []
                for row in range(len(highlight_state)):
                    for pawn_row in range(len(highlight_state)):
                        if piece_state[row][pawn_row] == 'SP0':
                            pawn_on_column.append(pawn_row)

                for column in range(9):
                    if column not in pawn_on_column:
                        pawn_free.append(column)

                for column in pawn_free:
                    for row in range(1, len(highlight_state[row])):
                        if piece_state[row][column] == '':
                            highlight_state[row][column] = 'M'

            elif piece_type == 'Knight':
                for row in range(2, len(highlight_state)):
                    for column in range(len(highlight_state[row])):
                        if piece_state[row][column] == '':
                            highlight_state[row][column] = 'M'

            else:
                for row in range(1, len(highlight_state)):
                    for column in range(len(highlight_state[row])):
                        if piece_state[row][column] == '':
                            highlight_state[row][column] = 'M'

        elif turn == 'G':

            if piece_type == 'Pawn':

                pawn_on_column = []
                pawn_free = []

                for row in range(len(highlight_state)):

                    for pawn_row in range(len(highlight_state)):

                        if piece_state[row][pawn_row] == 'GP0':
                            pawn_on_column.append(pawn_row)

                for column in range(9):

                    if column not in pawn_on_column:
                        pawn_free.append(column)

                for column in pawn_free:

                    for row in range(len(highlight_state[row]) - 1):

                        if piece_state[row][column] == '':
                            highlight_state[row][column] = 'M'

            elif piece_type == 'Knight':

                for row in range(len(highlight_state) - 2):

                    for column in range(len(highlight_state[row])):

                        if piece_state[row][column] == '':
                            highlight_state[row][column] = 'M'
            else:

                for row in range(len(highlight_state) - 1):

                    for column in range(len(highlight_state[row])):

                        if piece_state[row][column] == '':
                            highlight_state[row][column] = 'M'

    def check_inside(piece_type, piece_pos, side):
        if side == 'S':
            return inside_poly(position[0] - board_margin_left - board_size - 2 * stand_margin,
                           position[1] + stand_size + stand_margin - screen_height,
                           [add_tuple(piece_pos, corner_pos[piece_type + ' 1']),
                            add_tuple(piece_pos, corner_pos[piece_type + ' 2']),
                            add_tuple(piece_pos, corner_pos[piece_type + ' 3']),
                            add_tuple(piece_pos, corner_pos[piece_type + ' 4']),
                            add_tuple(piece_pos, corner_pos[piece_type + ' 5'])])
        elif side == 'G':
            centre = (stand_margin + stand_size / 2, stand_margin + stand_size / 2)
            return inside_poly(2 * centre[0] - position[0] - stand_margin,
                               2 * centre[1] - position[1] - stand_margin,
                               [add_tuple(piece_pos, corner_pos[piece_type + ' 1']),
                                add_tuple(piece_pos, corner_pos[piece_type + ' 2']),
                                add_tuple(piece_pos, corner_pos[piece_type + ' 3']),
                                add_tuple(piece_pos, corner_pos[piece_type + ' 4']),
                                add_tuple(piece_pos, corner_pos[piece_type + ' 5'])])

    def move_piece(x_index, y_index):
        active = False
        for row in range(len(highlight_state)):
            for column in range(len(highlight_state[row])):
                if highlight_state[row][column] == 'S':
                    x_active = column
                    y_active = row
                    active = True
                    break

        if active:
            if highlight_state[y_index][x_index] == 'A':
                piece_add(piece_state[y_index][x_index])

            piece_state[y_index][x_index], piece_state[y_active][x_active] = \
                piece_state[y_active][x_active], ''

            x_active = False
            y_active = False

        else:

            for piece_type in range(len(stand_state[0])):
                if stand_active_state[0][piece_type]:
                    if piece_type == 0:
                        piece_state[y_index][x_index] = 'SP0'
                        piece_remove('SP0')

                    elif piece_type == 1:
                        piece_state[y_index][x_index] = 'SL0'
                        piece_remove('SL0')

                    elif piece_type == 2:
                        piece_state[y_index][x_index] = 'SN0'
                        piece_remove('SN0')

                    elif piece_type == 3:
                        piece_state[y_index][x_index] = 'SS0'
                        piece_remove('SS0')

                    elif piece_type == 4:
                        piece_state[y_index][x_index] = 'SG0'
                        piece_remove('SG0')

                    elif piece_type == 5:
                        piece_state[y_index][x_index] = 'SB0'
                        piece_remove('SB0')

                    elif piece_type == 6:
                        piece_state[y_index][x_index] = 'SR0'
                        piece_remove('SR0')

            for piece_type in range(len(stand_state[1])):
                if stand_active_state[1][piece_type]:
                    if piece_type == 0:
                        piece_state[y_index][x_index] = 'GP0'
                        piece_remove('GP0')

                    elif piece_type == 1:
                        piece_state[y_index][x_index] = 'GL0'
                        piece_remove('GL0')

                    elif piece_type == 2:
                        piece_state[y_index][x_index] = 'GN0'
                        piece_remove('GN0')

                    elif piece_type == 3:
                        piece_state[y_index][x_index] = 'GS0'
                        piece_remove('GS0')

                    elif piece_type == 4:
                        piece_state[y_index][x_index] = 'GG0'
                        piece_remove('GG0')

                    elif piece_type == 5:
                        piece_state[y_index][x_index] = 'GB0'
                        piece_remove('GB0')

                    elif piece_type == 6:
                        piece_state[y_index][x_index] = 'SR0'
                        piece_remove('SR0')





        clear_highlight()

    def piece_add(piece):
        if piece[0] == 'G':
            side = 0

        elif piece[0] == 'S':
            side = 1

        if piece[1] == 'P':
            piece_type = 0

        elif piece[1] == 'L':
            piece_type = 1

        elif piece[1] == 'N':
            piece_type = 2

        elif piece[1] == 'S':
            piece_type = 3

        elif piece[1] == 'G':
            piece_type = 4

        elif piece[1] == 'B':
            piece_type = 5

        elif piece[1] == 'R':
            piece_type = 6

        stand_state[side][piece_type] += 1

    def piece_remove(piece):
        if piece[0] == 'G':
            side = 1

        elif piece[0] == 'S':
            side = 0

        if piece[1] == 'P':
            piece_type = 0

        elif piece[1] == 'L':
            piece_type = 1

        elif piece[1] == 'N':
            piece_type = 2

        elif piece[1] == 'S':
            piece_type = 3

        elif piece[1] == 'G':
            piece_type = 4

        elif piece[1] == 'B':
            piece_type = 5

        elif piece[1] == 'R':
            piece_type = 6

        stand_state[side][piece_type] -= 1

    # Piece select
    def piece_select(x_index, y_index):

        # Highlight square
        piece_select_highlight(x_index, y_index)

        # Move type
        piece_rules(x_index, y_index)

        # Piece select highlight

    def piece_select_highlight(x_index, y_index):
        clear_highlight()

        if piece_state[y_index][x_index] != '':
            highlight_state[y_index][x_index] = 'S'

    # Possible piece moves
    def piece_rules(x_index, y_index):

        # Sente Pawn
        if piece_state[y_index][x_index] == 'SP0':
            piece_move_highlight([[(x_index, y_index - 1)]], 'S')

        # Sente Rook
        elif piece_state[y_index][x_index] == 'SR0':
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
        elif piece_state[y_index][x_index] == 'SB0':
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
        elif piece_state[y_index][x_index] == 'SL0':

            rule_up = []

            y_move = y_index

            while y_move > 0:
                y_move -= 1
                rule_up.append((x_index, y_move))

            piece_move_highlight([rule_up], 'S')

        # Sente Knight
        elif piece_state[y_index][x_index] == 'SN0':

            piece_move_highlight([[(x_index - 1, y_index - 2)],
                                  [(x_index + 1, y_index - 2)]], 'S')

        # Sente Silver
        elif piece_state[y_index][x_index] == 'SS0':

            piece_move_highlight([[(x_index - 1, y_index - 1)],
                                  [(x_index, y_index - 1)],
                                  [(x_index + 1, y_index - 1)],
                                  [(x_index - 1, y_index + 1)],
                                  [(x_index + 1, y_index + 1)]], 'S')

        # Sente Gold
        elif piece_state[y_index][x_index] == 'SG0':

            piece_move_highlight([[(x_index - 1, y_index - 1)],
                                  [(x_index, y_index - 1)],
                                  [(x_index + 1, y_index - 1)],
                                  [(x_index - 1, y_index)],
                                  [(x_index + 1, y_index)],
                                  [(x_index, y_index + 1)]], 'S')

        # Sente King
        elif piece_state[y_index][x_index] == 'SK0':

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
        if piece_state[y_index][x_index] == 'GP0':
            piece_move_highlight([[(x_index, y_index + 1)]], 'G')

        # Sente Rook
        elif piece_state[y_index][x_index] == 'GR0':
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

        # Sente Bishop
        elif piece_state[y_index][x_index] == 'GB0':
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

        # Sente Lance
        elif piece_state[y_index][x_index] == 'GL0':

            rule_down = []

            y_move = y_index

            while y_move < 9:
                y_move += 1
                rule_down.append((x_index, y_move))

            piece_move_highlight([rule_down], 'G')

        # Sente Knight
        elif piece_state[y_index][x_index] == 'GN0':

            piece_move_highlight([[(x_index - 1, y_index + 2)],
                                  [(x_index + 1, y_index + 2)]], 'G')

        # Sente Silver
        elif piece_state[y_index][x_index] == 'GS0':

            piece_move_highlight([[(x_index - 1, y_index + 1)],
                                  [(x_index, y_index + 1)],
                                  [(x_index + 1, y_index + 1)],
                                  [(x_index - 1, y_index - 1)],
                                  [(x_index + 1, y_index - 1)]], 'G')

        # Sente Gold
        elif piece_state[y_index][x_index] == 'GG0':

            piece_move_highlight([[(x_index - 1, y_index + 1)],
                                  [(x_index, y_index + 1)],
                                  [(x_index + 1, y_index + 1)],
                                  [(x_index - 1, y_index)],
                                  [(x_index + 1, y_index)],
                                  [(x_index, y_index - 1)]], 'G')

        # Sente King
        elif piece_state[y_index][x_index] == 'GK0':

            piece_move_highlight([[(x_index - 1, y_index - 1)],
                                  [(x_index, y_index - 1)],
                                  [(x_index + 1, y_index - 1)],
                                  [(x_index + 1, y_index)],
                                  [(x_index, y_index + 1)],
                                  [(x_index + 1, y_index + 1)],
                                  [(x_index, y_index + 1)],
                                  [(x_index - 1, y_index + 1)],
                                  [(x_index - 1, y_index)]], 'G')

            # Highlight possible move

    def piece_move_highlight(possible_moves, turn):
        for path in possible_moves:
            for position in path:
                if -1 < position[1] < 9 and -1 < position[0] < 9:
                    if piece_state[position[1]][position[0]] == '':
                        highlight_state[position[1]][position[0]] = 'M'

                    elif piece_state[position[1]][position[0]][0] != turn:
                        highlight_state[position[1]][position[0]] = 'A'
                        break

                    elif piece_state[position[1]][position[0]][0] == turn:
                        break

    # Clear highlight
    def clear_highlight():
        for row in range(len(highlight_state)):
            for column in range(len(highlight_state[row])):
                highlight_state[row][column] = ''

        for side in range(len(stand_active_state)):
            for piece in range(len(stand_active_state[side])):
                stand_active_state[side][piece] = False

    # Render the board
    draw_screen()

    # Running program
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                square_select(position)

                draw_screen()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


# Run shogi
if __name__ == "__main__":
    shogi_run()
