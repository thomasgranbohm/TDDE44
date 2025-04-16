
import lab5
import random


def random_layout(squares, frame_height, frame_width):
    for square in squares:
        square_size = square.winfo_width()
        xpos = random.randint(0, frame_width - square_size)
        ypos = random.randint(0, frame_height - square_size)
        square.place(x=xpos, y=ypos)

def row_layout(squares, frame_height, frame_width):
    SQUARE_SIZE = max([x.winfo_width() for x in squares]) 
    MIN_SPACING = 10
    SQUARE_FRAME = (SQUARE_SIZE + MIN_SPACING)

    x_pos, y_pos = 0, 0
    
    for square in squares:
        if y_pos + SQUARE_FRAME >= frame_height:
            break;
        
        padding = (SQUARE_FRAME - square.winfo_width()) / 2
        x_place, y_place = x_pos + padding, y_pos + padding
        square.place(x=x_place, y=y_place)

        if x_pos + (2 * SQUARE_FRAME) >= frame_width:
            x_pos = 0
            y_pos += SQUARE_FRAME
        else: 
            x_pos += SQUARE_FRAME

if __name__ == "__main__":
    layout_tester = lab5.LayoutTester(row_layout)
    
