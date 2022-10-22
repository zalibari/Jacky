import pygame

gold = (197, 179, 88)
met_gray = (100, 100, 100)
black = (30, 30, 30)
gray = (169, 169, 169)


class Button:
    def __init__(self, text, width, height, pos, elevation, font_size):
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.gui_font = pygame.font.Font(None, font_size)
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = gray
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = met_gray
        self.text = text
        self.text_surf = self.gui_font.render(text, True, black)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, screen):
        action = False
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=18)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=18)
        pygame.Surface.blit(screen, self.text_surf, self.text_rect)
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = gold
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.dynamic_elevation = 0
                self.pressed = True
                action = True
        else:
            self.top_color = gray
        if pygame.mouse.get_pressed()[0] == 0:
            self.dynamic_elevation = self.elevation
            self.pressed = False
        return action

# class Button:
#     def __init__(self, x, y, image, scale):
#         width = image.get_width()
#         height = image.get_height()
#         self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x, y)
#         self.clicked = False
#
#     def draw(self, surface):
#         action = False
#         # get mouse position
#         pos = pygame.mouse.get_pos()
#
#         # check mouseover and clicked conditions
#         if self.rect.collidepoint(pos):
#             if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
#                 self.clicked = True
#                 action = True
#
#         if pygame.mouse.get_pressed()[0] == 0:
#             self.clicked = False
#
#         # draw button on screen
#         surface.blit(self.image, (self.rect.x, self.rect.y))
#
#         return action
