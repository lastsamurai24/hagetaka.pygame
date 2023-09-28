import pygame

# クラス定義
class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1000  # 初期資金
        self.companies = []  # 所有する会社のリスト

class Company:
    def __init__(self, name, value):
        self.name = name
        self.value = value  # 会社の価値

class Game:
    def __init__(self, players):
        self.players = players
        self.companies = [Company("CompanyA", 100), Company("CompanyB", 150)]
        self.current_player_index = 0

    def player_turn(self):
        # プレイヤーのターンの処理
        pass

    def next_player(self):
        self.current_player_index += 1
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0

    def run(self):
        pygame.init()

        WIDTH, HEIGHT = 800, 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ハゲタカのえじき")

        font = pygame.font.SysFont(None, 36)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # キー入力で次のプレイヤーのターンに移行
                if event.type == pygame.KEYDOWN:
                    self.next_player()

            screen.fill((255, 255, 255))

            # 現在のプレイヤーのターンを表示
            turn_info = font.render(f"現在のターン: {self.players[self.current_player_index].name}", True, (0, 0, 0))
            screen.blit(turn_info, (10, 10))

            # プレイヤー情報の表示
            y_offset = 50
            for player in self.players:
                player_info = font.render(f"{player.name}: {player.money}円", True, (0, 0, 0))
                screen.blit(player_info, (10, y_offset))
                y_offset += 40

            # 会社情報の表示
            for company in self.companies:
                company_info = font.render(f"{company.name}: {company.value}円", True, (0, 0, 0))
                screen.blit(company_info, (10, y_offset))
                y_offset += 40

            pygame.display.flip()

        pygame.quit()

# ゲームの開始
players = [Player("Player1"), Player("Player2")]
game = Game(players)
game.run()