def print_doors():
    """Printar dörrarna."""
    print()
    print(r"   _________________________________________________________ ")
    print(r" /|     -_-                                             _-  |\ ")
    print(r"/ |_-_- _                                         -_- _-   -| \ ")
    print(r"  |                            _-  _--                      | ")
    print(r"  |                            ,                            | ")
    print(r"  |      .-'````````'.        '(`        .-'```````'-.      | ")
    print(r"  |    .` |           `.      `)'      .` |           `.    | ")
    print(r"  |   /   |   ()        \      U      /   |    ()       \   | ")
    print(r"  |  |    |    ;         | o   T   o |    |    ;         |  | ")
    print(r"  |  |    |     ;        |  .  |  .  |    |    ;         |  | ")
    print(r"  |  |    |     ;        |   . | .   |    |    ;         |  | ")
    print(r"  |  |    |     ;        |    .|.    |    |    ;         |  | ")
    print(r"  |  |    |____;_________|     |     |    |____;_________|  | ")
    print(r"  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  | ")
    print(r"  |  |  / __  ()        -|        -  |  /  __--      -   |  | ")
    print(r"  |  | /        __-- _   |   _- _ -  | /        __--_    |  | ")
    print(r"  |__|/__________________|___________|/__________________|__| ")
    print(r" /                                             _ -        lc \ ")
    print(r"/   -_- _ -             _- _---                       -_-  -_ \ ")
    print()


def print_dragon():
    """Printar draken."""
    print()
    print(r"            |                     | ")
    print(r"         \     /               \     / ")
    print(r"        -= .'> =-             -= <'. =- ")
    print(r"           '.'.                 .'.' ")
    print(r"             '.'.             .'.' ")
    print(r"               '.'.----^----.'.' ")
    print(r"                /'==========='\ ")
    print(r"            .  /  .-.     .-.  \  . ")
    print(r"            :'.\ '.O.') ('.O.' /.': ")
    print(r"            '. |               | .' ")
    print(r"              '|      / \      |' ")
    print(r"               \     (o'o)     / ")
    print(r"               |\             /| ")
    print(r"               \('._________.')/ ")
    print(r"                '. \/|_|_|\/ .' ")
    print(r"                 /'._______.'\ lc ")
    print()


def print_treasure():
    """Printar skattkistan."""
    print()
    print("                      _.--. ")
    print("                  _.-'_:-'|| ")
    print("              _.-'_.-::::'|| ")
    print("         _.-:'_.-::::::'  || ")
    print("       .'`-.-:::::::'     || ")
    print("      /.'`;|:::::::'      ||_ ")
    print("     ||   ||::::::'     _.;._'-._ ")
    print("     ||   ||:::::'  _.-!oo @.!-._'-. ")
    print("     ('.  ||:::::.-!()oo @!()@.-'_.| ")
    print("      '.'-;|:.-'.&$@.& ()$%-'o.'-U|| ")
    print("        `>'-.!@%()@'@_%-'_.-o _.|'|| ")
    print("         ||-._'-.@.-'_.-' _.-o  |'|| ")
    print("         ||=[ '-._.-+U/.-'    o |'|| ")
    print("         || '-.]=|| |'|      o  |'|| ")
    print("         ||      || |'|        _| '; ")
    print("         ||      || |'|    _.-'_.-' ")
    print("         |'-._   || |'|_.-'_.-' ")
    print("          '-._'-.|| |' `_.-' ")
    print("              '-.||_/.-' ")
    print()


def print_guard():
    """Printar vakten."""
    print()
    print(r"                        ___I___ ")
    print(r"                       /=  |  #\ ")
    print(r"                      /.__-| __ \ ")
    print(r"                      |/ _\_/_ \| ")
    print(r"                      (( __ \__)) ")
    print(r"                   __ ((()))))()) __ ")
    print(r"                 ,'  |()))))(((()|# `. ")
    print(r"                /    |^))()))))(^|   =\ ")
    print(r"               /    /^v^(())()()v^;'  .\ ")
    print(r"               |__.'^v^v^))))))^v^v`.__| ")
    print(r"              /_ ' \______(()_____(   | ")
    print(r"         _..-'   _//_____[xxx]_____\.-| ")
    print(r"        /,_#\.=-' /v^v^v^v^v^v^v^v^| _| ")
    print(r"        \)|)      v^v^v^v^v^v^v^v^v| _| ")
    print(r"         ||       :v^v^v^v^v^v`.-' |#  \, ")
    print(r"         ||       v^v^v^v`_/\__,--.|\_=_/ ")
    print(r"         ><       :v^v____|  \_____|_ ")
    print(r"      ,  ||       v^      /  \       / ")
    print(r"     //\_||_)\    `/_..-._\   )_...__\ ")
    print(r"    ||   \/  #|     |_='_(     |  =_(_ ")
    print(r"    ||  _/\_  |    /     =\    /  '  =\ ")
    print(r"     \\\/ \/ )/    |=____#|    '=....#| ")
    print()


def print_game_over():
    """Printar gameover bilden."""
    print()
    print(r"   _____          __  __ ______    ______      ________ _____ ")
    print(r"  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ ")
    print(r" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) | ")
    print(r" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / ")
    print(r" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ ")
    print(r"  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ ")
    print()


def print_pic(state):
    """Printar bilden tillhörande spelets stadie."""
    match state:
        case "Start":
            return print_doors()
        case "Red":
            return print_dragon()
        case "Chest":
            return print_treasure()
        case "Guard":
            return print_guard()
        case "Take":
            return print_guard()
        case "Leave":
            return print_guard()
        case "Talk":
            return print_guard()
        case "End":
            return print_game_over()
        case _:
            return
