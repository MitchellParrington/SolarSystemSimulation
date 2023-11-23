


class TransformC:

    translation:complex = complex(0,0);
    rotation:complex = complex(0,0);
    scale:complex = complex(0,0);

    def __init__(self, t:complex=complex(0,0), r:complex=complex(0,0), s:complex=complex(0,0)):
        self.Com(t,r,s);

    def Com(self, t:complex=complex(0,0), r:complex=complex(0,0), s:complex=complex(0,0)):
        self.translation = t;
        self.rotation = r;
        self.scale = s;
        return self;

    def Tup(self, t:tuple[float,float]=(0,0), r:tuple[float,float]=(0,0), s:tuple[float,float]=(0,0)):
        self.translation = complex(t[0],t[1]);
        self.rotation = complex(r[0],r[1]);
        self.scale = complex(s[0],s[1]);
        return self;

    def Translate(self, coord:complex) -> complex:
        return self.translation + coord;

    def Rotate(self, coord:complex) -> complex:
        return self.rotation * coord;

    def Scale(self, coord:complex) -> complex:
        return complex(self.scale.real * coord.real, self.scale.imag * coord.imag);



def TransformCoord(transform:TransformC, coord:complex=complex(0,0)) -> complex:
    # Scale -> Rotate -> Translate
    
    # Scale
    coord = transform.Scale(coord);

    # Rotate
    coord = transform.Rotate(coord);

    # Translate
    coord = transform.Translate(coord);

    return coord; # + complex(WIDTH / 2, HEIGHT / 2);


def UnTransformCoord(transform:TransformC, coord:complex=complex(0,0), zoomCoord:complex=complex(0,0)) -> complex:
    # coord = coord - complex(WIDTH / 2, HEIGHT / 2);
    coord = coord - transform.translation;
    # coord = coord * complex(1, -transform.rotation);
    # coord = coord - zoomCoord;
    coord = complex(coord.real / transform.scale.real, coord.imag / transform.scale.imag);
    # coord = coord + zoomCoord;
    return coord;





# class Transform_old:
#     def __init__(self, translation:tuple[float,float], rotation:float, scale:tuple[float,float], offset:tuple[float,float]=(0.0,0.0)):
#         self.translation:list[float,float] = [translation[0], translation[1]];
#         self.rotation:float = rotation;
#         self.scale:list[float,float] = [scale[0], scale[1]];
#         self.offset:list[float,float] = [offset[0], offset[1]];
#         self.translationScreenspace:list[float,float] = [0,0];

#     def Translate(self, coord:tuple[float,float]) -> tuple[float,float]:
#         return self.TranslateF(coord, self.translation);

#     def TranslateF(self, coord:tuple[float,float], translation:tuple[float,float]) -> tuple[float,float]:
#         x, y = coord;
#         x += translation[0];
#         y += translation[1];
#         return (x, y);
    
#     def Rotate(self, coord:tuple[float,float]) -> tuple[float,float]:
#         return coord;
#         x = coord[0] * math.cos(self.rotation) - coord[1] * math.sin(self.rotation);
#         y = coord[0] * math.sin(self.rotation) + coord[1] * math.cos(self.rotation);
#         return (x,y);

#     def Scale(self, coord:tuple[float,float]) -> tuple[float,float]:
#         x = coord[0] * self.scale[0];
#         y = coord[1] * self.scale[1];
#         return (x,y);

#     def __call__(self, coord:tuple[float,float]) -> tuple[float,float]:
#         coord = self.Rotate(coord);
#         coord = self.Translate(coord);
#         coord = self.Scale(coord);
#         coord = self.TranslateF(coord, self.translationScreenspace);
#         # coord = self.Scale((coord[0] - self.offset[0], coord[1] - self.offset[1]));
#         coord = (coord[0] + self.offset[0], coord[1] + self.offset[1])
#         return coord;

#         x, y = coord;
#         # a = math.atan2(x,y);
#         # r = math.sqrt(x*x + y*y);
#         # rotate
#         x2 = x*math.cos(self.rotation) - y*math.sin(self.rotation);
#         y2 = x*math.sin(self.rotation) + y*math.cos(self.rotation);
#         # translate
#         x2 += self.translation[0];
#         y2 += self.translation[1];
#         # scale
#         x2 *= self.scale[0];
#         y2 *= self.scale[1];

#         return (x2,y2);
#     # translation:np.ndarray[float,float] = np.array([0.0,0.0]);
#     # rotation:np.ndarray[float,float] = np.array([0.0,0.0]);
#     # scale:np.ndarray[float,float] = np.array([0.0,0.0]);

# def transformCoord(coord:tuple[float,float], trans:tuple[tuple[float,float],float,float]) -> tuple[float,float]:
#     pass




