from cs1graphics import *
from time import sleep

w = 1000 # Width of the Canvas

paper = Canvas(w, w*0.6, 'lightblue' ,'The Ostrich and The Rabbit',)

# Landscape

greenpart = Rectangle(w, w*0.3, Point(w*0.5, w*0.45))
greenpart.setFillColor('Green')
greenpart.setBorderColor('Green')
paper.add(greenpart)

# Tree Layer

tree = Layer()

foliage1 = Circle(w*0.05, Point(0, -w*0.02))
foliage1.setFillColor('green')

foliage2 = Circle(w*0.05, Point(-w*0.02, w*0.005))
foliage2.setFillColor('green')

foliage3 = Circle(w*0.05, Point(w*0.02, w*0.005))
foliage3.setFillColor('green')

trunk = Rectangle(w*0.03, w*0.15, Point(0, w*0.1))
trunk.setBorderColor((210,105,30))
trunk.setFillColor((210,105,30))

tree.add(trunk)
tree.add(foliage3)
tree.add(foliage2)
tree.add(foliage1)

tree1 = tree.clone()
tree1.moveTo(w*0.93-830, w*0.2+200)
tree1.scale(0.6)
paper.add(tree1)

# Eggs Layer

eggs = Layer()

egg1 = Ellipse(20, 40, Point(0,0))
egg1.setFillColor('White')

egg2 = Ellipse(20, 40, Point(-10,20))
egg2.setFillColor('White')

egg3 = Ellipse(20, 40, Point(10,20))
egg3.setFillColor('White')

eggs.add(egg1)
eggs.add(egg2)
eggs.add(egg3)

eggs.moveTo(500, 550)
paper.add(eggs)


# Ostrich Layer

ostrich = Layer()

head = Ellipse(30, 20, Point(-8, -85))
head.setFillColor('White')

eye = Circle(2, Point(-15, -85))
eye.setFillColor('Black')

mouth = Polygon(Point(0, 0), Point(20, 20), Point(40, 0))
mouth.setFillColor('White')
mouth.moveTo(-15, -85)
mouth.rotate(150)
mouth.scale(0.5)

head1 = Path(Point(0, -80), Point(0, -30), Point(20, 0))
head1.setBorderWidth(7)

body = Ellipse(90, 40, Point(50, 0))
body.setFillColor('White')

feet1 = Path(Point(0, -80), Point(0, -30), Point( 20, 0))
feet1.rotate(180)
feet1.setBorderWidth(7)
feet1.moveTo(60, 90)

feet2 = Path(Point(0, -80), Point(0, -30), Point( 20, 0))
feet2.rotate(180)
feet2.setBorderWidth(7)
feet2.moveTo(80, 90)

ostrich.add(feet1)
ostrich.add(feet2)
ostrich.add(mouth)
ostrich.add(head1)
ostrich.add(head)
ostrich.add(eye)
ostrich.add(body)

ostrich.scale(0.7)
ostrich.flip()
paper.add(ostrich)

ostrich.moveTo(-30, 450)


# Rabbit Layer

rabbit = Layer()

head = Ellipse(80, 40, Point(0, -40))
head.setFillColor('White')
head.rotate(-30)

eye = Circle(5, Point(-15, -40))
eye.setFillColor('Black')

brow1 = Path(Point(0,0), Point(0,15))
brow1.moveTo(-30, -20)

brow2 = Path(Point(0,0), Point(0,15))
brow2.moveTo(-30, -20)
brow2.rotate(40)

brow3 = Path(Point(0,0), Point(0,15))
brow3.moveTo(-30, -20)
brow3.rotate(80)

ear1 = Ellipse(20, 60, Point(30, -70))
ear1.setFillColor('White')

ear2 = Ellipse(20, 60, Point(15, -70))
ear2.setFillColor('White')
ear2.rotate(-20)

