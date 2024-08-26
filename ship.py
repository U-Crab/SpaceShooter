import pygame


class Ship():
    """宇宙戦艦を管理するクラス"""
    
    def __init__(self,ai_game) -> None: #aigameにはalian_invasionインスタンスが代入される。これによってshipは全てのAlianInvasionで定義されたメソッドを簡単に利用できる
        """宇宙船を初期化"""
        
        self.screen = ai_game.screen #ディスプレイサイズをAlianInvasionから取得 pygame.display.set_mode(~)
        self.screen_rect = ai_game.screen.get_rect() #AlianInvasionの長方形の情報を取得
        
        # 宇宙船の画像の読み込み。サイズの取得
        self.image = pygame.image.load("img/ship.bmp")
        self.rect = self.image.get_rect()
        
        #新しい宇宙船を画面下部の中央に配置する
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """宇宙船を現在位置に描画"""
        self.screen.blit(self.image,self.rect)
    