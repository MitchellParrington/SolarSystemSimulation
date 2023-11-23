
from itertools import combinations
import pygame

from text import TextHandler, Label, ShortenName;
from body import Body, ForceOnBody;

class System:

    texthandler:TextHandler;

    bodies:list[Body] = [];
    target:int;

    # Text / Lables
    opttextmaxchars:int = 6;
    targetLabel:Label;
    allLabel:Label;

    def __init__(self, bodies:list[Body], texthandler:TextHandler, target:int=0):
        if len(bodies) == 0:
            raise Exception("EmptySystemError");
        if target > len(bodies):
            target = len(bodies) - 1;
        if target < 0:
            target = 0;
        
        self.bodies = bodies;
        self.target = target;
        self.texthandler = texthandler;

        self.GenAllLabel();
        self.GenTargetLabel();

    def GenAllLabel(self) -> None:
        text:str = " ".join(ShortenName(b.name, self.opttextmaxchars) for b in self.bodies);
        self.allLabel = Label(text, self.texthandler, self.texthandler.dtextcolor);
        return None;

    def GenTargetLabel(self) -> None:
        offsetText:str = "".join(ShortenName(b.name, self.opttextmaxchars) + " " for b in self.bodies[:self.target]);
        offsetWidth:int = self.texthandler.GetSize(offsetText)[0];
        text:str = ShortenName(self.GetTargetBody().name, self.opttextmaxchars);
        # self.targetLabel = Label(text, self.texthandler, color=self.texthandler.dtextcolor, bgcolor=self.texthandler.dhighlightcolor, displacement=complex(offsetWidth, 0));
        self.targetLabel = Label(text, self.texthandler, color=self.texthandler.dtextcolor, displacement=complex(offsetWidth, 0));
        return None;

    def SetTarget(self, target:int) -> None:
        if self.target != target:
            for b in self.bodies:
                b.history = [];
        self.target = target % len(self.bodies);
        self.GenAllLabel();
        self.GenTargetLabel();

        return None;

    def GetTargetBody(self) -> Body:
        return self.bodies[self.target % len(self.bodies)];

    def UpdateBodies(self, dt:float) -> None:
        for n, m in combinations(range(len(self.bodies)), 2):
            force:complex = ForceOnBody(self.bodies[n], self.bodies[m]);
            self.bodies[n].UpdateVelocity(dt, force);
            self.bodies[m].UpdateVelocity(dt, force * (-1)); # force in oppisate direction
        for n in range(len(self.bodies)):
            self.bodies[n].UpdateDisplacement(dt);
        return None;


