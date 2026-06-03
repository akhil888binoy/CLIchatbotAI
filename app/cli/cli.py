import cmd
from app.services.chat_service import chat_model

provider = "OLLAMA"


class ChatCLI(cmd.Cmd):
    prompt = ">> "
    intro = "Welcome to AI Chatbot CLI"
    print(f"Current Model {provider}")

    def do_quit(self, line):
        """Exit the CLI"""
        return True

    def do_choosemodel(self, line):
        """Choose a model"""
        global provider
        print(" 1.Ollama")
        selection = line.strip().lower()
        if selection in {"1", "ollama"}:
            provider = "OLLAMA"
        else:
            print("Unknown model. Keeping current provider.")
            return
        print(f"Current Model {provider}")

    def do_chat(self, line):
        response = chat_model(line, provider)
        print(response)


if __name__ == '__main__':
    ChatCLI().cmdloop()
