# ---------------------------
# 显式谓词定义
# ---------------------------


class SITE:
    """
    谓词 SITE(x, y): 表示个体 x 位于位置 y。
    个体 x 的取值 {Monkey, Box}；
    y 的取值 {a, b, c}
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(("SITE", self.x, self.y))

    def __eq__(self, other):
        return isinstance(other, SITE) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"SITE({self.x}, {self.y})"


class HANG:
    """
    谓词 HANG(w, y): 表示物体 w 悬挂在位置 y 处。
    w 的取值 {Banana}；
    y 的取值 {a, b, c}
    """

    def __init__(self, w, y):
        self.w = w
        self.y = y

    def __hash__(self):
        return hash(("HANG", self.w, self.y))

    def __eq__(self, other):
        return isinstance(other, HANG) and self.w == other.w and self.y == other.y

    def __repr__(self):
        return f"HANG({self.w}, {self.y})"


class ON:
    """
    谓词 ON(z): 表示个体 z 正在箱子上面。
    z 的取值 {Monkey}
    """

    def __init__(self, z):
        self.z = z

    def __hash__(self):
        return hash(("ON", self.z))

    def __eq__(self, other):
        return isinstance(other, ON) and self.z == other.z

    def __repr__(self):
        return f"ON({self.z})"


class HOLDS:
    """
    谓词 HOLDS(z): 表示个体 z 手里拿着香蕉。
    z 的取值 {Monkey}
    """

    def __init__(self, z):
        self.z = z

    def __hash__(self):
        return hash(("HOLDS", self.z))

    def __eq__(self, other):
        return isinstance(other, HOLDS) and self.z == other.z

    def __repr__(self):
        return f"HOLDS({self.z})"
