
import pygame

from util.ctp import ctp;

def ShortenName(text:str, max_len:int) -> str:
    return (text + " " * max_len)[:max_len].strip();


class TextHandler:
    font:pygame.font.Font;
    dtextcolor:tuple[float,float,float];
    dhighlightcolor:tuple[float,float,float];

    def __init__(self, fontnames:list[str], size:int, color:tuple[float,float,float]=(200.0,200.0,200.0), highlight:tuple[float,float,float]=(100.0,100.0,100.0)):
        self.font = pygame.font.SysFont(fontnames, size);
        self.dtextcolor = color;
        self.dhighlightcolor = highlight;

    def GetSize(self, text:str) -> tuple[int,int]:
        return pygame.font.Font.size(self.font, text);

    def GetSurface(self, text:str, color:tuple[float,float,float]=None, highlight:bool=False, highlightcolor:tuple[float,float,float]=None) -> pygame.Surface:
        if color == None:
            color = self.dtextcolor;
        if highlight:
            if highlightcolor == None:
                highlightcolor = self.dhighlightcolor;
            return self.font.render(text, True, color, highlightcolor);
        else:
            return self.font.render(text, True, color, None);



class Label:
    text:str;
    textHandler:TextHandler;
    label:pygame.Surface;
    displacement:complex;
    color:tuple[float,float,float];
    bg:bool;
    bgcolor:tuple[float,float,float];

    def __init__(self, text:str, text_handler:TextHandler, color:tuple[float,float,float]=(255,255,255), bgcolor:tuple[float,float,float]=None, displacement:complex=complex(0,0), placement=complex(0,0)):
        self.text = text;
        self.textHandler = text_handler;
        self.color = color;
        self.bgcolor = bgcolor;
        self.bg = False if bgcolor==None else True;
        textSize = self.textHandler.GetSize(self.text);
        self.displacement = displacement - placement.real * textSize[0] - placement.imag * textSize[1] * 1j;
        self.GenLabel();

    def GenLabel(self) -> None:
        self.label = self.textHandler.GetSurface(self.text, self.color, self.bg, self.bgcolor);
        pygame.draw.rect(self.label, (200,200,200), pygame.Rect((0,0), self.textHandler.GetSize(self.text)), width=2, border_radius=5);
        print(ctp(self.displacement), self.textHandler.GetSize(self.text));
        return None;

    def UpdateText(self, text:str) -> None:
        self.text = text;
        self.GenLabel();
        return None;
