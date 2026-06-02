import cmd

class ChatCLI(cmd.Cmd):
    prompt='>>'
    intro='Welcome to AI Chatbot CLI'

    def do_quit(self , line):
        """Exit the CLI"""
        return True

    def do_save(self , line):
        """" Save the Conversation"""
        print("Conversation Saved")

    def do_hello(self , line):
        """" Hello Greet"""
        print("hello")

    
if __name__ == '__main__':
    ChatCLI().cmdloop()

