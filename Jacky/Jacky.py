import sys
import pygame
import random
from Button import Button
from Text import Text

deck = [(5, 2), (2, 2), (3, 2), (4, 2), (6, 3), (7, 3), (8, 3), (9, 3), (10, 4),
        (11, 4), (12, 4), (13, 4), (14, 5), (15, 5), (16, 5), (17, 5), (18, 6), (19, 6),
        (20, 6), (21, 6), (22, 7), (23, 7), (24, 7), (25, 7), (26, 8), (27, 8), (28, 8),
        (29, 8), (30, 9), (31, 9), (32, 9), (33, 9), (34, 10), (35, 10), (36, 10), (37, 10),
        (38, 10), (39, 10), (40, 10), (41, 10), (42, 10), (43, 10), (44, 10), (45, 10), (46, 10),
        (47, 10), (48, 10), (49, 10), (50, 11), (51, 11), (52, 11), (53, 11)]

deck2 = []
random.shuffle(deck)

gold = (197, 179, 88)
met_gray = (100, 100, 100)
black = (30, 30, 30)
gray = (169, 169, 169)

pygame.init()
clock = pygame.time.Clock()
w, h = 900, 500
pygame.display.set_caption('Jacky')
pygame.display.set_icon(pygame.image.load('images//icon.bmp'))
sc = pygame.display.set_mode((w, h))
sc.fill(black)

title = pygame.image.load("images//title.png")
bg = pygame.image.load("images//Black_Jack.png")
bg2 = pygame.image.load("images//Black_Jack.png")
backside = pygame.image.load("images//backside1.png")

fps = 30
x, y = 730, 20
dlr, plr = 0, 0
dealer, player = 0, 0
xp, yp = 400, 290
xd, yd = 380, 38

play = Button('PLAY', 200, 100, (350, 350), 10, 60)
hit = Button('HIT', 100, 50, (750, 350), 5, 30)
stand = Button('STAND', 100, 50, (750, 420), 5, 30)
deal = Button('DEAL', 100, 50, (750, 280), 5, 30)
next_round = Button('NEXT', 200, 100, (350, 350), 10, 60)


def play_run():
    global x, y
    sc.blit(bg, (0, 0))
    pygame.time.delay(50)
    if y != 40:
        bg.blit(backside, (x, y))
        x += 1
        y += 1


def deal_run():
    global dealer, player, dlr, plr, deck, deck2
    sc.blit(bg, (0, 0))
    dealerB = Text(f'DEALER Points: {dealer}', 200, 50, (180, 38), 30)
    playerB = Text(f'PLAYER Points: {player}', 200, 50, (180, 290), 30)
    dealerB.draw_t(bg)
    playerB.draw_t(bg)
    if dlr < 1:
        frst_d = deck.pop()
        deck2.append(frst_d)
        card_d = pygame.image.load(f"images//{frst_d[0]}.png")
        bg.blit(card_d, (380, 38))
        dealer += frst_d[1]
        dlr += 1
    if plr < 1:
        frst_p = deck.pop()
        deck2.append(frst_p)
        print(frst_p)
        card_p = pygame.image.load(f"images//{frst_p[0]}.png")
        bg.blit(card_p, (380, 290))
        player += frst_p[1]
        scnd_p = deck.pop()
        print(scnd_p)
        card_p = pygame.image.load(f"images//{scnd_p[0]}.png")
        bg.blit(card_p, (400, 290))
        player += scnd_p[1]
        deck2.append(scnd_p)
        plr += 1
        if len(deck) < 1:
            deck, deck2 = deck2, deck



def pick_card_plr():
    global xp, yp, player, deck2, deck
    xp += 20
    pick = deck.pop()
    card = pygame.image.load(f"images//{pick[0]}.png")
    bg.blit(card, (xp, yp))
    player += pick[1]
    deck2.append(pick)
    if len(deck) < 1:
        deck, deck2 = deck2, deck



def pick_card_dlr():
    global xd, yd, dealer, deck, deck2
    while dealer < 17:
        xd += 20
        pick = deck.pop()
        card = pygame.image.load(f"images//{pick[0]}.png")
        bg.blit(card, (xd, yd))
        dealer += pick[1]
        deck2.append(pick)
        if len(deck) < 7:
            deck, deck2 = deck2, deck



def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def result(text):
    s = pygame.Surface((900, 500))
    s.set_alpha(200)
    s.fill(black)
    sc.blit(s, (0, 0))
    dealerB = Text(text, 500, 100, (200, 150), 60)
    dealerB.draw_t(sc)


def start():
    global period_game
    if period_game == 'start':
        sc.blit(title, (290, 20))
        if play.draw(sc):
            period_game = 'deal'
    if period_game == 'deal':
        play_run()
        if deal.draw(sc):
            period_game = 'choose'



def end():
    global period_game, x, y, \
        dlr, plr, dealer, player, xp, yp, xd, yd, deck, deck2
    pygame.display.update()
    pygame.time.delay(3000)
    x, y = 730, 20
    dlr, plr = 0, 0
    dealer, player = 0, 0
    xp, yp = 400, 290
    xd, yd = 380, 38
    bg.blit(bg2, (0, 0))
    if len(deck) < 1:
        deck, deck2 = deck2, deck


def game():
    global period_game
    if period_game == 'choose':
        deal_run()
        if player < 21:
            if hit.draw(sc):
                pick_card_plr()
            if dealer < 17:
                if stand.draw(sc):
                    pick_card_dlr()
            elif dealer == 21:
                result('Вы проиграли!')
                end()
                deal_run()
            elif dealer > 21:
                result('Вы выиграли!')
                end()
                deal_run()
            elif player == dealer:
                result('Ничья!')
                end()
                deal_run()
            elif player > dealer:
                result('Вы выиграли!')
                end()
                deal_run()
            elif player < dealer:
                result('Вы проиграли!')
                end()
                deal_run()
        elif player == 21:
            result('У Вас 21! Поздравляю!')
            end()
            deal_run()
        elif player > 21:
            result('Вы проиграли!')
            end()
            deal_run()

period_game = 'start'
while True:
    events()
    start()
    game()
    pygame.display.flip()
    clock.tick(fps)
