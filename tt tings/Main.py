import pygame
from tkinter import *

class RPG():

    pygame.init()
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
        self.backgroundmenuleft = 0
        self.backgroundmenuright = 0
        self.mainmenuadventurebros = pygame.image.load('mainlogo.png')
        self.mainmenulogostart = pygame.image.load('startlogo.png')
        self.mainmenulogoinformation = pygame.image.load('informationlogo.png')

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

        self.charRight = [self.playerRightOne, self.playerRightTwo,
                          self.playerRightThree, self.playerRightTwo,
                          self.playerRightOne, self.playerRightTwo,
                          self.playerRightThree, self.playerRightTwo,
                          self.playerRightOne, self.playerRightTwo,
                          self.playerRightThree, self.playerRightTwo,
                          self.playerRightOne, self.playerRightTwo,
                          self.playerRightThree, self.playerRightTwo]

        self.charLeft = [self.playerLeftOne, self.playerLeftTwo,
                          self.playerLeftThree, self.playerLeftTwo,
                          self.playerLeftOne, self.playerLeftTwo,
                          self.playerLeftThree, self.playerLeftTwo,
                          self.playerLeftOne, self.playerLeftTwo,
                          self.playerLeftThree, self.playerLeftTwo,
                          self.playerLeftOne, self.playerLeftTwo,
                          self.playerLeftThree, self.playerLeftTwo]

        self.charStand = pygame.image.load('playerStand.png')
        self.booleanJumping = False
        self.moveLeft = False
        self.moveRight = False

        self.jumpingCount = 9
        self.velocity = 4
        self.walkingCount = 0

        self.x, self.y = 20, 600

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

            pygame.display.flip()
            self.clock.tick(60)

    def maingamescreen(self):

        pygame.mixer.music.load(self.menumusic)
        pygame.mixer.music.play(-1)

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

            elif self.keys[pygame.K_d]:

                self.x += self.velocity
                self.backgroundmenuposx -= self.velocity
                self.moveLeft = False
                self.moveRight = True

            else:

                self.moveLeft = False
                self.moveRight = True
                self.walkingCount = 0

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

            pygame.display.flip()
            self.clock.tick(60)

    def redrawGameWindow(self):

        self.screen.blit(self.backgroundmenu, (self.backgroundmenuposx, self.backgroundmenuposy))
        self.changerate1 = 0

        if self.backgroundmenuposx > 0:

            self.screen.blit(self.backgroundmenu, (1600 - self.backgroundmenurect[2], self.backgroundmenuposy))

        print(self.backgroundmenuposx)


        if self.walkingCount + 1 >= 27:
            self.walkingCount = 0

        if self.moveRight:
            self.screen.blit(self.charRight[self.walkingCount // 3], (self.x, self.y))
            self.walkingCount += 1

        elif self.moveLeft:
            self.screen.blit(self.charLeft[self.walkingCount // 3], (self.x, self.y))
            self.walkingCount += 1

        if self.x <= 123:
            self.x += self.velocity

        if self.x >= 1300:
            self.x -= self.velocity

        pygame.display.update()


def main():
    mw = RPG()
    mw.grabinformation()


if __name__ == "__main__":
    main()
