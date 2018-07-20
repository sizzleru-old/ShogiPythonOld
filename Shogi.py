# Imports
from pygame import Color
from pygame.locals import *

import pygame
import sys
import math
import os


# Shogi program
def shogi_run():

    # Screen
    size = screen_width, screen_height = 1620, 900
    screen = pygame.display.set_mode(size)

    # Board margin
    board_margin_top = 43
    board_margin_bottom = 43
    board_margin_right = 403
    board_margin_left = 403

    # Stand margin
    stand_margin = 43

    # Dimensions
    line_width = 4
    board_size = screen_width - board_margin_right - board_margin_left
    square_size = int((board_size - 10 * line_width) / 9)
    stand_size = 272

    # Load board
    board_image = pygame.image.load("Others//board.png").convert()

    # Highlight
    highlight = {}

    highlight['A'] = pygame.Surface((square_size, square_size), pygame.SRCALPHA) # Attack
    highlight['S'] = pygame.Surface((square_size, square_size), pygame.SRCALPHA) # Select
    highlight['M'] = pygame.image.load("Others//move.png").convert_alpha() # Move
    
    highlight['A'].fill((255, 0, 0, 120))
    highlight['S'].fill((0, 255, 0, 120))
    
    # Surfaces
    board_surface = pygame.Surface((screen_width, screen_height))
    piece_surface = pygame.Surface((board_size, board_size), pygame.SRCALPHA, 32).convert_alpha()
    stand_surface_gote = pygame.Surface((stand_size, stand_size), pygame.SRCALPHA, 32).convert_alpha()
    stand_surface_sente = pygame.Surface((stand_size, stand_size), pygame.SRCALPHA, 32).convert_alpha()
    highlight_surface = pygame.Surface((board_size, board_size), pygame.SRCALPHA, 32).convert_alpha()

    # Background
    board_surface.blit(board_image, (0,0))

    # Pieces
    pieces = {}
    
    pieces['SP0'] = pygame.image.load("Pieces//SP0.png")
    pieces['SL0'] = pygame.image.load("Pieces//SL0.png")
    pieces['SN0'] = pygame.image.load("Pieces//SN0.png")
    pieces['SS0'] = pygame.image.load("Pieces//SS0.png")
    pieces['SG0'] = pygame.image.load("Pieces//SG0.png")
    pieces['SB0'] = pygame.image.load("Pieces//SB0.png")
    pieces['SR0'] = pygame.image.load("Pieces//SR0.png")
    pieces['SK0'] = pygame.image.load("Pieces//SK0.png")
    pieces['SP1'] = pygame.image.load("Pieces//SP1.png")
    pieces['SL1'] = pygame.image.load("Pieces//SL1.png")
    pieces['SN1'] = pygame.image.load("Pieces//SN1.png")
    pieces['SS1'] = pygame.image.load("Pieces//SS1.png")
    pieces['SB1'] = pygame.image.load("Pieces//SB1.png")
    pieces['SR1'] = pygame.image.load("Pieces//SR1.png")
    pieces['GP0'] = pygame.image.load("Pieces//GP0.png")
    pieces['GL0'] = pygame.image.load("Pieces//GL0.png")
    pieces['GN0'] = pygame.image.load("Pieces//GN0.png")
    pieces['GS0'] = pygame.image.load("Pieces//GS0.png")
    pieces['GG0'] = pygame.image.load("Pieces//GG0.png")
    pieces['GB0'] = pygame.image.load("Pieces//GB0.png")
    pieces['GR0'] = pygame.image.load("Pieces//GR0.png")
    pieces['GK0'] = pygame.image.load("Pieces//GK0.png")
    pieces['GP1'] = pygame.image.load("Pieces//GP1.png")
    pieces['GL1'] = pygame.image.load("Pieces//GL1.png")
    pieces['GN1'] = pygame.image.load("Pieces//GN1.png")
    pieces['GS1'] = pygame.image.load("Pieces//GS1.png")
    pieces['GB1'] = pygame.image.load("Pieces//GB1.png")
    pieces['GR1'] = pygame.image.load("Pieces//GR1.png")

    # Stand pieces
    sp = pygame.image.load("Pieces_tilted//SP0_tilt.png")
    sl = pygame.image.load("Pieces_tilted//SL0_tilt.png")
    sn = pygame.image.load("Pieces_tilted//SN0_tilt.png")
    ss = pygame.image.load("Pieces_tilted//SS0_tilt.png")
    sg = pygame.image.load("Pieces_tilted//SG0_tilt.png")
    sb = pygame.image.load("Pieces_tilted//SB0_tilt.png")
    sr = pygame.image.load("Pieces_tilted//SR0_tilt.png")
    gp = pygame.image.load("Pieces_tilted//GP0_tilt.png")
    gl = pygame.image.load("Pieces_tilted//GL0_tilt.png")
    gn = pygame.image.load("Pieces_tilted//GN0_tilt.png")
    gs = pygame.image.load("Pieces_tilted//GS0_tilt.png")
    gg = pygame.image.load("Pieces_tilted//GG0_tilt.png")
    gb = pygame.image.load("Pieces_tilted//GB0_tilt.png")
    gr = pygame.image.load("Pieces_tilted//GR0_tilt.png")

    # Bishop info
    bishop_br_width = 10
    bishop_br_height = 9
    bishop_width = 72
    bishop_height = 87

    # Rook info
    rook_bl_width = 6
    rook_bl_height = 8
    rook_width = 72
    rook_height = 89

    # Knight info
    knight_tr_width = 24
    knight_tr_height = 14
    knight_tl_width = 23
    knight_tl_height = 14
    knight_width = 86
    knight_height = 86

    # Silver info
    silver_tl_width = 5
    silver_tl_height = 19
    silver_tr_width = 38
    silver_tr_height = 6
    silver_width = 79
    silver_height = 91

    # Gold info
    gold_tl_width = 3
    gold_tl_height = 29
    gold_tr_width = 55
    gold_tr_height = 7
    gold_width = 91
    gold_height = 94

    # Lance info
    lance_tl_width = 34
    lance_tl_height = 4
    lance_tr_width = 9
    lance_tr_height = 15
    lance_width = 91
    lance_height = 94

    # Pawn info
    pawn_tl_width = 49
    pawn_tl_height = 3
    pawn_tr_width = 7
    pawn_tr_height = 26
    pawn_width = 87
    pawn_height = 87

    # Stand piece positions
    bishop_pos = (stand_size / 2 - bishop_width + bishop_br_width - 2,
                  stand_size / 2 - bishop_height + bishop_br_height)
    
    rook_pos = (stand_size / 2 - rook_bl_width ,
                stand_size / 2 + rook_bl_height - rook_height)
    
    knight_pos = (stand_size / 2 - knight_width/2,
                  3 * stand_size / 4 - knight_height/2)
    
    silver_pos = (knight_pos[0] + (knight_width - knight_tr_width) - silver_tl_width + 2,
                  knight_pos[1] + knight_tr_height - silver_tl_height)

    gold_pos = (silver_pos[0] + (silver_width - silver_tr_width) - gold_tl_width + 1,
                  silver_pos[1] + silver_tr_height - gold_tl_height)

    lance_pos = (knight_pos[0] - knight_tl_width - lance_tl_width + lance_tr_width - 1,
                  knight_pos[1] - knight_tl_height + lance_tr_height - 1)

    pawn_pos = (lance_pos[0] + lance_tl_width - pawn_width + pawn_tr_width - 2,
                  lance_pos[1] + lance_tl_height - pawn_tr_height)

    # Other info
    display_distance = stand_size/8
    angle = 9.205
    # States
    piece_state = [['GL0', 'GN0','GS0', 'GG0', 'GK0', 'GG0', 'GS0', 'GN0', 'GL0'],
                   ['', 'GR0', '', '', '', '', '', 'GB0', ''],
                   ['GP0']*9,
                   ['']*9,
                   ['', '', '', '', '', '', '', '', ''],
                   ['']*9,
                   ['SP0']*9,
                   ['', 'SB0', '', '', '', '', '', 'SR0', ''],
                   ['SL0', 'SN0','SS0', 'SG0', 'SK0', 'SS0', 'SG0', 'SN0', 'SL0']]

    highlight_state = [['']*9,
                       ['']*9,
                       ['']*9,
                       ['']*9,
                       ['']*9,
                       ['']*9,
                       ['']*9,
                       ['']*9,
                       ['']*9]

    stand_state = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    # Drawing the pieces
    def draw_pieces():
        piece_surface.fill(Color(0,0,0,0))
        
        for row in range(len(piece_state)):
            for column in range(len(piece_state[row])):
                if piece_state[row][column] != '':
                    piece_surface.blit(pieces[piece_state[row][column]],
                                (line_width + column * (line_width + square_size),
                                 line_width + row * (line_width + square_size)))

    # Draw stand pieces
    def draw_stand():
        
        stand_surface_sente.fill(Color(0,0,0,0))
        stand_surface_gote.fill(Color(0,0,0,0))
        
        for sente_piece_index in range(len(stand_state[0])):
            if stand_state[0][sente_piece_index] != 0:
                if sente_piece_index == 6:
                    stand_surface_sente.blit(sr, rook_pos)

                    display_quantity(stand_state[0][sente_piece_index],
                                     ((rook_pos)[0] - display_distance * math.cos(angle), rook_pos[1] - display_distance * math.sin(angle)))


                elif sente_piece_index == 5:
                    stand_surface_sente.blit(sb, bishop_pos)

                    display_quantity(stand_state[0][sente_piece_index],
                                     ((bishop_pos)[0] + display_distance * math.cos(angle) + bishop_width, - bishop_br_height + bishop_pos[1] + display_distance * math.sin(angle)))
                
                elif sente_piece_index == 4:
                    stand_surface_sente.blit(sg, gold_pos)

                    display_quantity(stand_state[0][sente_piece_index],
                                     ((rook_pos)[0] + display_distance * math.cos(angle), rook_pos[1] + display_distance * math.sin(angle)))

                elif sente_piece_index == 3:
                    stand_surface_sente.blit(ss, silver_pos)

                elif sente_piece_index == 2:
                    stand_surface_sente.blit(sn, knight_pos)

                elif sente_piece_index == 1:
                    stand_surface_sente.blit(sl, lance_pos)

                elif sente_piece_index == 0:
                    stand_surface_sente.blit(sp, pawn_pos)
                    
        for gote_piece_index in range(len(stand_state[1])):
            if stand_state[1][gote_piece_index] != 0:
                if gote_piece_index == 6:
                    stand_surface_gote.blit(sr, rook_pos)

                elif gote_piece_index == 5:
                    stand_surface_gote.blit(sb, bishop_pos)
                
                elif gote_piece_index == 4:
                    stand_surface_gote.blit(sg, gold_pos)

                elif gote_piece_index == 3:
                    stand_surface_gote.blit(ss, silver_pos)

                elif gote_piece_index == 2:
                    stand_surface_gote.blit(sn, knight_pos)

                elif gote_piece_index == 1:
                    stand_surface_gote.blit(sl, lance_pos)

                elif gote_piece_index == 0:
                    stand_surface_gote.blit(sp, pawn_pos)

    # Display number of pieces
    def display_quantity(quantity, position):
        pygame.font.init()
        display_font = pygame.font.Font(None, 50)
        display_surf = display_font.render(str(quantity), 1, (0, 0, 0))

        stand_surface_sente.blit(display_surf, position)
        
    # Drawing the highlight
    def draw_highlight():
        highlight_surface.fill(Color(0,0,0,0))
        
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
        screen.blit(board_surface, (0,0))
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
        x , y = position
        
        if board_margin_left < x < screen_width - board_margin_right and \
           board_margin_top < y < screen_height - board_margin_bottom:
            
            x_index = math.floor((x - board_margin_left - line_width) / (square_size + line_width))
            y_index = math.floor((y - board_margin_top - line_width) / (square_size + line_width))

            if highlight_state[y_index][x_index] == '':
                piece_select(x_index, y_index)

            elif highlight_state[y_index][x_index] == 'M':
                move_piece(x_index, y_index)

            elif highlight_state[y_index][x_index] == 'A':
                move_piece(x_index, y_index)

            elif highlight_state[y_index][x_index] == 'S':
                clear_highlight()
                

    def move_piece(x_index, y_index):
        active = False
        for row in range(len(highlight_state)):
            for column in range(len(highlight_state[row])):
                if highlight_state[row][column] == 'S':
                    x_active = column
                    y_active = row
                    active = True

        if active:
            if highlight_state[y_index][x_index] == 'A':
                piece_add(piece_state[y_index][x_index])
            
            piece_state[y_index][x_index], piece_state[y_active][x_active] = \
                                           piece_state[y_active][x_active], ''

            


            clear_highlight()
            
            x_active = False
            y_active = False

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

    # Piece select
    def piece_select(x_index, y_index):

        # Highlight square
        piece_select_highlight(x_index, y_index)

        # Move type
        piece_rules(x_index, y_index)        
        
    # Piece select highlight
    def piece_select_highlight(x_index, y_index):                
        for row in range(len(highlight_state)):
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
                y_move -=1
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
                                  [(x_index + 1, y_index )],
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
                y_move -=1
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
                                  [(x_index + 1, y_index )],
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
if __name__== "__main__":
    shogi_run()
