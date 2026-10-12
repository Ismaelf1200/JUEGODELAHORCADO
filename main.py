import random
import sys
import pygame

# Inicialización de Pygame par el funcionamiento 
pygame.init()
pygame.font.init()

# Configuración de la interfaz para el usuario
WIDTH, HEIGHT = 850, 650
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego del Ahorcado Interactivo")
CLOCK = pygame.time.Clock()

# Paletas de Colores (Estilo Dark UI)
BG_COLOR = (15, 23, 42)        # slate-900
PANEL_COLOR = (30, 41, 59)     # slate-800
ACCENT_BLUE = (59, 130, 246)   # blue-500
TEXT_LIGHT = (248, 250, 252)   # slate-50
TEXT_MUTED = (148, 163, 184)   # slate-400
COLOR_SUCCESS = (52, 211, 153)  # emerald-400
COLOR_DANGER = (244, 63, 94)    # rose-500
KEY_BG = (51, 65, 85)          # slate-700


FONT_TITLE = pygame.font.SysFont("arial", 32, bold=True)
FONT_LARGE = pygame.font.SysFont("arial", 28, bold=True)
FONT_MEDIUM = pygame.font.SysFont("arial", 18, bold=True)
FONT_SMALL = pygame.font.SysFont("arial", 14)

# Clasificacion de temas para el juego 
WORDS_DATABASE = {
    "tecnologia": [
        {"word": "PROGRAMACION", "hint": "Arte de escribir código e instrucciones para ordenadores."},
        {"word": "COMPUTADORA", "hint": "Dispositivo electrónico utilizado para procesar información."},
        {"word": "INTERNET", "hint": "Red global de redes de comunicación interconectadas."},
        {"word": "ALGORITMO", "hint": "Conjunto ordenado y finito de operaciones para resolver un problema."}
    ],
    "animales": [
        {"word": "ELEFANTE", "hint": "Mamífero terrestre más grande, conocido por su gran trompa."},
        {"word": "DELFIN", "hint": "Mamífero marino altamente inteligente y sociable."},
        {"word": "CAMALEON", "hint": "Reptil conocido por cambiar de color para camuflarse."}
    ],
    "paises": [
        {"word": "COLOMBIA", "hint": "País sudamericano famoso por su café y biodiversidad."},
        {"word": "ESPAÑA", "hint": "País europeo ubicado en la Península Ibérica."},
        {"word": "JAPON", "hint": "Nación insular del este de Asia, conocida como el Sol Naciente."}
    ]
}

ALPHABET = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

