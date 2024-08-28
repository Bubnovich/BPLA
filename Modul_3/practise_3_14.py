from practise_3_13 import  *

class SafetyCheck(ICommand):
    def __init__(self, command: ICommand, token: str):
        self.__command = command
        self.__token = token

    def execute(self):
        # проверка ???
        pass

    def check_token(self):
        print("Проверка безопасности...")
        if self.__token == 'my_token':
            print("Токен действительный")
            return True
        else:
            print("Токен недействительный")
            return False