hand1 = Path(Point(0, 0), Point(20, -20), Point(50, -20))
hand1.setBorderWidth(8)
hand1.setBorderColor('White')
hand1.moveTo(-30,30)

hand2 = Path(Point(0, 0), Point(20, -20), Point(50, -20))
hand2.setBorderWidth(8)
hand2.moveTo(-30,30)
hand2.adjustReference(50, -20)
hand2.setBorderColor('White')
hand2.rotate(-20)

feet1 = Path(Point(10, 0), Point(20, -10), Point(50, -10))
feet1.setBorderColor('white')
feet1.setBorderWidth(7)
feet1.rotate(150)
feet1.moveTo(30, 90)

feet2 = Path(Point(10, 0), Point(20, -10), Point(50, -10))
feet2.setBorderColor('white')
feet2.setBorderWidth(7)
feet2.rotate(100)
feet2.moveTo(30, 90)

back = Ellipse(20, 30, Point(0,0))
back.setFillColor('White')
back.moveTo(45, 80)

body = Ellipse(60, 150, Point(30, 20))
body.setFillColor('White')


rabbit.add(back)
rabbit.add(body)
rabbit.add(brow1)
rabbit.add(brow2)
rabbit.add(brow3)
rabbit.add(head)
rabbit.add(ear1)
rabbit.add(ear2)
rabbit.add(eye)
rabbit.add(hand1)
rabbit.add(hand2)
rabbit.add(feet1)
rabbit.add(feet2)

rabbit.scale(0.5)
paper.add(rabbit)

rabbit.moveTo(1100, 500)



# Mountains

mountain = Layer()

mount = Ellipse(w*0.31, w*0.1, Point(0,0))
mount.setFillColor('Green')

mountain.add(mount)
mountain.moveTo(w*0.1, w*0.3)
mountain.setDepth(75)
mountain.setDepth(60)

mountain1 = mountain.clone()
mountain1.moveTo(w*0.2, w*0.3)
paper.add(mountain1)
mountain1.setDepth(60)

mountain2 = mountain.clone()
mountain2.moveTo(w*0.3, w*0.3)
paper.add(mountain2)
mountain2.setDepth(60)

mountain3 = mountain.clone()
mountain3.moveTo(w*0.4, w*0.3)
paper.add(mountain3)
mountain3.setDepth(60)

mountain4 = mountain.clone()
mountain4.moveTo(w*0.55, w*0.3)
paper.add(mountain4)
mountain4.setDepth(60)

mountain5 = mountain.clone()
mountain5.moveTo(w*0.7, w*0.3)
paper.add(mountain5)
mountain5.setDepth(60)

mountain6 = mountain.clone()
mountain6.moveTo(w*0.9, w*0.3)
paper.add(mountain6)
mountain6.setDepth(60)

paper.add(mountain)

# Trees

tree.moveTo(w*0.83-100, w*0.2)
tree.scale(0.5)
paper.add(tree)

tree2 = tree.clone()
tree2.moveTo(w*0.88, w*0.2)
paper.add(tree2)

tree3 = tree.clone()
tree3.moveTo(w*0.93-500, w*0.2)
paper.add(tree3)

tree4 = tree.clone()
tree4.moveTo(w*0.93-350, w*0.2)
paper.add(tree4)

tree5 = tree.clone()
tree5.moveTo(w*0.93-800, w*0.2)
paper.add(tree5)

tree6 = tree.clone()
tree6.moveTo(w*0.93-650, w*0.2)
paper.add(tree6)

# Sun Layer

sun = Layer()

core = Circle(w*0.04, Point(0,0))
core.setFillColor('Yellow')
core.setBorderColor('Yellow')

lighting1 = Path(Point(-w*0.04, -w*0.02), Point(-w*0.08, -w*0.04))
lighting1.setBorderColor('Yellow')
lighting1.setBorderWidth(w*0.005)