class HangmanGame:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.categories = ["todas"] + list(WORDS_DATABASE.keys())
        self.selected_category_idx = 0
        self.category_rects = []
        self.key_rects = {}
        self.reset_game()

    def set_category(self, idx):
        if self.selected_category_idx != idx:
            self.selected_category_idx = idx
            self.reset_game()

    def next_category(self):
        self.selected_category_idx = (self.selected_category_idx + 1) % len(self.categories)
        self.reset_game()

    def reset_game(self):
        self.max_attempts = 6
        self.wrong_count = 0
        self.guessed_letters = set()
        self.is_game_over = False
        self.has_won = False
        
        cat_key = self.categories[self.selected_category_idx]
        if cat_key == "todas":
            pool = [item for sublist in WORDS_DATABASE.values() for item in sublist]
        else:
            pool = WORDS_DATABASE[cat_key]
            
        selected = random.choice(pool)
        self.current_word = selected["word"]
        self.current_hint = selected["hint"]

    def handle_guess(self, letter):
        if self.is_game_over or letter in self.guessed_letters:
            return

        self.guessed_letters.add(letter)

        if letter not in self.current_word:
            self.wrong_count += 1
            if self.wrong_count >= self.max_attempts:
                self.is_game_over = True
                self.has_won = False
                self.losses += 1
        else:
            if all(char in self.guessed_letters for char in self.current_word):
                self.is_game_over = True
                self.has_won = True
                self.wins += 1

    def handle_click(self, pos):
        if self.is_game_over:
            return

        # Comprobar clics en categorías
        for idx, rect in enumerate(self.category_rects):
            if rect.collidepoint(pos):
                self.set_category(idx)
                return

        # Comprobar clics en el teclado
        for letter, rect in self.key_rects.items():
            if rect.collidepoint(pos):
                self.handle_guess(letter)
                return

    def draw_categories(self, surface):
        self.category_rects = []
        start_x, start_y = 30, 20
        padding_x, padding_y = 12, 6
        
        label_surf = FONT_SMALL.render("Categoría (Haz clic o pulsa TAB):", True, TEXT_MUTED)
        surface.blit(label_surf, (start_x, start_y))
        
        current_x = start_x
        current_y = start_y + 22

        for idx, cat in enumerate(self.categories):
            is_selected = (idx == self.selected_category_idx)
            text_color = TEXT_LIGHT if is_selected else TEXT_MUTED
            bg_color = ACCENT_BLUE if is_selected else PANEL_COLOR

            cat_text = cat.upper()
            txt_surf = FONT_SMALL.render(cat_text, True, text_color)
            
            btn_w = txt_surf.get_width() + (padding_x * 2)
            btn_h = txt_surf.get_height() + (padding_y * 2)
            rect = pygame.Rect(current_x, current_y, btn_w, btn_h)
            
            pygame.draw.rect(surface, bg_color, rect, border_radius=6)
            if is_selected:
                pygame.draw.rect(surface, TEXT_LIGHT, rect, width=2, border_radius=6)
                
            surface.blit(txt_surf, (current_x + padding_x, current_y + padding_y))
            self.category_rects.append(rect)
            
            current_x += btn_w + 8

    def draw_gallows(self, surface, x, y):
        # Base y Estructura
        pygame.draw.line(surface, TEXT_MUTED, (x - 60, y + 140), (x + 60, y + 140), 5)
        pygame.draw.line(surface, TEXT_MUTED, (x - 30, y + 140), (x - 30, y - 60), 5)
        pygame.draw.line(surface, TEXT_MUTED, (x - 30, y - 60), (x + 30, y - 60), 5)
        pygame.draw.line(surface, TEXT_LIGHT, (x + 30, y - 60), (x + 30, y - 30), 3)

        # Partes del Monigote
        if self.wrong_count >= 1:
            pygame.draw.circle(surface, COLOR_DANGER, (x + 30, y - 10), 20, 4)
        if self.wrong_count >= 2:
            pygame.draw.line(surface, COLOR_DANGER, (x + 30, y + 10), (x + 30, y + 70), 4)
        if self.wrong_count >= 3:
            pygame.draw.line(surface, COLOR_DANGER, (x + 30, y + 25), (x, y + 45), 4)
        if self.wrong_count >= 4:
            pygame.draw.line(surface, COLOR_DANGER, (x + 30, y + 25), (x + 60, y + 45), 4)
        if self.wrong_count >= 5:
            pygame.draw.line(surface, COLOR_DANGER, (x + 30, y + 70), (x + 5, y + 110), 4)
        if self.wrong_count >= 6:
            pygame.draw.line(surface, COLOR_DANGER, (x + 30, y + 70), (x + 55, y + 110), 4)

    def draw(self, surface):
        surface.fill(BG_COLOR)

        # Barra de Categorías (Interactiva)
        self.draw_categories(surface)

        # Indicador de Victorias / Derrotas
        stats_text = f"Ganadas: {self.wins}  |  Perdidas: {self.losses}"
        stats_surf = FONT_MEDIUM.render(stats_text, True, TEXT_LIGHT)
        surface.blit(stats_surf, (WIDTH - stats_surf.get_width() - 30, 25))

        # Área del Dibujo
        self.draw_gallows(surface, 200, 230)

        # Pista
        hint_label = FONT_SMALL.render("PISTA:", True, (251, 191, 36))
        surface.blit(hint_label, (380, 130))
        hint_word = FONT_MEDIUM.render(self.current_hint, True, TEXT_LIGHT)
        surface.blit(hint_word, (380, 155))

        # Palabra Secreta (Guiones/Letras)
        display_word = " ".join([c if c in self.guessed_letters else "_" for c in self.current_word])
        word_surf = FONT_LARGE.render(display_word, True, ACCENT_BLUE)
        surface.blit(word_surf, (380, 220))

        # Intentos Fallidos
        attempts_surf = FONT_SMALL.render(f"Intentos fallidos: {self.wrong_count} / {self.max_attempts}", True, COLOR_DANGER)
        surface.blit(attempts_surf, (380, 280))

        # Teclado en Pantalla (Interactivo)
        start_x, start_y = 60, 410
        btn_w, btn_h, gap = 42, 45, 8
        cols = 10
        self.key_rects = {}

        for idx, letter in enumerate(ALPHABET):
            r = idx // cols
            c = idx % cols
            bx = start_x + c * (btn_w + gap)
            by = start_y + r * (btn_h + gap)
            rect = pygame.Rect(bx, by, btn_w, btn_h)
            self.key_rects[letter] = rect

            if letter in self.guessed_letters:
                bg = COLOR_SUCCESS if letter in self.current_word else (50, 50, 60)
            else:
                bg = KEY_BG

            pygame.draw.rect(surface, bg, rect, border_radius=6)
            let_surf = FONT_MEDIUM.render(letter, True, TEXT_LIGHT)
            surface.blit(let_surf, (bx + (btn_w - let_surf.get_width()) // 2, by + (btn_h - let_surf.get_height()) // 2))

        # Mensaje de Fin de Juego
        if self.is_game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((15, 23, 42, 220))
            surface.blit(overlay, (0, 0))

            msg = "¡FELICIDADES! GANASTE" if self.has_won else f"JUEGO TERMINADO — Era: {self.current_word}"
            color = COLOR_SUCCESS if self.has_won else COLOR_DANGER
            msg_surf = FONT_LARGE.render(msg, True, color)
            sub_surf = FONT_MEDIUM.render("Presiona ESPACIO para jugar de nuevo", True, TEXT_LIGHT)

            surface.blit(msg_surf, (WIDTH // 2 - msg_surf.get_width() // 2, HEIGHT // 2 - 40))
            surface.blit(sub_surf, (WIDTH // 2 - sub_surf.get_width() // 2, HEIGHT // 2 + 20))


def main():
    game = HangmanGame()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Clic izquierdo
                    game.handle_click(event.pos)

            elif event.type == pygame.KEYDOWN:
                if game.is_game_over:
                    if event.key == pygame.K_SPACE:
                        game.reset_game()
                else:
                    if event.key == pygame.K_TAB:
                        game.next_category()
                    else:
                        key_name = event.unicode.upper()
                        if key_name in ALPHABET:
                            game.handle_guess(key_name)

        game.draw(SCREEN)
        pygame.display.flip()
        CLOCK.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
