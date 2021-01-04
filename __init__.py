from mycroft import MycroftSkill, intent_file_handler


class CandleControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.candle.intent')
    def handle_control_candle(self, message):
        self.speak_dialog('control.candle')


def create_skill():
    return CandleControl()

