import random 

class Player():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender
    def choice(self):    
        tool = ['rock','paper','scissors']
        a = random.choice(tool)
        return a

class Game():
    def __init__(self, round):
        self.p1 = Player(name='Stan', age=2, gender='male')
        self.p2 = Player(name='Nini', age=3, gender='male')
        self.round = int(round)

    def start_game(self):
        a1 = 0
        a2 = 0
        for i in range(self.round):
            if self.p1.choice() == 'rock':
                if self.p2.choice() == 'paper':
                    a2 +=1 
                    print(f'Round {i+1}: {self.p1.choice()} vs {self.p1.choice()},{self.p2.name}+1')
                    
                elif self.p2.choice() == 'rock':
                    pass 
                else:
                    a1+=1
                    print(f'Round {i+1}: {self.p1.choice()} vs {self.p1.choice()},{self.p1.name}+1') 
            elif self.p1.choice() == 'paper':
                if self.p2.choice() == 'scissors':
                    a2 +=1 
                    print(f'Round {i+1}: {self.p1.choice()} vs {self.p1.choice()},{self.p2.name}+1')
                elif self.p2.choice() == 'paper':
                    pass 
                else:
                    a1+=1
                    print(f'Round {i+1}: {self.p1.choice()} vs {self.p1.choice()},{self.p1.name}+1') 
            else:
                if self.p2.choice() == 'rock':
                    a2+=1 
                    print(f'Round {i+1}: {self.p1.choice()} vs {self.p1.choice()},{self.p2.name}+1')
                elif self.p2.choice() == 'scissors':
                    pass 
                else:
                    a1+=1
                    print(f'Round {i+1}: {self.p1.choice()} vs {self.p1.choice()},{self.p1.name}+1') 
        if a1 > a2:
            print(f'-------------------------\n{self.p1.name} beats {self.p2.name}! Final score {a1}-{a2}')
        elif a1 < a2:
            print(f'-------------------------\n{self.p2.name} beats {self.p1.name}! Final score {a1}-{a2}')
        else:
            print(f'-------------------------\n{self.p1.name} and {self.p2.name} play to a draw, final score {a1}-{a2}')

b = Game(5)
b.start_game()

# import random 

# class Player():
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age 
#         self.gender = gender
#     def choice(self):    
#         num = random.randint(1,3)
#         return num

# class Game():
#     def __init__(self, round):
#         self.p1 = Player(name='Stan', age=2, gender='male')
#         self.p2 = Player(name='Nini', age=3, gender='male')
#         self.round = int(round)
#         print(f'PLAYER 1\nName:{self.p1.name} Age:{self.p1.age} Gender:{self.p1.gender}\nPLAYER 2\nName:{self.p2.name} Age:{self.p2.age} Gender:{self.p2.gender}\n-------------------')

#     def start_game(self):
#         a1 = 0
#         a2 = 0
#         for i in range(self.round):
#             m1 = self.p1.choice()
#             m2 = self.p2.choice()
#             if m1 == 1 and m2 == 3:
#                 a1+=1
#             elif m1 == 3 and m2 == 1:
#                 a2+=1
#             elif m1>m2:
#                 a1+=1 
#             elif m2<2:
#                 a2+=1 
#             else:
#                 pass 
#         if a1 > a2:
#             print(f'{self.p1.name} beats {self.p2.name}! Final score {a1}-{a2}')
#         elif a1 < a2:
#             print(f'{self.p2.name} beats {self.p1.name}! Final score {a1}-{a2}')
#         else:
#             print(f'{self.p1.name} and {self.p2.name} play to a draw, final score {a1}-{a2}')
    
# b = Game(30)
# b.start_game()
