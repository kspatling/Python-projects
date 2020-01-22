# Kevin Spatling
# Here I imported the assets for my game.
import pygame
from tkinter import *
import random as rng


# Here I created my class where all my game code will be stored.
class RPG():
    # I initialze the pygame functions I will use.
    pygame.font.init()
    pygame.mixer.init()

    # I predefine my static variables that load before anything else loads up in the program.
    def __init__(self):

        # Here I define the width and height of the window.
        self.WIDTH, self.HEIGHT = 1550, 850
        self.windowsize = (self.WIDTH, self.HEIGHT)

        # I then create a pygame screen using these variables.
        self.screen = pygame.display.set_mode(self.windowsize)

        # I title the window.
        pygame.display.set_caption("Adventure Bros")

        # I define the frame refresh rate.
        self.clock = pygame.time.Clock()

        # Here I import my background menu and convert it to a jpg.
        self.backgroundmenu = pygame.image.load('backgroundback.png').convert()

        # I define the x and y coords of the background.
        self.backgroundmenuposx = 0
        self.backgroundmenuposy = 0

        # Here I import the background menu for the info screen.
        self.backgroundmenuinfo = pygame.image.load('backgroundback4.png').convert()

        # Here I import the main menu button images.
        self.mainmenuadventurebros = pygame.image.load('mainlogo.png')
        self.mainmenulogostart = pygame.image.load('startlogo.png')
        self.mainmenulogoinformation = pygame.image.load('informationlogo.png')

        # Here I defined what font I will use for my text.
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

        # I import the music for my file.
        self.menumusic = ('Main Menu Theme Song.wav')

        # I import all frames of my player I will use to make him look like hes moving, and I scale the images to be smaller. This is for right movement.
        self.playerRightOne = pygame.image.load('playerRightOne.png')
        self.playerRightOne = pygame.transform.scale(self.playerRightOne, (115, 150))
        self.playerRightTwo = pygame.image.load('playerRightTwo.png')
        self.playerRightTwo = pygame.transform.scale(self.playerRightTwo, (115, 150))
        self.playerRightThree = pygame.image.load('playerRightThree.png')
        self.playerRightThree = pygame.transform.scale(self.playerRightThree, (115, 150))

        # I import all frames of my player I will use to make him look like hes moving, and I scale the images to be smaller. This is for left movement.
        self.playerLeftOne = pygame.image.load('playerLeftOne.png')
        self.playerLeftOne = pygame.transform.scale(self.playerLeftOne, (115, 150))
        self.playerLeftTwo = pygame.image.load('playerLeftTwo.png')
        self.playerLeftTwo = pygame.transform.scale(self.playerLeftTwo, (115, 150))
        self.playerLeftThree = pygame.image.load('playerLeftThree.png')
        self.playerLeftThree = pygame.transform.scale(self.playerLeftThree, (115, 150))

        # Here I import the last shot and grab the laser's x and y coordinates
        self.lasershot = pygame.image.load('lasershot.png')
        self.lasershot = pygame.transform.scale(self.lasershot, (75, 10))
        self.lasershotrect = self.lasershot.get_rect()

        # Here I define if the bad guy is still alive.
        self.badguyalive = True

        # Here I create the character right movement.
        self.charRight = []

        # Here I append constantly the images of my player so that when they move it will constantly go through their movement.
        for x in range(1000):
            self.charRight.append(self.playerRightOne)
            self.charRight.append(self.playerRightTwo)
            self.charRight.append(self.playerRightThree)

        # Here I create the character left movement.
        self.charLeft = []

        # Here I append constantly the images of my player so that when they move it will constantly go through their movement.
        for x in range(1000):
            self.charLeft.append(self.playerLeftOne)
            self.charLeft.append(self.playerLeftTwo)
            self.charLeft.append(self.playerLeftThree)

        # I import all frames of my bad guy I will use to make him look like hes moving, and I scale the images to be smaller. This is for left movement. The badguy can only move left.
        self.badguyLeftOne = pygame.image.load('bad_guy1.png')
        self.badguyLeftOne = pygame.transform.scale(self.badguyLeftOne, (230, 300))
        self.badguyLeftTwo = pygame.image.load('bad_guy2.png')
        self.badguyLeftTwo = pygame.transform.scale(self.badguyLeftTwo, (230, 300))
        self.badguyLeftThree = pygame.image.load('bad_guy4.png')
        self.badguyLeftThree = pygame.transform.scale(self.badguyLeftThree, (230, 300))

        # Here is where I will store all his movement pictures.
        self.badcharLeft = []

        # Here I append constantly the images of my badguy so that when they move it will constantly go through their movement.
        for x in range(10000):
            self.badcharLeft.append(self.badguyLeftOne)
            self.badcharLeft.append(self.badguyLeftTwo)
            self.badcharLeft.append(self.badguyLeftThree)

        # Here I create my player's x and y variables and my bad guy's x and y variables
        self.x, self.y = 128, 600
        self.badguyx, self.badguyy = 3100, 450

        # The player's enemy and health.
        self.healthplayer = 150
        self.healthenemy = 150
        self.damage = 0

        # Here I created the NPC's image.
        self.npcAlex = pygame.image.load('NPC1.png')
        self.npcAlex = pygame.transform.scale(self.npcAlex, (345, 450))

        # Here I created the bad guys image for the info screen.
        self.badguyInfo = pygame.image.load('bad_guy6.png')
        self.badguyInfo = pygame.transform.scale(self.badguyInfo, (345, 450))

        # Here I created the bosses image.
        self.badguyBoss = pygame.image.load('bad_guy6.png')
        self.badguyBoss = pygame.transform.scale(self.badguyInfo, (300, 390))

        # Here I defined the player's non constant movement.
        self.charStand = pygame.image.load('playerStand.png')
        self.charStand = pygame.transform.scale(self.charStand, (115, 150))

        # Booleans for when the player is jumping or moving left and right.
        self.booleanJumping = False
        self.moveLeft = False
        self.moveRight = False
        self.standingstill = True

        # Here I define my variables for the movement system to look through the list and display the images to make it look like the characters are moving on the screen.
        self.jumpingCount = 9
        self.velocity = 4
        self.walkingCount = 0
        self.enemywalkingCount = 0

        # Here I created the npc on the screen.
        self.npc1x, self.npc1y = 1600, 370

        # Here i created the laser on the screen to be predeifned off the screen.
        self.lasershots = self.screen.blit(self.lasershot, (11110, 11110))

        # This creates a text variable, and displays it as True to display text when put on a screen, and then I choose the text color.
        self.npcChat1 = self.myfont.render("Please Help! My village is under attack by vicious Mingo's!", True, (0, 0, 0))

        # This is the x coords of the npc's text box
        self.npcChat1x = 1400

        # This is the other chat boxes and I store them in these variables so later I can draw them onto the screen.
        self.chatInfo1 = self.myfont.render("Use A to move Left & D to move Right!", True, (0, 0, 0))
        self.chatInfo2 = self.myfont.render("Use SPACE to jump & Left-CLick to shoot!", True, (0, 0, 0))
        self.chatInfo3 = self.myfont.render("Help the villagers from the ravage Mingo's!", True, (0, 0, 0))
        self.chatInfo4 = self.myfont.render("Mingo: Bad Guy! Run! Shoot! Hide!", True, (0, 0, 0))

    # Here I create a function to open my pre-game info screen with tkinter.
    def grabinformation(self):

        # Here I initilaze the tkinter window method.
        self.window = Tk()

        # I name the window.
        self.window.title('Adventure Bros')

        # I set the window's width and height.
        self.window.geometry('500x500')

        # Here I import the file I will use for my background for the window.
        self.photobackground = PhotoImage(file='backgroundback.png')


        # I take that background file and I create an empty label while placing it off the screen.
        # This will give the effect that I had placed an image there.
        self.background = Label(self.window, image=self.photobackground)
        self.background.place(x=-400, y=-400)

        # I create a label for "Name". I choose it's borderwidth around the text, and the font of the text.
        self.lbl1 = Label(self.window, text='Name', borderwidth=0, font=('Helvetica', 18, 'bold'))
        self.lbl1.place(x=210, y=145)

        # I create an entry box for the name, I focus it on the screen to avoid going over length of the textbox.
        self.nameget = Entry(self.window)
        self.nameget.focus_set()
        self.nameget.place(x=185, y=200)

        # I create a label for "Username". I choose it's borderwidth around the text, and the font I use of the text.
        self.lbl2 = Label(self.window, text='Username', borderwidth=0, font=('Helvetica', 18, 'bold'))
        self.lbl2.place(x=186, y=295)

        # I create an entry box for the username, I focus it on the screen to avoid going over length of the textbox.
        self.usernameget = Entry(self.window)
        self.usernameget.focus_set()
        self.usernameget.place(x=185, y=350)

        # This button once clicked will run the command to open my main menu screen.
        self.btn1 = Button(self.window, text='Accept', borderwidth=0, font=('Helvetica', 18, 'bold'), command=self.mainmenu)
        self.btn1.place(x=195, y=450)

        mainloop()

    def mainmenu(self):

        # This destroys the main window once they click the button.
        #self.window.destroy()

        # I load my game music I predifined earlier.
        pygame.mixer.music.load(self.menumusic)

        # This plays the music for an infinite loop.
        pygame.mixer.music.play(-1)

        # This defines the game in a loop so the game will always constantly be running, but if pygame detects that the
        # event of "quit" or clicking off the game, it will then run the command to close the game window.
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # This takes my background, logo, start button, and information button and draws them onto the screen at the given x & y coords.
            self.screen.blit(self.backgroundmenu, (0, 0))
            self.screen.blit(self.mainmenuadventurebros, (255, 300))
            self.screen.blit(self.mainmenulogostart, (675, 500))
            self.screen.blit(self.mainmenulogoinformation, (590, 600))

            # I use pygame.mouse.get_pos() to grab a list of the mouse's x and y coords. I then search through this list
            # With [0] & [1] to grab their x and y coords.
            self.mousex = pygame.mouse.get_pos()[0]
            self.mousey = pygame.mouse.get_pos()[1]

            # I do the same thing as above except I sift through to grab the left click function.
            self.mouseclick = pygame.mouse.get_pressed()[0]

            # I detect if the mouse x coords are within my buttons parameters.
            if self.mousex >= 684 and self.mousex <= 821:

                # I then detect if the mouse y coords are within my buttons parameters.
                if self.mousey >= 507 and self.mousey <= 554:

                    # If both are true then it will search for if the user will left click.
                    if self.mouseclick == 1:

                        # If the user left click's then they will be presented with the main game screen.
                        self.maingamescreen()

            # I detect if the mouse x coords are within my buttons parameters.
            if self.mousex >= 600 and self.mousex <= 930:

                # I then detect if the mouse y coords are within my buttons parameters.
                if self.mousey >= 625 and self.mousey <= 655:

                    # If both are true then it will search for if the user will left click.
                    if self.mouseclick == 1:

                        # If the user left click's then they will be presented with the information screen.
                        self.maininfoscreen()

            # I refresh the screen.
            pygame.display.flip()

            # I update the refresh rate at which the window will update at, to make sure it does not change.
            self.clock.tick(60)

