import os;
import sys; 
sys.path.append(os.path.dirname(os.path.realpath(__file__)));
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "true";

import pygame;
from pygame import DOUBLEBUF, HWSURFACE, RESIZABLE, SRCALPHA;

import math;
import numpy as np;
import cmath;

import time;

# LOCAL
from util.ctp import ctp;
from config import *;
from body import Body, ForceOnBody, ctp, SOLAR_SYSTEM_BODIES; 
from transform import *;


from system import System;
from text import TextHandler, Label;



class Program:
    def __init__(self, window_dimensions:tuple[float,float], name:str="Unknown Program"):
        pass

    def Setup(self) -> int:
        return RETURNCODE_SUCCESS;

    def Loop(self) -> int:

        begintime:float = time.time();
        tiks:int = 0;
        dt:float = 0.0;
        return RETURNCODE_SUCCESS;

    def Frame(self, dt:float, tick:int) -> int:
        return RETURNCODE_SUCCESS;

    

def main(args:list[str]) -> int:

    mainreturnval = 0;

    mainbegintime:float = time.time();

    name:str = "planets yay";
    dimsC:complex = complex(WINDOW_WIDTH, WINDOW_HEIGHT);
    dims:tuple = ctp(dimsC);

    pygame.init();
    pygame.display.set_caption("planets yay");
    pygame.event.poll();

    window = pygame.display.set_mode(dims, HWSURFACE|DOUBLEBUF|RESIZABLE|SRCALPHA);
    surface = pygame.Surface(dims, SRCALPHA);

    myfont = pygame.font.SysFont("consolas", 15);

    textHandler = TextHandler(["consolas", "monospace", "cascadia mono",], 15, (230,30,30), (120,10,10));

    s = System(SOLAR_SYSTEM_BODIES, texthandler=textHandler, target=0);
    
    mouseMovementCurrent:bool = False;
    mousePos:tuple = (0,0);
    timescale:float = 1.0;
    tiks:int = 0;
    paused:bool = False;
    running:bool = True;
    maintimer:float = 0.0;
    timestate:int = 5;
    timestates:list[tuple[float,str]] = [
        (1.0, "1 year"), # years
        (2.0, "6 months"), # half years
        (4.0, "3 months"), # quaters
        (12.0, "1 month"), # months
        (26.0, "2 weeks (fortnight)"), # fortnights
        (52.0, "1 week"), # weeks
        (156.0, "3 days"), # 3 days
        (365.0, "1 day"), # days
        (730.0, "12 hours"), # 12 hours
        (8760.0, "1 hour"), # hours
        (525600.0, "1 minute"), # minutes
        (31536000.0, "1 second"), # seconds
    ];

    # In A Year
    yearsInYear = 1;
    daysInYear = 365 * yearsInYear;
    hoursInYear = 24 * daysInYear;
    minutesInYear = 60 * hoursInYear;
    secondsInYear = 60 * minutesInYear;


    transform:TransformC = TransformC().Tup((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), (1.0, 0.0), (1.0,1.0));

    pauseLabel:Label = Label("Paused", textHandler, (230,30,30), displacement=complex(WINDOW_WIDTH - 5, 5), placement=complex(1,0));

    clock = pygame.time.Clock();

    while running:
        tiks += 1;
        dt = clock.tick(480) / 1000;

        mousePos = pygame.mouse.get_pos();
        mouseRel = pygame.mouse.get_rel();

        mousePosC:complex = complex(*mousePos);
        mouseRelC:complex = complex(*mouseRel);

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
            if event.type == pygame.VIDEORESIZE:
                dims = window.get_size();
            if event.type == pygame.MOUSEWHEEL:
                transform.scale = transform.scale * (1 + event.y * dt);
                surface.fill((0,0,0));
            if event.type == pygame.KEYDOWN:
                key:int = event.key
                if key == ord('n'): # Change Target Planet
                    s.SetTarget(s.target - 1);
                elif key == ord('m'): # Change Target Planet
                    s.SetTarget(s.target + 1);
                elif key == ord('r'): # Restart Program
                    mainreturnval = RETURNCODE_RUNAGAIN;
                    running = False;
                elif key == ord('p'): # Pause Program
                    paused = not paused;
                elif key == ord('.'): # Change Time Speed
                    timestate = (timestate - 1) % len(timestates);
                elif key == ord(','): # Change Time Speed
                    timestate = (timestate + 1) % len(timestates);
                print("keydown", key);
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseMovementCurrent = True;
            if event.type == pygame.MOUSEBUTTONUP:
                mouseMovementCurrent = False;


        if not paused:
            maintimer += dt;

        if mouseMovementCurrent == True:
            transform.translation = transform.translation + mouseRelC;

        pressed = pygame.key.get_pressed();
        if pressed[pygame.K_q]:
            running = False;
            
        if not paused:
            s.UpdateBodies(secondsInYear / timestates[timestate % len(timestates)][0] * dt);

        windowSize = window.get_rect().size;

        surface.fill((0,0,0));

        for b in s.bodies:
            screenspaceCoord:tuple[float,float] = ctp(TransformCoord(
                transform, 
                (b.displacement - s.GetTargetBody().displacement) * math.pow(10, -9)
            ));

            screenspaceRadius:float = math.ceil(transform.Scale(complex(b.diameter * math.pow(10, -9) / 2.0, 0.0)).real);

            if not paused:
                if len(b.history) > 80:
                    b.history.pop(0);
                if len(b.history) == 0:
                    b.history.append(screenspaceCoord);
                b.history.append(screenspaceCoord);


            pygame.draw.circle(
                surface,
                (0.0,255.0,10.0),
                screenspaceCoord,
                screenspaceRadius
            );

        if len(s.bodies[0].history) >= 2:
            for b in s.bodies:
                pygame.draw.aalines(
                    surface,
                    (200.0,200.0,200.0),
                    False,
                    b.history,
                );

        planetOptionLabelOffset:complex = complex(5, 5);

        # surface.blit(s.optlabelall, ctp(s.optposall + planetOptionLabelOffset));
        # surface.blit(s.optlabeltarget, ctp(s.optpostarget + planetOptionLabelOffset));

        surface.blit(s.allLabel.label, ctp(s.allLabel.displacement + planetOptionLabelOffset));
        surface.blit(s.targetLabel.label, ctp(s.targetLabel.displacement + planetOptionLabelOffset));

        timelabel = myfont.render(f"dt: {str(dt)}s Elapsed: {'{:.3f}'.format(maintimer)}s", True, (230,30,30));
        surface.blit(timelabel, (5, 25));
        
        timestatelabel = myfont.render(f"1 second = {timestates[timestate % len(timestates)][1]} simulated", True, (230,30,30));
        surface.blit(timestatelabel, (5, 45));

        if paused:
            surface.blit(pauseLabel.label, ctp(pauseLabel.displacement));

        window.blit(pygame.transform.scale(surface, windowSize), (0.0,0.0));
        pygame.display.flip();

    
    pygame.display.quit();
    pygame.quit();

    return mainreturnval;



if __name__ == "__main__":
    result:int = RETURNCODE_NORUN;
    while True:
        result = main(sys.argv);
        if result != RETURNCODE_RUNAGAIN:
            break;
        elif result == RETURNCODE_RUNAGAIN:
            continue;

    print("Program Exit With Return Code", result);
    input("Press any key to continue...");