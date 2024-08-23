import pygame


class Ship():
    """宇宙戦艦を管理するクラス"""
    
    def __init__(self,ai_game) -> None:
        """宇宙船を初期化"""
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # 宇宙船の画像の読み込み。サイズの取得
        self.image = pygame.image.load("img/ship.bmp")
        self.rect = self.image.get_rect()
    