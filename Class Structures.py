class Garden():
    class Tree():
        def __init__(self, age, kind):
            self.age = age
            self.kind = kind

            class Leaf():
                def __init__(self, color, shape):
                    self.color = color
                    self.shape = shape

            class Fruit():
                def __init__(self, kind):
                    self.kind = kind

    class Ground():
        class Flower():
            def __init__(self, kind, color):
                self.kind = kind
                self.color = color

        class Ground_Shape():
            def __init__(self, weather):
                self.weather = weather

bnm_agac = Garden.Tree(age=10, kind="Pine")
bnm_yaprak = bnm_agac.Leaf(color="Green", shape="Pointy")
bnm_cicek = Garden.Ground.Flower(kind="Edelweiss", color="White")
bnm_sekil = Garden.Ground.Ground_Shape(weather="Snowy")

print(bnm_agac.age)
print(bnm_yaprak.color)
print(bnm_cicek.kind)
print(bnm_sekil.weather)
