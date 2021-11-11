from cs1graphics import *

class Duck(Layer):
    def __init__(self, color = "White", eyeColor = "black"):
        """
        Create a new Duck instance
        
        It has "white" as the default skin color.
        """
        super().__init__()
        
        if not isinstance(color, str):
            raise TypeError('Invalid Color')
        
        self._skinColor = color
        self._eyeColor = eyeColor
        
        self._head = Ellipse(30, 20, Point(-8, -85))
        self._head.move(0, 37)
        self._head.rotate(-20)

        self.setEyeColor(self._eyeColor)

        # Close Mouth
        self._closeMouth = Polygon(Point(0, 0), Point(15, 15), Point(40, 0))
        self._closeMouth.setFillColor('Orange')
        self._closeMouth.setBorderColor('Orange')
        self._closeMouth.moveTo(-13, -80)
        self._closeMouth.move(3, 43)
        self._closeMouth.rotate(180)
        self._closeMouth.scale(0.7)

        self._neck = Path(Point(0, -80), Point(0, -30), Point(20, 0))
        self._neck.move(3, 33)
        self._neck.scale(0.5)
        self._neck.setBorderWidth(10)

        self._body = Ellipse(100, 60, Point(50, 0))
        self._body.rotate(15)

        self._firstFeet = Path(Point(0, -25), Point(0, -5), Point(15, 0))
        self._firstFeet.flip()
        self._firstFeet.setBorderWidth(7)
        self._firstFeet.setBorderColor('Orange')

        self._secondFeet = self._firstFeet.clone()
        self._secondFeet.moveTo(80, 30)
        self._firstFeet.moveTo(60, 30)

        self.setSkinColor(self._skinColor)

        self.add(self._firstFeet)
        self.add(self._secondFeet)
        self.add(self._closeMouth)
        self.add(self._neck)
        self.add(self._head)
        self.add(self._eye)
        self.add(self._body)

        self.scale(0.7)
        self.flip()
    
    def openMouth(self):
        """
        This method allows to change the mouth of the duck.
        Opens duck's mouth.
        """
        self._openMouth = Polygon(Point(0, 0), Point(10, 15), Point(10, -15), Point(-15, 0))
        self._openMouth.setFillColor('Orange')
        self._openMouth.setBorderColor('Orange')
        self._openMouth.moveTo(-28, -80)
        self._openMouth.move(3, 43)
        self._openMouth.rotate(40)
        self._openMouth.scale(0.5)
        self.remove(self._closeMouth)
        self.add(self._openMouth)

    def setSkinColor(self, color):
        """
        This method sets the skin color of the body
        """
        if not isinstance(color, str):
            raise TypeError('Invalid Color')

        self._skinColor = color
        self._head.setFillColor(self._skinColor)
        self._head.setBorderColor(self._skinColor)
        self._neck.setBorderColor(self._skinColor)
        self._body.setFillColor(self._skinColor)
        self._body.setBorderColor(self._skinColor)

    def setEyeColor(self, color):
        """
        This method sets the color of the eye
        """
        if not isinstance(color, str):
            raise TypeError('Invalid Color')

        self._eye = Circle(3, Point(-15, -85))
        self._eye.move(3, 37)
        self._eye.setFillColor(self._eyeColor)

if __name__ == "__main__":
    paper = Canvas(400, 400, 'lightblue', 'Duck')
    duckOne = Duck()
    duckTwo = Duck('grey', 'blue')
    duckThree = Duck('black', 'white')
    duckFour = Duck('Yellow')
    
    duckOne.moveTo(200, 150)
    duckTwo.moveTo(300, 150)
    duckThree.moveTo(200, 250)
    duckFour.moveTo(300, 250)
    
    duckOne.openMouth()
    duckThree.openMouth()

    paper.add(duckOne)
    paper.add(duckTwo)
    paper.add(duckThree)
    paper.add(duckFour)