lighting2 = Path(Point(w*0.04, -w*0.02), Point(w*0.08, -w*0.04))
lighting2.setBorderColor('Yellow')
lighting2.setBorderWidth(w*0.005)

lighting3 = Path(Point(-w*0.04, w*0.02), Point(-w*0.08, w*0.04))
lighting3.setBorderColor('Yellow')
lighting3.setBorderWidth(w*0.005)

lighting4 = Path(Point(w*0.04, w*0.02), Point(w*0.08, w*0.04))
lighting4.setBorderColor('Yellow')
lighting4.setBorderWidth(w*0.005)

lighting5 = Path(Point(0, -w*0.045), Point(0, -w*0.085))
lighting5.setBorderColor('Yellow')
lighting5.setBorderWidth(w*0.005)

lighting6 = Path(Point(0, w*0.045), Point(0, w*0.085))
lighting6.setBorderColor('Yellow')
lighting6.setBorderWidth(w*0.005)


sun.add(core)
sun.add(lighting1)
sun.add(lighting2)
sun.add(lighting3)
sun.add(lighting4)
sun.add(lighting5)
sun.add(lighting6)

sun.moveTo(w*0.9, w*0.05)
sun.scale(w*0.0007)
paper.add(sun)

# Storyline

text1 = Text("Well! Well! Well! \nThat's my lunch over there!", 14, Point(800, 350))

text2 = Text("Oh, Crap! The Ostrich! Time to run! ", 14, Point(500, 400))

text3 = Text("The End!", 18, Point(500, 100))

# Animation

rabbit.move(-40, 0)
sleep(0.5)
rabbit.move(-40, 0)
sleep(0.5)
rabbit.move(-40, 0)
sleep(0.5)
paper.add(text1)
sleep(0.5)
rabbit.move(-40, 0)
sleep(0.5)
rabbit.move(-40, 0)
sleep(0.5)
rabbit.move(-40, 0)
sleep(0.5)
rabbit.move(-40, 0)
sleep(0.5)
rabbit.move(-40, 0)
sleep(0.5)
rabbit.move(-40, 0)
sleep(0.5)
rabbit.move(-40, 0)
sleep(0.5)
ostrich.move(50, 0)
sleep(0.5)
rabbit.move(-40, 0)
sleep(0.5)
rabbit.move(-40, 0)
sleep(0.75)
ostrich.move(50, 0)
sleep(0.5)
paper.remove(text1)
sleep(0.75)
ostrich.move(50, 0)
sleep(0.5)
rabbit.move(-40, 0)
sleep(0.75)
ostrich.move(50, 0)
sleep(0.5)
ostrich.move(50, 0)
sleep(0.5)
paper.add(text2)

sleep(0.25)
rabbit.flip()
sleep(0.25)
ostrich.move(50, 0)
sleep(0.25)
rabbit.move(40, 0)
sleep(0.25)
ostrich.move(50, 0)

sleep(0.5)
paper.remove(text2)

sleep(0.5)
rabbit.move(40, 0)
sleep(0.5)
ostrich.move(50, 0)
sleep(0.5)
rabbit.move(40, 0)
sleep(0.5)
ostrich.move(50, 0)
sleep(0.5)
rabbit.move(40, 0)
sleep(0.5)
ostrich.move(50, 0)
sleep(0.5)
rabbit.move(40, 0)
sleep(0.5)
ostrich.move(50, 0)

sleep(0.5)
tree.move(-20, 0)
tree1.move(-20, 0)
tree2.move(-20, 0)
tree3.move(-20, 0)
tree4.move(-20, 0)
tree5.move(-20, 0)
tree6.move(-20, 0)
sun.move(-20, 0)
eggs.move(-40, 0)
ostrich.move(50, 0)
rabbit.move(40, 0)

sleep(0.5)
tree.move(-20, 0)
tree1.move(-20, 0)
tree2.move(-20, 0)
tree3.move(-20, 0)
tree4.move(-20, 0)
tree5.move(-20, 0)
tree6.move(-20, 0)
sun.move(-20, 0)
eggs.move(-40, 0)
ostrich.move(50, 0)
rabbit.move(40, 0)

