#################################################################
# Adding music
# Importing a sound -> sound.play()
#################################################################
import pygame, sys, random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_walk = [pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha(), 
                            pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[0]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0
        self.player_jumping = False

        #adding a sound jump using pygame.mixer.Sound(file) function
        self.jump_sound = pygame.mixer.Sound('audio\jump.mp3')
        self.jump_sound.set_volume(0.3)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -18
            self.player_jumping = True
            self.jump_sound.play()

    def apply_gravity(self):
        self.rect.y += self.gravity
        if self.rect.bottom > 300: 
            self.gravity = 0
            self.rect.bottom = 300
            self.player_jumping = False
        else:
            self.gravity += 1

    def animation_state(self):
        if self.player_jumping:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index > len(self.player_walk): 
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
        
class Obsatacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            self.frames = [pygame.image.load('graphics/Fly/Fly1.png').convert_alpha(),
                           pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()]
            y_pos = 300 - player_rect.height - 10
        else:
            self.frames = [pygame.image.load('graphics/snail/snail1.png').convert_alpha(), 
                           pygame.image.load('graphics/snail/snail2.png').convert_alpha()]
            y_pos = 300
        self.obstacle_index = 0
        self.image = self.frames[self.obstacle_index]
        self.rect = self.image.get_rect(bottomright = (random.randint(900, 1100), y_pos))
    
    def animation_state(self):
        self.obstacle_index += 0.1
        if self.obstacle_index >= len(self.frames):
            self.obstacle_index = 0
        self.image = self.frames[int(self.obstacle_index)]

    def update(self):
        self.animation_state()
        self.destroy()
        self.rect.x -= 6

    def destroy(self):
        if self.rect.x < -100:
            self.kill()
 
def sprite_collide():
    has_collided = pygame.sprite.spritecollide(character.sprite, obstacle_group, False)
    if has_collided:
        obstacle_group.empty()
    return not has_collided

pygame.init()
bg_music = pygame.mixer.Sound('audio\music.wav')
bg_music.set_volume(0.4)
bg_music.play(loops = -1)

pygame.display.set_caption('Game Title')
screen = pygame.display.set_mode((800, 400)) 
clock = pygame.time.Clock()

game_active = False

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

font = pygame.font.Font('font/Pixeltype.ttf', 50)

score = 0
start_time = 0

character = pygame.sprite.GroupSingle()
character.add(Player())

obstacle_group = pygame.sprite.Group()

score_surface = font.render("score: " + str(score), False, (64, 64, 64))
score_rect = pygame.Rect(400 - (score_surface.get_width()/2), 10, 
                         score_surface.get_width() + 20, score_surface.get_height())

snail_frames = [pygame.image.load('graphics/snail/snail1.png').convert_alpha(), 
         pygame.image.load('graphics/snail/snail2.png').convert_alpha()]
snail_index = 0
snail = snail_frames[0]

fly_frames = [pygame.image.load('graphics/Fly/Fly1.png').convert_alpha(),
         pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()]
fly_index = 0
fly = fly_frames[0]

obstacles = []

player_walk = [pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha(), 
               pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()]
player_index = 0
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

player = player_walk[0]
player_rect = player.get_rect(midbottom = (80,300))
player_gravity = 0
player_jumping = False

stand_player = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
stand_player = pygame.transform.rotozoom(stand_player, 0, 1.5)

stand_player_rect = stand_player.get_rect(center = (400, 200))

intro_text = font.render("Snail Hopper", False, 'black')
intro_text_rect = intro_text.get_rect(center = (400, 50))

instruction_text = font.render("Press any button to start", False, 'black')
instruction_text_rect = instruction_text.get_rect(center = (410, 350))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 200)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not player_jumping:
                    player_gravity = -18
                    player_jumping = True
        else:
            if event.type == pygame.KEYDOWN:
                game_active = True

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obsatacle(random.choice(['fly', 'snail', 'snail', 'snail'])))
            
            if event.type == snail_animation_timer:
                snail = snail_frames[snail_index]
                if snail_index:
                    snail_index = 0
                else: 
                    snail_index = 1

            if event.type == fly_animation_timer:
                fly = fly_frames[fly_index]
                if fly_index:
                    fly_index = 0
                else: 
                    fly_index = 1

    if game_active:
        screen.fill('black')
        
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        
        pygame.draw.rect(screen, '#c0e8ec' , score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)

        curr_time = pygame.time.get_ticks() - start_time
        score = int(curr_time / 1000)

        score_surface = font.render("score: " + str(score), False, (64, 64, 64))
        screen.blit(score_surface, (score_rect.x + 10, score_rect.y + 4))
        
        character.draw(screen)
        character.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = sprite_collide()
    else:
        screen.fill((94, 129, 162))
        
        score_text = font.render(f'score: {score}', False, 'black')
        score_text_rect = score_text.get_rect(center = (400, 340))

        game_over_text = font.render('Game Over', False, 'black')
        game_over_text_rect = score_text.get_rect(center = (390, 50))
        
        screen.blit(stand_player, stand_player_rect)
        if not score:
            screen.blit(instruction_text, instruction_text_rect)
            screen.blit(intro_text, intro_text_rect)
        else:
            screen.blit(game_over_text, game_over_text_rect)
            screen.blit(score_text, score_text_rect)

        start_time = pygame.time.get_ticks()

    pygame.display.update()
    clock.tick(60)