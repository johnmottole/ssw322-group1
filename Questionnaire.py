class Questionnaire(object):
    def __init__(self, name, tag):
        self._name_id = name
        self._tag = tag
        self._question_list = []
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self.tag = value

    @property
    def name_id(self):
        return self._name_id

    @name_id.setter
    def name_id(self, value):
        self._name_id = value

    @property
    def question_list(self):
        return self._question_list

    def add_question(self, question):
        self._question_list.append(question)