sleep(0.5)
tree.move(-20, 0)
tree1.move(-20, 0)
tree2.move(-20, 0)
tree3.move(-20, 0)
tree4.move(-20, 0)
tree5.move(-20, 0)
tree6.move(-20, 0)
sun.move(-20, 0)
eggs.move(-40, 0)
ostrich.move(50, 0)
rabbit.move(40, 0)

sleep(0.5)
tree.move(-20, 0)
tree1.move(-20, 0)
tree2.move(-20, 0)
tree3.move(-20, 0)
tree4.move(-20, 0)
tree5.move(-20, 0)
tree6.move(-20, 0)
sun.move(-20, 0)
eggs.move(-40, 0)
ostrich.move(50, 0)
rabbit.move(40, 0)

sleep(0.5)
tree.move(-20, 0)
tree1.move(-20, 0)
tree2.move(-20, 0)
tree3.move(-20, 0)
tree4.move(-20, 0)
tree5.move(-20, 0)
tree6.move(-20, 0)
sun.move(-20, 0)
eggs.move(-40, 0)
ostrich.move(50, 0)
rabbit.move(40, 0)

sleep(0.5)
tree.move(-20, 0)
tree1.move(-20, 0)
tree2.move(-20, 0)
tree3.move(-20, 0)
tree4.move(-20, 0)
tree5.move(-20, 0)
tree6.move(-20, 0)
sun.move(-20, 0)
eggs.move(-40, 0)
ostrich.move(50, 0)
rabbit.move(40, 0)

sleep(0.5)
tree.move(-20, 0)
tree1.move(-20, 0)
tree2.move(-20, 0)
tree3.move(-20, 0)
tree4.move(-20, 0)
tree5.move(-20, 0)
tree6.move(-20, 0)
sun.move(-20, 0)
eggs.move(-40, 0)
ostrich.move(50, 0)
rabbit.move(40, 0)

sleep(0.5)
tree.move(-20, 0)
tree1.move(-20, 0)
tree2.move(-20, 0)
tree3.move(-20, 0)
tree4.move(-20, 0)
tree5.move(-20, 0)
tree6.move(-20, 0)
sun.move(-20, 0)
eggs.move(-40, 0)
ostrich.move(50, 0)
rabbit.move(40, 0)

sleep(0.5)
tree.move(-20, 0)
tree1.move(-20, 0)
tree2.move(-20, 0)
tree3.move(-20, 0)
tree4.move(-20, 0)
tree5.move(-20, 0)
tree6.move(-20, 0)
sun.move(-20, 0)
eggs.move(-40, 0)
ostrich.move(50, 0)
rabbit.move(40, 0)

sleep(0.5)
tree.move(-20, 0)
tree2.move(-20, 0)
tree3.move(-20, 0)
tree4.move(-20, 0)
tree5.move(-20, 0)
tree6.move(-20, 0)
sun.move(-20, 0)
eggs.move(-40, 0)
ostrich.move(50, 0)
rabbit.move(40, 0)

sleep(0.5)
tree.move(-20, 0)
tree2.move(-20, 0)
tree3.move(-20, 0)
tree4.move(-20, 0)
tree5.move(-20, 0)
tree6.move(-20, 0)
sun.move(-20, 0)
eggs.move(-40, 0)
ostrich.move(50, 0)
rabbit.move(40, 0)

sleep(0.5)
paper.add(text3)
paper.setBackgroundColor('grey')
sleep(0.25)
paper.setBackgroundColor('white')
sleep(0.25)
paper.setBackgroundColor('lightblue')
sleep(0.25)
paper.setBackgroundColor('grey')
sleep(0.25)
paper.setBackgroundColor('white')
sleep(0.25)
paper.setBackgroundColor('lightblue')