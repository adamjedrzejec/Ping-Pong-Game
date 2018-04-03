import pygame, sys
black = (0, 0, 0); white = (255, 255, 255); green = (0, 204, 0); grey = (128, 128, 128)
pygame.init()

scr = pygame.display.set_mode((1080, 720))
win = scr.get_rect()


net = pygame.Rect( 0, 0, 50, win.h)
net.center = win.center
ball = pygame.Rect( 0, 0, 30, 30)
ball.center = win.center
paddle1 = pygame.Rect( 0, 0, 30, 60)
paddle1.midleft = win.midleft
paddle2 = pygame.Rect( 0, 0, 30, 60)
paddle2.midright = win.midright

vec = [1,1]
pygame.key.set_repeat(50,12)
fps = pygame.time.Clock()

step = 5

points1 = 0; points2 = 0

#points of the first player
myfont = pygame.font.Font('freesansbold.ttf', 48)
msg1 = myfont.render(str("Points: {0}".format(points1)), True, green)
msg1_box = msg1.get_rect()
msg1_box.center = (win.w/4,win.h/2)

#points of the second player
myfont = pygame.font.Font('freesansbold.ttf', 48)
msg2 = myfont.render(str("Points: {0}".format(points2)), True, green)
msg2_box = msg2.get_rect()
msg2_box.center = (win.w*3/4,win.h/2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                paddle1 = paddle1.move(0,step)
                if paddle1.bottom > win.bottom:
                    paddle1.bottom = win.bottom
                paddle2 = paddle2.move(0,step)
                if paddle2.bottom > win.bottom:
                    paddle2.bottom = win.bottom
            if event.key == pygame.K_UP:
                paddle1 = paddle1.move(0,-step)
                if paddle1.top < win.top:
                    paddle1.top = win.top
                paddle2 = paddle2.move(0,-step)
                if paddle2.top < win.top:
                    paddle2.top = win.top

#collisions ball-wall
    ball = ball.move(vec)
    if not win.contains(ball):
        if ball.left < win.left or ball.right > win.right:
            vec[0] = -vec[0]
        if ball.top < win.top or ball.bottom > win.bottom:
            vec[1] = -vec[1]
#collisions ball-paddle1
    if ball.colliderect(paddle1):
        if (ball.left == (paddle1.right - 1)):
            vec[0] = -vec[0]
        else:
            vec[1] = -vec[1]
#collisions ball-paddle2
    if ball.colliderect(paddle2):
        if (ball.right == (paddle2.left + 1)):
            vec[0] = -vec[0]
        else:
            vec[1] = -vec[1]

#counting points
    if ball.left < win.left:
        points2 += 1
        msg2 = myfont.render(str("Points: {0}".format(points2)), True, green)
    if ball.right > win.right:
        points1 += 1
        msg1 = myfont.render(str("Points: {0}".format(points1)), True, green)



    scr.fill(black)
    scr.blit(msg1, msg1_box)
    scr.blit(msg2, msg2_box)
    pygame.draw.rect(scr,grey,net)
    pygame.draw.rect(scr,white,ball)
    pygame.draw.rect(scr,white,paddle1)
    pygame.draw.rect(scr,white,paddle2)
    pygame.display.flip()
    fps.tick(260)
