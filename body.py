
import math;

from util.ctp import ctp;

GRAVITATIONAL_CONSTANT = 6.6743 * math.pow(10, -11);

class Body:
    mass:float;
    diameter:float;
    displacement:complex;
    velocity:complex;

    history:list[tuple[float,float]];
    name:str;
    effective:bool;

    def __init__(self, mass:float, displacement:complex=complex(0.0,0.0), velocity:complex=complex(0.0,0.0), diameter:float=1.0, effective:bool=True, name:str="Unknown"):
        self.mass = mass;
        self.displacement = displacement;
        self.velocity = velocity;
        self.diameter = diameter;
        self.history = [];
        self.name = name;
        self.effective = effective;

    def UpdateDisplacement(self, dt:float) -> None:
        ds:float = self.velocity * dt;
        self.displacement += ds;

    def UpdateVelocity(self, dt:float, force:complex) -> None:
        a:complex = force / self.mass;
        dv:complex = a * dt;
        self.velocity += dv;



def ForceOnBody(body:Body, otherBody:Body) -> complex:
    diff:complex = otherBody.displacement - body.displacement;
    distance:float = abs(diff);
    force:complex = (diff / distance) * ( GRAVITATIONAL_CONSTANT * body.mass * otherBody.mass ) / math.pow(distance, 2);
    return force; 


# BODIES

SOLAR_SYSTEM_BODIES:list[Body,] = [
    Body(
        mass=1.989 * math.pow(10, 30), 
        displacement=complex(0.000 * math.pow(10, 0)), 
        velocity=complex(0.000, 0.000 * math.pow(10, 0)), 
        diameter=1.3927 * math.pow(10, 6),
        name="Sun",
        ), # sun!!

    Body(
        mass=0.330 * math.pow(10, 24), 
        displacement=complex(57.90 * math.pow(10, 9)), 
        velocity=complex(0.000, 47.40 * math.pow(10, 3)), 
        diameter=4879.0 * math.pow(10, 3),
        name="Mercury"
        ), # mercury

    Body(
        mass=4.870 * math.pow(10, 24), 
        displacement=complex(108.2 * math.pow(10, 9)), 
        velocity=complex(0.000, 35.00 * math.pow(10, 3)),
        diameter=12104.0 * math.pow(10, 3),
        name="Venus"
        ), # venus

    Body(
        mass=5.970 * math.pow(10, 24), 
        displacement=complex(149.6 * math.pow(10, 9)), 
        velocity=complex(0.000, 29.80 * math.pow(10, 3)), 
        diameter=12756.0 * math.pow(10, 3),
        name="Earth"
        ), # earth

    Body(
        mass=0.073 * math.pow(10, 24), 
        displacement=complex(149.984*math.pow(10, 9)), 
        velocity=complex(0.000, 30.80 * math.pow(10, 3)), 
        diameter=3475.0 * math.pow(10, 3),
        name="Moon"
        ), # mooooon

    Body(
        mass=0.642 * math.pow(10, 24), 
        displacement=complex(228.0 * math.pow(10, 9)), 
        velocity=complex(0.000, 24.10 * math.pow(10, 3)), 
        diameter=6792.0 * math.pow(10, 3),
        name="Mars"
        ), # mars

    Body(
        mass=1898. * math.pow(10, 24), 
        displacement=complex(778.5 * math.pow(10, 9)), 
        velocity=complex(0.000, 13.10 * math.pow(10, 3)),
        diameter=142984.0 * math.pow(10, 3), 
        name="Jupiter"
        ), # jupiter

    Body(
        mass=568.0 * math.pow(10, 24), 
        displacement=complex(1432. * math.pow(10, 9)), 
        velocity=complex(0.000, 9.700 * math.pow(10, 3)), 
        diameter=120536.0 * math.pow(10, 3),
        name="Saturn"
        ), # saturn

    Body(
        mass=86.80 * math.pow(10, 24), 
        displacement=complex(2867. * math.pow(10, 9)), 
        velocity=complex(0.000, 6.800 * math.pow(10, 3)), 
        diameter=51118.0 * math.pow(10, 3),
        name="Uranus"
        ), # uranus 

    Body(
        mass=102.0 * math.pow(10, 24), 
        displacement=complex(4515. * math.pow(10, 9)), 
        velocity=complex(0.000, 5.400 * math.pow(10, 3)), 
        diameter=49528.0 * math.pow(10, 3),
        name="Neptune"
        ), # neptune

    Body(
        mass=0.013 * math.pow(10, 24), 
        displacement=complex(5906. * math.pow(10, 9)), 
        velocity=complex(0.000, 4.700 * math.pow(10, 3)), 
        diameter=2376.0 * math.pow(10, 3),
        name="Pluto"
        ), # pluto...
];