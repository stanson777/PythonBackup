import PySimpleGUI as sg


class Hangman:
    def __init__(self):
        layout=[
            [
                self._build_canvas_frame(),
                self._build_letters_frame(),
            ],
            [
                self._build_guessed_word_frame(),
            ],
            [
                self._build_action_buttons_frame(),
            ]
        ]
        self._window=sg.Window(
            title="Better Hangman",
            layout=[[]],
            finalize=True,
            margins=(100,100),
        )

        def _build_canvas_frame(self)

    def read_event(self):
        event=self._window.read()
        event_id=event[0] if event is not None else None
        return event_id

    def close(self):
        self._window.close()



if __name__=="__main__":
    game=Hangman()
    while True:
        event_id=game.read_event()
        if event_id in {sg.WIN_CLOSED}:
            break

    game.close()