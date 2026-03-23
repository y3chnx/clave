from llm_engine import load_llm, generate_reply


title = """
         ππ≈+√          π×+×√π                 
        π÷++++≠π       π++++++≠         
       √-+++++≠√√√√√√√√√≈=+++++×π       
       ≠++++++++++++++++++++++++=           ██████╗██╗      █████╗ ██╗   ██╗███████╗ 
       ÷++++++++++++++++++++++++÷          ██╔════╝██║     ██╔══██╗██║   ██║██╔════╝
       ×+++×√√√√√√=+++=√√√√√×+++÷          ██║     ██║     ███████║██║   ██║█████╗  
       =+++-π     =+++=    √-+++=          ██║     ██║     ██╔══██║╚██╗ ██╔╝██╔══╝  
       ≠++++×√    =+++=  π√-++++=          ╚██████╗███████╗██║  ██║ ╚████╔╝ ███████╗
        ≠+++++++×≠∞=+++÷≠-+++++++=          ╚═════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝
       ≠++++++++++++++++++++++++=       
       ≠+++×≈-++++++++++++×≈×+++=       
       ≈×××≠    π√∞∞∞∞√π    ≠===∞                                  
"""


def main():
    print(title)
    llm = load_llm()
    print("✅ | Clave Beta model Loaded")
    history = []

    while True:
        user_input = input("User:")
        if user_input.lower() == "exit":
            break

        history.append(f"User: {user_input}")
        prompt = "\n".join(history) + "\nAssistant:"

        reply = generate_reply(llm, prompt)
        print("Clave:", reply)

        history.append(f"Assistant: {reply}")

if __name__ == "__main__":
    main()