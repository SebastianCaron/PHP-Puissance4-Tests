from utils import *
import test_create_game
import test_join_game
import test_delete_game
import test_get_game
import test_play
import test_list_games

GAME_PATH = "~sebastian_caron/api/"
#GAME_PATH = "~paul_nassiri/PUISSANCE4/API"
BASE_URL = "http://172.31.143.240"


if __name__ == "__main__":
    print(BASE_URL)
    print(GAME_PATH)
    print(BASE_URL + GAME_PATH)
    r = list_all_games(BASE_URL, GAME_PATH)
    l = 0
    if("error" not in r or  r["error"] == 0):
        l = len(r["games"])

    print(f'LEN START : {l}')
    test_create_game.test_create_games(BASE_URL, GAME_PATH)
    test_join_game.test_join_games(BASE_URL, GAME_PATH)
    test_delete_game.test_delete_games(BASE_URL, GAME_PATH)
    test_get_game.test_get_games(BASE_URL, GAME_PATH)
    test_play.test_play(BASE_URL, GAME_PATH)
    test_list_games.test_list_games(BASE_URL, GAME_PATH)
    r = list_all_games(BASE_URL, GAME_PATH)
    l2 = 0
    if("error" not in r or r["error"] == 0):
        l2 = len(r["games"])
    print(f'LEN END : {l2}')
    if(l == l2):
        print("TEST TAILLE : OK !")
    
    