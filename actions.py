from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction
import pandas as pd

class ActionQuestion(Action):
  def name(self):
    return "action_retrieve_questions"


  def run(self, dispatcher, tracker, domain):
    group = tracker.get_slot("group")
    dispatcher.utter_message("Please choose the number that corresponds with the question. Type in your response as lesson number_question number. For example, if you wanted to see the answer to question 4 from lesson 3, type 3_4. After that, the answer will be revealed.")
    if group == "lesson_3_q":
        switcher_3 = {
            "1": "1. What does the number of nodes in the input layer correspond to?",
            "2": "2. What does the number of nodes in the output layer correspond to?",
            "3": "3. What does L2 regularization achieve?",
            "4": "4. What is the optimization algorithm used for minimizing the cost of an error function?"
        }
        for values in switcher_3.values():
            dispatcher.utter_message(values)


class ActionAnswer(Action):
  def name(self):
    return "action_retrieve_answers"

  def lesson_3_answers(self, number=None):
    switcher = {
        "1": "The number of data points determines the number of nodes in the input layer.",
        "2": "The number of classes determines the number of nodes in the output layer.",
        "3": "It helps mitigate the issue of overfitting the model to the data",
        "4": "Gradient Descent. What it does is that it mathematically closes the gap between the model predicted output and the actual result."
    }
    if number == "1":
      return switcher["1"]
    elif number == "2":
      return switcher["2"]
    elif number == "3":
      return switcher["3"]
    elif number == "4":
      return switcher["4"]

  def run(self, dispatcher, tracker, domain):
    group = tracker.get_slot("group")

    if group == "lesson_3_a_1":
      dispatcher.utter_message(self.lesson_3_answers(group[-1]))
    elif group == "lesson_3_a_2":
      dispatcher.utter_message(self.lesson_3_answers(group[-1]))
    elif group == "lesson_3_a_3":
      dispatcher.utter_message(self.lesson_3_answers(group[-1]))
    elif group == "lesson_3_a_4":
      dispatcher.utter_message(self.lesson_3_answers(group[-1]))

class AnswerForm(FormAction):
    def name(self):
        return "better_answer_form"

    @staticmethod
    def required_slots(tracker: Tracker):
        return ["better_answer"]


    def slot_mappings(self):
        dict_answer = {"better_answer": [self.from_entity(entity="slack_id"),
                                         self.from_entity(entity="lessonnumber_questionnumber"),
                                         self.from_entity(entity="better_answer"), self.from_text()]}

        return dict_answer

    def create_db(self, data_list):
        database = pd.DataFrame(columns=["Slack_ID", "LessonNumber_QuestionNumber", "Better_Answer"])
        database = database.append({"Slack_ID": data_list[0], "LessonNumber_QuestionNumber": data_list[1],
                        "Better_Answer": data_list[2]}, ignore_index=True)
        database.to_csv("database.csv")

    def submit(self, dispatcher, tracker, domain):
        text = tracker.get_slot("better_answer")
        text_arr = text.split(" | ")
        self.create_db(text_arr)
        dispatcher.utter_message("Submitted! Thank you. :)")
        return []
