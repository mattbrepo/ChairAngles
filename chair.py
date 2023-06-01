import turtle
import math

def mycos(degree):
  return math.cos(math.radians(degree))

def mysin(degree):
  return math.sin(math.radians(degree))

def calculate(l, m, h, b, c, d, e, f):
  t = h + 2 * f
  u = m - d - 2 * e - b
  
  # quadratic equation
  snddeg_a = (u**2 / t**2 + 1)
  snddeg_b = -2*u*h / t**2
  snddeg_c = h**2 / t**2 - 1
  snddeg1 = (-snddeg_b + math.sqrt(snddeg_b**2 - 4 * snddeg_a * snddeg_c)) / (2 * snddeg_a)
  snddeg2 = (-snddeg_b - math.sqrt(snddeg_b**2 - 4 * snddeg_a * snddeg_c)) / (2 * snddeg_a)
  
  theta = math.acos(snddeg1)
  theta_deg = math.degrees(theta)
  theta_deg2 = math.degrees(math.acos(snddeg2))
  if theta_deg > theta_deg2:
    theta_deg = theta_deg # prodebug: it may be worth investigating
  
  gamma = theta + math.radians(90)
  gamma_deg = math.degrees(gamma)
  m1 = b + e + (f + h) * math.tan(theta)
  l1 = l - e - c - h / math.cos(theta) + h * math.tan(theta)
  a = math.sqrt(l1 ** 2 + m1 ** 2 - 2 * l1 * m1 * math.cos(gamma))
  alpha = math.asin((m1 * math.sin(gamma)) / a)
  
  alpha_deg = math.degrees(alpha)
  beta_deg = 180 - gamma_deg - alpha_deg
  return (alpha_deg, beta_deg, a, l1, m1)

#def drawMeasurement(t, points, msg, font, msgPoint):
#  t.pencolor('red')
#  drawLines(t, points)
#  t.goto(msgPoint)
#  t.write(msg, font = font)
#  t.pencolor('black')
  
def drawLines(t, points):
  t.penup()
  for point in points:
    t.goto(point)
    t.pendown()
  t.penup()
    
def drawIt(l, m, h, alpha, beta, a, b, c, d, e, f, l1, m1):
  turtle.bgcolor('white')

  t = turtle.Turtle()
  t.pensize(3)
  t.speed(10)
  font = ('Arial', 12, 'normal')
  
  # the origin is the lower cross point between block l and block m
  O = (0, -100)
  antibeta = 180 - 90 - beta
  antialpha = 180 - 90 - alpha
  seat_height = l * mysin(alpha)

  # ground
  t.pencolor('green')
  points = []
  points.append((O[0] - l1 * mycos(alpha) - 150, O[1] - l1 * mysin(alpha)))
  points.append((O[0] + m1 * mycos(beta) + 150, O[1] - m1 * mysin(beta)))
  drawLines(t, points)
  t.pencolor('black')
  
  # key info
  if True:
    t.goto((50, 240))
    t.write('alpha: ' + str(round(alpha, 1)) + '°', font = font)
    t.goto((50, 220))
    t.write('beta: ' + str(round(beta, 1)) + '°', font = font)
    t.goto((50, 200))
    t.write('a: ' + str(round(a, 1)), font = font)
    t.goto((50, 180))
    t.write('seat height: ' + str(round(seat_height, 1)), font = font)
  
  # block m
  points = []
  points.append(O)
  points.append((points[-1][0] + m1 * mycos(beta), points[-1][1] - m1 * mysin(beta))) # go to the previous origin
  points.append((points[-1][0] - m * mycos(beta), points[-1][1] + m * mysin(beta)))
  pointM_LeftUp = points[-1]
  points.append((points[-1][0] + h * mycos(antibeta), points[-1][1] + h * mysin(antibeta)))
  points.append((points[-1][0] + m * mycos(beta), points[-1][1] - m * mysin(beta)))
  pointM_RightDown = points[-1]
  points.append(points[1])
  drawLines(t, points)
  
  # block b
  points = []
  points.append((pointM_RightDown[0] - b * mycos(beta), pointM_RightDown[1] + b * mysin(beta)))
  points.append((points[-1][0] + f * mycos(antibeta), points[-1][1] + f * mysin(antibeta)))
  points.append((points[-1][0] - e * mycos(beta), points[-1][1] + e * mysin(beta)))
  points.append((points[-1][0] - f * mycos(antibeta), points[-1][1] - f * mysin(antibeta)))
  drawLines(t, points)

  # block d
  points = []
  points.append((pointM_LeftUp[0] + (d + e) * mycos(beta), pointM_LeftUp[1] - (d + e) * mysin(beta)))
  points.append((points[-1][0] - f * mycos(antibeta), points[-1][1] - f * mysin(antibeta)))
  points.append((points[-1][0] - e * mycos(beta), points[-1][1] + e * mysin(beta)))
  points.append((points[-1][0] + f * mycos(antibeta), points[-1][1] + f * mysin(antibeta)))
  drawLines(t, points)

  # block l
  points = []
  points.append(O)
  points.append((points[-1][0] - l1 * mycos(alpha), points[-1][1] - l1 * mysin(alpha)))
  points.append((points[-1][0] + l * mycos(alpha), points[-1][1] + l * mysin(alpha)))
  pointL_RightDown = points[-1]
  points.append((points[-1][0] - h * mycos(antialpha), points[-1][1] + h * mysin(antialpha)))
  pointL_RightUp = points[-1]
  points.append((points[-1][0] - l * mycos(alpha), points[-1][1] - l * mysin(alpha)))
  points.append(points[1])
  drawLines(t, points)
  
  # block c
  points = []
  points.append((pointL_RightUp[0] - (c + e) * mycos(alpha), pointL_RightUp[1] - (c + e) * mysin(alpha)))
  points.append((points[-1][0] - f * mycos(antialpha), points[-1][1] + f * mysin(antialpha)))
  points.append((points[-1][0] + e * mycos(alpha), points[-1][1] + e * mysin(alpha)))
  points.append((points[-1][0] + f * mycos(antialpha), points[-1][1] - f * mysin(antialpha)))
  drawLines(t, points)
  
  # prodebug
  # points = []
  # points.append(pointL_RightDown)
  # points.append((points[-1][0], points[-1][1] - seat_height))
  # drawLines(t, points)
  
  # final turtle settings
  t.hideturtle()
  turtle.Screen().exitonclick()  

#
# Main
#

if __name__ == "__main__":
  l = 400
  m = 400
  h = 30
  e = 20
  f = 20

  b = 25
  gap_block_bd = 100
  c = 100
  d = m - 2 * e - gap_block_bd
  
  (alpha, beta, a, l1, m1) = calculate(l, m, h, b, c, d, e, f)
  
  drawIt(l, m, h, alpha, beta, a, b, c, d, e, f, l1, m1)
  
  
  