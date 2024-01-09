import random
from enum import IntEnum


class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock
}



class EstrategiaRandom:
    
    def get_computer_action(self,_user_action):#user action tiene un barra baja delante porque me salta un warning al no usarlo en la función
        computer_selection = random.randint(0, len(GameAction) - 1)
        computer_action = GameAction(computer_selection)
        print(f"Computer picked {computer_action.name}.")    
        return computer_action
    
    
    
class EstrategiaPrincipal:
    def __init__(self):
        self.history=[]
        
    def get_computer_action(self,user_action):
        computer_action=None
        
        if len(self.history)==0:#Comportamiento en la primera ronda
            computer_selection = random.randint(0, len(GameAction) - 1)
            computer_action = GameAction(computer_selection)
        
       
        elif assess_game_silent(self.history[-1][0],self.history[-1][1])==GameResult.Defeat:#Cuando la máquina pierde en la ultima ronda
            past_user_action=self.history[-1][0]
            if len(self.history)>=2 and assess_game_silent(self.history[-2][0],self.history[-2][1])==GameResult.Defeat:#Esto si ha perdido dos veces seguidas
                
                lista_posibilidades=[GameAction.Rock,GameAction.Scissors,GameAction.Paper]
                past_computer_action=self.history[-1][1]
                past_past_computer_action=self.history[-2][1]
                
                if past_computer_action in lista_posibilidades:
                    lista_posibilidades.remove(past_computer_action)#Se elimina el lo que se ha utilizado en el último turno
                if past_past_computer_action in lista_posibilidades:
                    lista_posibilidades.remove(past_computer_action)#Se elimina el lo que se ha utilizado en el penúltimo turno
                    
                computer_selection = random.randint(0, len(lista_posibilidades) - 1)
                computer_action = GameAction(computer_selection)  
                      
            else:#Cuando solo ha perdido una vez    
                if past_user_action==GameAction.Scissors:
                    computer_action=GameAction.Rock
                elif past_user_action==GameAction.Rock:
                    computer_action=GameAction.Paper
                else: 
                    computer_action=GameAction.Scissors
            
        elif assess_game_silent(self.history[-1][0],self.history[-1][1])==GameResult.Victory: # Esoto es si ha ganado la última ronda
            past_user_action=self.history[-1][0]
            if len(self.history)>=2 and assess_game_silent(self.history[-2][0],self.history[-2][1])==GameResult.Victory:#Esto si ha ganado dos veces seguidas
                computer_action = past_user_action
            else: # Esto es si solo ha ganado una vez
                past_user_action=self.history[-1][0]
                computer_action = past_user_action
        
        elif assess_game_silent(self.history[-1][0],self.history[-1][1])==GameResult.Tie: # Esto es si ha empatado la ultima ronda
            lista_posibilidades=[GameAction.Rock,GameAction.Scissors,GameAction.Paper]
            past_computer_action=self.history[-1][1]
            if past_computer_action in lista_posibilidades:
                lista_posibilidades.remove(past_computer_action)#Se elimina el lo que se ha utilizado en el último turno
            computer_selection = random.randint(0, len(lista_posibilidades) - 1)
            computer_action = GameAction(computer_selection) 
                            
        self.history.append([user_action,computer_action])
        print(f"Computer picked {computer_action.name}.") 
        return computer_action 

def assess_game_silent(user_action, computer_action):

    game_result = None

    if user_action == computer_action:
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            game_result = GameResult.Victory
        else:
            game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            game_result = GameResult.Victory
        else:
            game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            game_result = GameResult.Defeat
        else:          
            game_result = GameResult.Victory

    return game_result

def assess_game(user_action, computer_action):

    game_result = None

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            game_result = GameResult.Victory
        else:
            print("Paper covers rock. You lost!")
            game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            game_result = GameResult.Victory
        else:
            print("Scissors cuts paper. You lost!")
            game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Scissors cuts paper. You won!")
            game_result = GameResult.Victory

    return game_result


def get_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)
    
    
    
    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'

def get_strategy():
    strategy=EstrategiaRandom() #Esta sería la estrategia por defecto
    
    dificulty_selection = int(input(f"\Pick a mode Easy(1) or Hard(2)"))
    
    if dificulty_selection==1:
        strategy=EstrategiaRandom()
    elif dificulty_selection==2:
        strategy=EstrategiaPrincipal()
    return strategy


def main():
    strategy= get_strategy()   
    number_games = int(input(f"How many games do you want to play?"))
    games_played = 0
    
    while number_games > games_played:
        
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue
        
        computer_action = strategy.get_computer_action(user_action)       
        assess_game(user_action, computer_action)
        
        games_played+=1    
        
        if games_played==number_games and play_another_round():
                number_games+=1
                

if __name__ == "__main__":
    main()