# Here I create my main information screen.
    def maininfoscreen(self):

        # I draw the background of the screen.
        self.screen.blit(self.backgroundmenu, (0, 0))

        # This defines the game in a loop so the game will always constantly be running, but if pygame detects that the
        # event of "quit" or clicking off the game, it will then run the command to close the game window.
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # This takes my bad guy, and text box's and draws them onto the screen at the given x & y coords.
            self.screen.blit(self.badguyInfo, (700, 350))
            self.screen.blit(self.chatInfo1, (500, 200))
            self.screen.blit(self.chatInfo2, (500, 300))
            self.screen.blit(self.chatInfo3, (500, 100))
            self.screen.blit(self.chatInfo4, (300, 550))
            self.screen.blit(self.mainmenulogostart, (700, 760))

            # I use pygame.mouse.get_pos() to grab a list of the mouse's x and y coords. I then search through this list
            # With [0] & [1] to grab their x and y coords.
            self.mousex = pygame.mouse.get_pos()[0]
            self.mousey = pygame.mouse.get_pos()[1]

            # I do the same thing as above except I sift through to grab the left click function.
            self.mouseclick = pygame.mouse.get_pressed()[0]

            # I detect if the mouse x coords are within my buttons parameters.
            if self.mousex >= 705 and self.mousex <= 848:

                # I then detect if the mouse y coords are within my buttons parameters.
                if self.mousey >= 765 and self.mousey <= 815:

                    # If both are true then it will search for if the user will left click.
                    if self.mouseclick == 1:

                        # If the user left click's then they will be presented with the main game screen.
                        self.maingamescreen()

                        # I then reset the left click variable to 0 again, instead of being stuck at 1.
                        self.mouseclick = 0

            # I refresh the screen.
            pygame.display.flip()

            # I update the refresh rate at which the window will update at, to make sure it does not change.
            self.clock.tick(60)

    # I create a new function for my main game screen.
    def maingamescreen(self):

        # I define my variables for the bulletstate (if it is firing or not) and the bullet x coordinates, and the velocity.
        self.bulletstate = 0
        self.bulletx = self.x
        self.bulletxvel = 8

        # I define if the boss battle is commencing or not in a boolean. I then set its x coords.
        self.bossbattle = False
        self.bossx = 350

        # I set the jump variable for the player.
        self.jumpmultiply = 0.2

        # This defines the game in a loop so the game will always constantly be running, but if pygame detects that the
        # event of "quit" or clicking off the game, it will then run the command to close the game window.
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # I initialze the pygame to search for key presses.
            self.keys = pygame.key.get_pressed()

            # If the player clicks the key A.
            if self.keys[pygame.K_a]:

                # I change the player position.
                self.x -= self.velocity

                # I define that the player is moving left and NOT right.
                self.moveLeft = True
                self.moveRight = False
                self.standingstill = False

                # I change the NPC's coordinates to scroll with the screen.
                self.npc1x += self.velocity
                self.npcChat1x += self.velocity

                # I change the bad guy's x coordinate, to continue walking.
                self.badguyx = self.badguyx - 3

                # I add the enemy walking count so it appears as if he was walking.
                self.enemywalkingCount += 1

                # I then change the bullet's moving velocity for that direction.
                self.bulletxvel = 8

                # I check if the player is in the boss battle. If he is not then the window will keep scrolling.
                if self.bossbattle == False:
                    self.backgroundmenuposx += self.velocity

            # If the player clicks the key D.
            elif self.keys[pygame.K_d]:

                # I change the player position.
                self.x += self.velocity

                # I define that the player is moving right and NOT left.
                self.moveLeft = False
                self.standingstill = False
                self.moveRight = True

                # I change the NPC's coordinates to scroll with the screen.
                self.npc1x -= self.velocity
                self.npcChat1x -= self.velocity

                # I change the bad guy's x coordinate, to continue walking.
                self.badguyx = self.badguyx - 3

                # I add the enemy walking count so it appears as if he was walking.
                self.enemywalkingCount += 1

                # I then change the bullet's moving velocity for that direction.
                self.bulletxvel = 8

                # I check if the player is in the boss battle. If he is not then the window will keep scrolling.
                if self.bossbattle == False:
                    self.backgroundmenuposx -= self.velocity

            # If the player is not moving left or right.
            else:

                # Change the left and right movement to be false.
                self.moveLeft = False
                self.moveRight = False
                
                # Tell the code for him to be standing still.
                self.standingstill = True
                
                # Set the walking count to 0 so it does not show him still walking.
                self.walkingCount = 0
                
                # Continue updating the bad guy's x coord to keep walking.
                self.badguyx = self.badguyx - 3
                
                # I make the enemy walk.
                self.enemywalkingCount += 1

            # I first check if the player is not jumping so he cannot double jump and fly away.
            if not self.booleanJumping:

                # I then check if the user clicks the space bar.
                if self.keys[pygame.K_SPACE]:
                    
                    # If he does then it will change the boolean for jumping to true, and make sure he isn't walking
                    # mid air by change the move left and move right to false. Also setting the walking count to 0.
                    self.booleanJumping = True
                    self.moveLeft = False
                    self.moveRight = False
                    self.walkingCount = 0
            
            # If the player is jumping.
            else:

                # If there jump count is greater than the curve of -9.
                if self.jumpingCount >= -9:

                    # It will multiply the jumping count by my jump multiplier so that he makes a curve.
                    # The jump count goes -1 each time so the player will continue on a curvature motion.
                    self.y -= (self.jumpingCount * abs(self.jumpingCount)) * self.jumpmultiply
                    self.jumpingCount -= 1
                    
                # When the jumping count is now greater then -9.
                else:

                    # I will set the jumping count back to 9, and change it so they are not jumping anymore.
                    self.jumpingCount = 9
                    self.booleanJumping = False

            # This runs my main backend function for the user, bad guy, scrolling background and bullets.
            self.redrawGameWindow()

            # I refresh the game window, and I update the refresh rate so I do not get any screen tearing or lagging.
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)

    def redrawGameWindow(self):

        pygame.init()

        self.lasershotrect = self.lasershot.get_rect()
        self.badcharrect = self.badcharLeft[self.enemywalkingCount // 3].get_rect()
        self.playerrect = self.charLeft[self.walkingCount // 3].get_rect()

        self.screen.blit(self.backgroundmenu, (self.backgroundmenuposx, self.backgroundmenuposy))
        self.rightBackgroundMultiply = 1
        self.leftBackgroundMultiply = -1

        self.mousex = pygame.mouse.get_pos()[0]
        self.mousey = pygame.mouse.get_pos()[1]

        self.mouseclick = pygame.mouse.get_pressed()[0]

        for x in range(10):
            self.screen.blit(self.backgroundmenu,
                             (self.backgroundmenuposx + (1600 * self.rightBackgroundMultiply), self.backgroundmenuposy))
            self.rightBackgroundMultiply = self.rightBackgroundMultiply + 1

        for x in range(10):
            self.screen.blit(self.backgroundmenu,
                             (self.backgroundmenuposx + (1600 * self.leftBackgroundMultiply), self.backgroundmenuposy))
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

        elif self.standingstill:

            self.screen.blit(self.npcAlex, (self.npc1x, self.npc1y))
            self.screen.blit(self.charStand, (self.x, self.y))


            self.walkingCount += 1

        if self.backgroundmenuposx <= -10:

            if self.badguyalive:
                self.enemy = self.screen.blit(self.badcharLeft[self.enemywalkingCount // 3],
                                              (self.badguyx, self.badguyy))

                pygame.draw.rect(self.screen, (0, 0, 0), [(self.badguyx + 35), (self.badguyy + 50), 160, 25], 0)
                pygame.draw.rect(self.screen, (255, 0, 0), [(self.badguyx + 40), (self.badguyy + 55), 150, 15], 0)
                pygame.draw.rect(self.screen, (0, 255, 0),
                                 [(self.badguyx + 40), (self.badguyy + 55), self.healthenemy, 15], 0)

        if self.bossbattle == False:

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

        if self.backgroundmenuposx <= -3200:
            self.bossbattle = True

        if self.bossbattle:

            self.velocity = 5
            self.jumpmultiply = 1.4

            if self.x <= 175:
                self.x += self.velocity

            if self.x >= 1300:
                self.x -= self.velocity

            self.screen.blit(self.badguyInfo, (self.bossx, 375))

        self.runcollisions()
        print(self.healthplayer)

        pygame.display.update()

    def shootbullet(self, x, y):
        self.bulletstate = 1
        self.lasershots = self.screen.blit(self.lasershot, (x + 32, y + 45))

    def runcollisions(self):

        if pygame.Rect.colliderect(self.badcharrect, self.lasershotrect):
            self.healthenemy = self.healthenemy - 0

        if self.healthenemy == 0:
            self.badguyalive = False

        if pygame.Rect.colliderect(self.badcharrect, self.playerrect):
            self.healthplayer = self.healthplayer - 0

        if self.healthplayer == 0:
            pass

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

# Defines my main class. Then looks through the class to find my main window of that class.
def main():
    mw = RPG()
    mw.mainmenu()

# Open the project file and call the main program class.
if __name__ == "__main__":
    main()
