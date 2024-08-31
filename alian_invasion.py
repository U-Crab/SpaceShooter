# alian_invasion

import sys

import pygame

from setting import Setting
from ship import Ship

class AlienInvasion:
    """ゲームのアセットと動作を管理する全体のクラス"""
    
    def __init__(self) -> None:
        """ゲームを初期化"""
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width,self.setting.screen_height))
        pygame.display.set_caption("Aliean Invasion")
        
        self.ship = Ship(self)
        
    def run_game(self):
        """ゲームのメインループを開始する"""
        
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
        
    def _check_events(self):
        # キーボードとマウイのイベントを監視する
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_RIGHT:
                        self.ship.moving_right =True
                elif event.type == pygame.KEYUP:
                    if event.key ==pygame.K_RIGHT:
                        self.ship.moving_right = False
    
    def _update_screen(self):
        # ループを通過するたびに画面を再描画する
            self.screen.fill(self.setting.bg_color) # 画面の塗りつぶし
            self.ship.blitme()
            
            # 最新の状態の画面を表示する
            pygame.display.flip()
            
if __name__ == "__main__":
    #ゲームのをインスタンス化し、ゲームを実行する
    ai = AlienInvasion()
    ai.run_game()