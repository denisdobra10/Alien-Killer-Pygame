import pygame


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Transform:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.localScale = Vector2(100, 100)



class ScreenOptions:
    def render_text_on_screen(screen, text_content: str, text_color_rgb, text_size: int, position: Vector2):
        font = pygame.font.Font(None, text_size)
        text_surface = font.render(text_content, True, text_color_rgb)
        screen.blit(text_surface, (position.x, position.y)) 
    

    def render_image_on_screen(screen, image, position: Vector2):
        screen.blit(image, (position.x, position.y))



