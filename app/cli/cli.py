import cmd
from services.chat_service import chat_model


provider = "OLLAMA"
class ChatCLI(cmd.Cmd):
    prompt='>>'
    intro='Welcome to AI Chatbot CLI'
    print(f"Current Model {provider}")

    def do_quit(self , line):
        """Exit the CLI"""
        return True

    def do_choosemodel(self, line):
        """"Choose a Model"""
        print(" 1.Ollama")
        provider = line
        print(f"Current Model {provider}")


    def do_chat(self , line):
        chat_model(line , provider)

    
if __name__ == '__main__':
    ChatCLI().cmdloop()

