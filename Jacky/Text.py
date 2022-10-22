import pygame

gold = (197, 179, 88)
met_gray = (130, 130, 130)
black = (30, 30, 30)
gray = (169, 169, 169)


class Text:
    def __init__(self, text, width, height, pos, font_size):
        self.gui_font = pygame.font.Font(None, font_size)
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = black
        self.text = text
        self.text_surf = self.gui_font.render(text, True, gold)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw_t(self, screen):
        self.text_rect.center = self.top_rect.center
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=5)
        pygame.Surface.blit(screen, self.text_surf, self.text_rect)

