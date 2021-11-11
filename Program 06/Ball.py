from math import sqrt

class Ball:
    def __init__(self, px = 0, py = 0, vx = 0, vy = 0):
        self._posX = px
        self._posY = py
        self._velX = vx
        self._velY = vy
    
    def getPositionX(self):
        return self._posX
    
    def getPositionY(self):
        return self._posY
    
    def getVelocityX(self):
        return self._velX
    
    def getVelocityY(self):
        return self._velY
    
    def advance(self, world):
        # The gravity applying on the ball
        gravity = world.getGravity()
        
        # Changing the X position
        self._posX += self._velX
        
        if gravity > 0:
            self._posY += self._velY  # Changing the Y position
            self._velY += gravity  # Changing the X velocity
        else:
            self._posY -= self._velY
            self._velY += gravity

        
        
        

        