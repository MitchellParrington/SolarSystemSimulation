import os;
import sys; 
sys.path.append(os.path.dirname(os.path.realpath(__file__)));
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "true";

import pygame;
from pygame import HWSURFACE, DOUBLEBUF, K_BACKSPACE, K_SPACE, RESIZABLE, SRCALPHA, K_a, K_z;


import time


# TYPE 'MACROS'
Color:type[pygame.color.Color] = pygame.color.Color;
Font:type[pygame.font.Font] = pygame.font.Font;
Surface:type[pygame.surface.Surface] = pygame.surface.Surface;

CoordTF:type[tuple[float,float]] = tuple[float,float];
CoordTI:type[tuple[int,int]] = tuple[int,int];
CoordC:type[complex] = complex;

DEFAULT_TEXTCOLOR:Color = Color(200,200,200,250); # realise not full transparancy
DEFAULT_TEXTBGCOLOR:Color = Color(100,100,250);

NULLCOLOR:Color = Color(0,0,0,0);


def cctti(coord:CoordC) -> CoordTI: # cctti --> "coord, complex to tuple int"
    return (int(coord.real), int(coord.imag));

def ccttf(coord:CoordC) -> CoordTF: # ccttf --> "coord, complex to tuple float"
    return (float(coord.real), float(coord.imag));

def cttc(coord:CoordTF|CoordTI) -> CoordC:
    return complex(coord[0], coord[1]);

def ShiftPosition(position:CoordC, size:CoordC, placement:CoordC) -> CoordC:
    return position - complex(size.real * placement.real, size.imag * placement.imag);

class Label:
    surface:Surface;

    def __init__(self) -> None:
        self.GenSurface();
        return None;

    def GetSize(self) -> CoordC: # please overide
        return complex(0,0);

    def GenSurface(self) -> None: # please overide
        self.surface = Surface((0,0));
        return None;

    def GetSurface(self) -> Surface:
        return self.surface;


class TextLabel(Label):
    font:Font;
    text:str;
    color:Color;
    bgcolor:Color;

    def __init__(self, font:Font, text:str, color:Color=NULLCOLOR, bgcolor:Color=NULLCOLOR) -> None:
        self.font = font;
        self.text = text;
        self.color = color;
        self.bgcolor = bgcolor;
        self.GenSurface();
        return None;

    def GetSize(self) -> CoordC:
        return complex(*self.font.size(self.text + "|"));

    def GenSurface(self) -> None:
        adder:str = " " if time.time() % 1 < 0.5 else "|";
        self.surface = self.font.render(self.text + adder, True, self.color, self.bgcolor);
        return None;


class Button:
    contents:Label;
    displacement:CoordC;
    placement:CoordC;
    displacementRaw:CoordC;

    def __init__(self, contents:Label, displacement:CoordC=complex(0,0), placement:CoordC=complex(0.5,0.5)) -> None:
        self.contents = contents;
        self.placement = placement;
        self.displacementRaw = displacement;
        self.displacement = ShiftPosition(displacement, contents.GetSize(), placement);
        return None;
        
    def GenDisplacement(self) -> None:
        self.displacement = ShiftPosition(self.displacementRaw, self.contents.GetSize(), self.placement);
        return None;



if __name__ == "__main__":

    dims:complex = complex(1080, 720);

    pygame.init();
    pygame.display.set_caption("option manager yay");
    pygame.event.poll();

    window = pygame.display.set_mode(cctti(dims), HWSURFACE|DOUBLEBUF|RESIZABLE|SRCALPHA);
    surface = pygame.Surface(cctti(dims), SRCALPHA);

    myfont = pygame.font.SysFont("consolas", 25);

    clock = pygame.time.Clock();

    bigtext:TextLabel = TextLabel(myfont, "hey there", DEFAULT_TEXTCOLOR, NULLCOLOR);
    bigbutton:Button = Button(bigtext, dims / 2);

    # typing:bool = True;
    running:bool = True;
    tiks:int = 0;
    while running:
        tiks += 1;
        dt = clock.tick(480) / 1000;

        mousePosC:complex = complex(*pygame.mouse.get_pos());
        mouseRelC:complex = complex(*pygame.mouse.get_rel());

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
            if event.type == pygame.VIDEORESIZE:
                dims = cttc(window.get_size());
            if event.type == pygame.MOUSEWHEEL:
                pass
            if event.type == pygame.KEYDOWN:
                key:int = event.key
                if (key >= K_a and key <= K_z) or key == K_SPACE:
                    bigbutton.contents.text += chr(key);
                    bigbutton.contents.GenSurface();
                    bigbutton.GenDisplacement();
                if key == K_BACKSPACE:
                    if len(bigbutton.contents.text) > 0:
                        bigbutton.contents.text = bigbutton.contents.text[:-1];
                        bigbutton.contents.GenSurface();
                        bigbutton.GenDisplacement();

                if key == ord('q'): # 'q' key pressed
                    running = False;

        if time.time() % 0.5 < 0.25:
            bigbutton.contents.GenSurface();
            bigbutton.GenDisplacement();

        surface.fill((0,0,0));

        windowSize = window.get_rect().size;

        surface.blit(bigbutton.contents.surface, cctti(bigbutton.displacement))

        window.blit(pygame.transform.scale(surface, windowSize), (0.0,0.0));
        pygame.display.flip();

    
    pygame.display.quit();
    pygame.quit();