import pygame
from PPlay import window
from PPlay import keyboard
from PPlay import gameobject
from PPlay import sprite
from PPlay import collision

width, height = 640, 480
janela = window.Window(width, height)
janela.set_title("PONG")

bola = sprite.Sprite("assets/ball.png")
ball_speed = 200
ballX = ballY = ball_speed

pad1 = sprite.Sprite("assets/pad1.png")
pad1.set_position(0, height/2)
pad2 = sprite.Sprite("assets/pad2.png")
pad2.set_position(janela.width - pad2.width, height/2)
pad_vel = 300
pad1.pontos = 0
pad2.pontos = 0
drawpos1X = janela.width/4

drawpos2X = 3 * janela.width/4

drawposY = janela.height/15

dificuldade = 1

teclado = keyboard.Keyboard()

def rst_pos(GameObject):
    GameObject.set_position(width / 2, height / 2)



while True:
    janela.set_background_color((50, 150, 80))
    bola.draw()
    pad1.draw()
    pad2.draw()
    #bola.update()
    bola.move_x(ballX*janela.delta_time())
    bola.move_y(ballY*janela.delta_time())
    if 0 > bola.x:
        #gol da dir
        rst_pos(bola)
        ballX *= -1
        ballX = ballY = ball_speed
        pad2.pontos+=1
    if bola.x> janela.width:
        # gol da esq
        rst_pos(bola)
        #ballX+=20
        ballX = ballY = ball_speed
        ballX *= -1
        pad1.pontos-=1
    if bola.y >= janela.height - bola.height:
        bola.y = janela.height - bola.height - 1
        ballY += 50
        ballY *= -1
    if bola.y <=3:
        bola.y = 4
        ballY += 50
        ballY *= -1
    if bola.y <= pad2.y + pad2.height / 2 and pad2.y > 0 and bola.x > janela.width/2 - 30:
        pad2.move_y(-pad_vel * janela.delta_time() * dificuldade)
    elif bola.y >= pad2.y + pad2.height / 2 and pad2.y < height - pad2.height and bola.x > janela.width/2 - 30:
        pad2.move_y(pad_vel * janela.delta_time() * dificuldade)

    if teclado.key_pressed("UP") and pad2.y >0 :
        pad2.move_y(-pad_vel*janela.delta_time())
    elif teclado.key_pressed("DOWN") and pad2.y < height-pad2.height:
        pad2.move_y(pad_vel*janela.delta_time())

    if teclado.key_pressed("W") and pad1.y >0 :
        pad1.move_y(-pad_vel*janela.delta_time())
    elif teclado.key_pressed("S") and pad1.y < height-pad1.height:
        pad1.move_y(pad_vel*janela.delta_time())

    if (bola.x + bola.width >= pad2.x and pad2.y+ pad2.height >bola.y+bola.height/2 > pad2.y):
        bola.x = pad2.x - bola.width -1
        ballX*=-1
    if (bola.x <= pad1.x + pad1.width and pad1.y + pad1.height > bola.y + bola.height / 2 > pad1.y):
        bola.x = pad1.x + pad1.width + 1
        ballX *= -1
    janela.draw_text(str(pad1.pontos), drawpos1X, drawposY)
    janela.draw_text(str(pad2.pontos), drawpos2X, drawposY)

    janela.update()