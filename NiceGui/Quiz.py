from nicegui import ui

questions = [
    ("Vad är 5 + 3?", ["6", "8", "10"]),
    ("Vilket land ligger i Europa?", ["Brasilien", "Sverige", "Japan"]),
    ("Vad är färgen på himlen en klar dag?", ["Blå", "Grön", "Röd"]),
    ("Hur många dagar har en vecka?", ["5", "7", "10"]),
]

@ui.page('/')
def quiz():

    ui.label("Quiz Master 4000")

    def show_question(index=0):
        ui.clear()

        if index >= len(questions):
            ui.label("Du är klar!")
            ui.button("Börja om", on_click=lambda: show_question(0))
            return

        question, answers = questions[index]

        ui.label(f"Fråga {index + 1}")
        ui.label(question)

        for answer in answers:
            ui.button(answer, on_click=lambda i=index+1: show_question(i))

    ui.button("Starta Quiz", on_click=lambda: show_question())

ui.run(native=True)