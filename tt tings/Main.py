import pygame
from tkinter import *
import random as rng

class RPG():

    pygame.font.init()
    pygame.mixer.init()

    def __init__(self):

        self.WIDTH, self.HEIGHT = 1550, 850
        self.windowsize = (self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.set_mode(self.windowsize)
        pygame.display.set_caption("Adventure Bros")
        self.clock = pygame.time.Clock()

        self.backgroundmenu = pygame.image.load('backgroundback.png').convert()
        self.backgroundmenurect = self.backgroundmenu.get_rect()
        self.backgroundmenuposx = 0
        self.backgroundmenuposy = 0

        self.backgroundmenuinfo = pygame.image.load('backgroundback4.png').convert()

        self.mainmenuadventurebros = pygame.image.load('mainlogo.png')
        self.mainmenulogostart = pygame.image.load('startlogo.png')
        self.mainmenulogoinformation = pygame.image.load('informationlogo.png')
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

        self.menumusic = ('Main Menu Theme Song.wav')

        self.playerRightOne = pygame.image.load('playerRightOne.png')
        self.playerRightOne = pygame.transform.scale(self.playerRightOne, (115, 150))
        self.playerRightTwo = pygame.image.load('playerRightTwo.png')
        self.playerRightTwo = pygame.transform.scale(self.playerRightTwo, (115, 150))
        self.playerRightThree = pygame.image.load('playerRightThree.png')
        self.playerRightThree = pygame.transform.scale(self.playerRightThree, (115, 150))

        self.playerLeftOne = pygame.image.load('playerLeftOne.png')
        self.playerLeftOne = pygame.transform.scale(self.playerLeftOne, (115, 150))
        self.playerLeftTwo = pygame.image.load('playerLeftTwo.png')
        self.playerLeftTwo = pygame.transform.scale(self.playerLeftTwo, (115, 150))
        self.playerLeftThree = pygame.image.load('playerLeftThree.png')
        self.playerLeftThree = pygame.transform.scale(self.playerLeftThree, (115, 150))

        self.lasershot = pygame.image.load('lasershot.png')
        self.lasershot = pygame.transform.scale(self.lasershot, (75, 10))
        self.lasershotrect = self.lasershot.get_rect()

        self.badguyalive = True

        self.charRight = []

        for x in range(1000):
            self.charRight.append(self.playerRightOne)
            self.charRight.append(self.playerRightTwo)
            self.charRight.append(self.playerRightThree)

        self.charLeft = []

        for x in range(1000):
            self.charLeft.append(self.playerLeftOne)
            self.charLeft.append(self.playerLeftTwo)
            self.charLeft.append(self.playerLeftThree)

        self.badguyLeftOne = pygame.image.load('bad_guy1.png')
        self.badguyLeftOne = pygame.transform.scale(self.badguyLeftOne, (230, 300))
        self.badguyLeftTwo = pygame.image.load('bad_guy2.png')
        self.badguyLeftTwo = pygame.transform.scale(self.badguyLeftTwo, (230, 300))
        self.badguyLeftThree = pygame.image.load('bad_guy4.png')
        self.badguyLeftThree = pygame.transform.scale(self.badguyLeftThree, (230, 300))

        self.badcharLeft = []

        for x in range(10000):
            self.badcharLeft.append(self.badguyLeftOne)
            self.badcharLeft.append(self.badguyLeftTwo)
            self.badcharLeft.append(self.badguyLeftThree)

        self.x, self.y = 128, 600
        self.badguyx, self.badguyy = 3100, 450

        self.healthplayer = 150
        self.healthenemy = 150

        self.npcAlex = pygame.image.load('NPC1.png')
        self.npcAlex = pygame.transform.scale(self.npcAlex, (345, 450))

        self.badguyInfo = pygame.image.load('bad_guy6.png')
        self.badguyInfo = pygame.transform.scale(self.badguyInfo, (345, 450))

        self.charStand = pygame.image.load('playerStand.png')
        self.booleanJumping = False
        self.moveLeft = False
        self.moveRight = False

        self.jumpingCount = 9
        self.velocity = 4
        self.walkingCount = 0
        self.enemywalkingCount = 0

        self.npc1x, self.npc1y = 1600, 370
        self.lasershots = self.screen.blit(self.lasershot, (11110, 11110))

        self.npcChat1 = self.myfont.render("Please Help! My village is under attack by vicious Mingo's!", True, (0, 0, 0))
        self.npcChat1x = 1400

        self.chatInfo1 = self.myfont.render("Use A to move Left & D to move Right!", True, (0, 0, 0))
        self.chatInfo2 = self.myfont.render("Use SPACE to jump & Left-CLick to shoot!", True, (0, 0, 0))
        self.chatInfo3 = self.myfont.render("Help the villagers from the ravage Mingo's!", True, (0, 0, 0))
        self.chatInfo4 = self.myfont.render("Mingo: Bad Guy! Run! Shoot! Hide!", True, (0, 0, 0))

    def grabinformation(self):

        self.window = Tk()
        self.window.title('Adventure Bros')
        self.window.geometry('500x500')

        self.photobackground = PhotoImage(file='backgroundback.png')

        self.background = Label(self.window, image=self.photobackground)
        self.background.place(x=-400, y=-400)

        self.lbl1 = Label(self.window, text='Name', borderwidth=0, font=('Helvetica', 18, 'bold'))
        self.lbl1.place(x=210, y=145)

        self.nameget = Entry(self.window)
        self.nameget.focus_set()
        self.nameget.place(x=185, y=200)

        self.lbl2 = Label(self.window, text='Username', borderwidth=0, font=('Helvetica', 18, 'bold'))
        self.lbl2.place(x=186, y=295)

        self.usernameget = Entry(self.window)
        self.usernameget.focus_set()
        self.usernameget.place(x=185, y=350)

        self.btn1 = Button(self.window, text='Accept', borderwidth=0, font=('Helvetica', 18, 'bold'), command=self.mainmenu)
        self.btn1.place(x=195, y=450)

        mainloop()

    def mainmenu(self):

        self.window.destroy()
        pygame.mixer.music.load(self.menumusic)
        pygame.mixer.music.play(-1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            self.screen.blit(self.backgroundmenu, (0, 0))
            self.screen.blit(self.mainmenuadventurebros, (255, 300))
            self.screen.blit(self.mainmenulogostart, (675, 500))
            self.screen.blit(self.mainmenulogoinformation, (590, 600))

            self.mousex = pygame.mouse.get_pos()[0]
            self.mousey = pygame.mouse.get_pos()[1]

            self.mouseclick = pygame.mouse.get_pressed()[0]

            if self.mousex >= 684 and self.mousex <= 821:

                if self.mousey >= 507 and self.mousey <= 554:

                    if self.mouseclick == 1:

                        self.maingamescreen()

            if self.mousex >= 600 and self.mousex <= 930:

                if self.mousey >= 625 and self.mousey <= 655:

                    if self.mouseclick == 1:

                        self.maininfoscreen()

            pygame.display.flip()
            self.clock.tick(60)

    def maininfoscreen(self):

        self.screen.blit(self.backgroundmenu, (0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            self.screen.blit(self.badguyInfo, (700, 350))
            self.screen.blit(self.chatInfo1, (500, 200))
            self.screen.blit(self.chatInfo2, (500, 300))
            self.screen.blit(self.chatInfo3, (500, 100))
            self.screen.blit(self.chatInfo4, (300, 550))
            self.screen.blit(self.mainmenulogostart, (700, 760))

            self.mousex = pygame.mouse.get_pos()[0]
            self.mousey = pygame.mouse.get_pos()[1]

            self.mouseclick = pygame.mouse.get_pressed()[0]

            if self.mousex >= 705 and self.mousex <= 848:

                if self.mousey >= 765 and self.mousey <= 815:

                    if self.mouseclick == 1:

                        self.maingamescreen()

                        self.mouseclick = 0

            pygame.display.flip()
            self.clock.tick(60)

    def maingamescreen(self):

        self.bulletstate = 0
        self.bulletx = self.x
        self.bulletxvel = 8

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            self.keys = pygame.key.get_pressed()

            if self.keys[pygame.K_a]:

                self.x -= self.velocity
                self.backgroundmenuposx += self.velocity
                self.moveLeft = True
                self.moveRight = False
                self.npc1x += self.velocity
                self.npcChat1x += self.velocity
                self.badguyx = self.badguyx - 3
                self.enemywalkingCount += 1
                self.bulletxvel = 8

            elif self.keys[pygame.K_d]:

                self.x += self.velocity
                self.backgroundmenuposx -= self.velocity
                self.moveLeft = False
                self.moveRight = True
                self.npc1x -= self.velocity
                self.npcChat1x -= self.velocity
                self.badguyx = self.badguyx - 3
                self.enemywalkingCount += 1
                self.bulletxvel = 8

            else:

                self.moveLeft = False
                self.moveRight = True
                self.walkingCount = 0
                self.badguyx = self.badguyx - 3
                self.enemywalkingCount += 1

            if not self.booleanJumping:

                if self.keys[pygame.K_SPACE]:

                    self.booleanJumping = True
                    self.moveLeft = False
                    self.moveRight = False
                    self.walkingCount = 0
            else:

                if self.jumpingCount >= -9:

                    self.y -= (self.jumpingCount * abs(self.jumpingCount)) * 0.2
                    self.jumpingCount -= 1
                else:

                    self.jumpingCount = 9
                    self.booleanJumping = False

            self.redrawGameWindow()

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)

    def redrawGameWindow(self):

        pygame.init()

        self.lasershotrect = self.lasershot.get_rect()
        self.badcharrect = self.badcharLeft[self.enemywalkingCount // 3].get_rect()
        self.playerrect = self.charLeft[self.walkingCount // 3].get_rect()
        #self.playerrect.topleft = self.x
        #self.lasershotrect.topleft = self.bulletx
        #self.badcharrect.topleft = self.x

        self.screen.blit(self.backgroundmenu, (self.backgroundmenuposx, self.backgroundmenuposy))
        self.rightBackgroundMultiply = 1
        self.leftBackgroundMultiply = -1

        self.mousex = pygame.mouse.get_pos()[0]
        self.mousey = pygame.mouse.get_pos()[1]

        self.mouseclick = pygame.mouse.get_pressed()[0]

        for x in range(10):
            self.screen.blit(self.backgroundmenu, (self.backgroundmenuposx + (1600 * self.rightBackgroundMultiply), self.backgroundmenuposy))
            self.rightBackgroundMultiply = self.rightBackgroundMultiply + 1

        for x in range(10):
            self.screen.blit(self.backgroundmenu, (self.backgroundmenuposx + (1600 * self.leftBackgroundMultiply), self.backgroundmenuposy))
            self.leftBackgroundMultiply = self.leftBackgroundMultiply - 1

        pygame.draw.rect(self.screen, (0, 0, 0), [(self.x - 35), (self.y - 35), 160, 25], 0)
        pygame.draw.rect(self.screen, (255, 0, 0), [(self.x - 30), (self.y - 30), 150, 15], 0)
        pygame.draw.rect(self.screen, (0, 255, 0), [(self.x - 30), (self.y - 30), self.healthplayer, 15], 0)

        if self.backgroundmenuposx <= -400:
            self.screen.blit(self.npcChat1, (self.npcChat1x, 400))

        if self.walkingCount + 1 >= 27:
            self.walkingCount = 0

        if self.moveRight:
            self.screen.blit(self.npcAlex, (self.npc1x, self.npc1y))
            self.screen.blit(self.charRight[self.walkingCount // 3], (self.x, self.y))

            self.walkingCount += 1

        elif self.moveLeft:
            self.screen.blit(self.npcAlex, (self.npc1x, self.npc1y))
            self.screen.blit(self.charLeft[self.walkingCount // 3], (self.x, self.y))

            self.walkingCount += 1

        if self.backgroundmenuposx <= -10:

            if self.badguyalive:
                self.enemy = self.screen.blit(self.badcharLeft[self.enemywalkingCount // 3], (self.badguyx, self.badguyy))

                pygame.draw.rect(self.screen, (0, 0, 0), [(self.badguyx + 35), (self.badguyy + 50), 160, 25], 0)
                pygame.draw.rect(self.screen, (255, 0, 0), [(self.badguyx + 40), (self.badguyy + 55), 150, 15], 0)
                pygame.draw.rect(self.screen, (0, 255, 0), [(self.badguyx + 40), (self.badguyy + 55), self.healthenemy, 15], 0)

        if self.x <= 124:
            self.x += self.velocity

        if self.x >= 700:
            self.x -= self.velocity

        self.mouseclick = pygame.mouse.get_pressed()[0]

        if self.keys[pygame.K_c]:
            self.bullety = self.y
            self.shootbullet(self.bulletx, self.bullety)

        if self.bulletstate is 1:
            self.shootbullet(self.bulletx, self.bullety)
            self.bulletx += self.bulletxvel

        if self.bulletx >= 1500:
            self.bulletstate = 0
            self.bulletx = self.x

        if self.bulletstate == 0:
            self.bulletx = self.x

        self.runcollisions()

        pygame.display.update()

    def shootbullet(self, x, y):
        self.bulletstate = 1
        self.lasershots = self.screen.blit(self.lasershot, (x + 32, y + 45))

    def runcollisions(self):

        #if pygame.Rect.colliderect(self.badcharrect, self.lasershotrect):

            #self.healthenemy = self.healthenemy =+ 25

        #if self.healthenemy == 0:
            #self.enemy.kill()

        #if pygame.Rect.colliderect(self.badcharrect, self.playerrect):

            #self.healthplayer = self.healthplayer =- 25

        #if self.healthplayer == 0:
            #self.playerrect.kill()

        if self.badguyalive:
            if self.bulletx >= self.badguyx:
                self.healthenemy = self.healthenemy - 25
                self.bulletstate = 0

        if self.healthenemy <= 0:
            self.badguyalive = False

        if self.badguyalive:
            if self.x >= self.badguyx:
                self.badguyalive = False
                self.healthplayer = self.healthplayer - 75


def main():
    mw = RPG()
    mw.grabinformation()


if __name__ == "__main__":
    main()
