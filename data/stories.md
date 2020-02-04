## lesson 3 path positive
* greet
    - utter_greet
* lesson_3_q {“group”:[”lesson_3_q”]}
    - action_retrieve_questions
* lesson_3_a {"group":["lesson_3_a_1", "lesson_3_a_2", "lesson_3_a_3", "lesson_3_a_4"]}
    - action_retrieve_answers
    - utter_did_that_help
* mood_affirm
    - utter_anything_else

## lesson 3 path negative
* greet
    - utter_greet
* lesson_3_q {“group”:[”lesson_3_q”]}
    - action_retrieve_questions
* lesson_3_a {"group":["lesson_3_a_1", "lesson_3_a_2", "lesson_3_a_3", "lesson_3_a_4"]}
    - action_retrieve_answers
    - utter_did_that_help
* mood_deny
    - utter_submit_better_answer
    - better_answer_form
    - form{"name":"better_answer_form"}

## lesson 4 path positive
* greet
    - utter_greet
* lesson_4_q {“group”:[”lesson_4_q”]}
    - action_retrieve_questions
* lesson_4_a {"group":"["lesson_4_a_1", "lesson_4_a_2", "lesson_4_a_3", "lesson_4_a_4"]
    - action_retrieve_answers
    - utter_did_that_help
* mood_affirm
    - utter_anything_else

## lesson 4 path negative
* greet
    - utter_greet
* lesson_4_q {“group”:[”lesson_4_q”]}
    - action_retrieve_questions
* lesson_4_a {"group":["lesson_4_a_1", "lesson_4_a_2", "lesson_4_a_3", "lesson_4_a_4"]}
    - action_retrieve_answers
    - utter_did_that_help
* mood_deny
    - utter_submit_better_answer
    - better_answer_form
    - form{"name":"better_answer_form"}

## lesson 5 path positive
* greet
    - utter_greet
* lesson_5_q {“group”:[”lesson_5_q”]}
    - action_retrieve_questions
* lesson_5_a {"group":["lesson_5_a_1", "lesson_5_a_2", "lesson_5_a_3", "lesson_5_a_4"]}
    - action_retrieve_answers
    - utter_did_that_help
* mood_affirm
    - utter_anything_else

## lesson 5 path negative
* greet
    - utter_greet
* lesson_5_q {“group”:[”lesson_5_q”]}
    - action_retrieve_questions
* lesson_5_a {"group":["lesson_5_a_1", "lesson_5_a_2", "lesson_5_a_3", "lesson_5_a_4"]}
    - action_retrieve_answers
    - utter_did_that_help
* mood_deny
    - utter_submit_better_answer
    - better_answer_form
    - form{"name":"better_answer_form"}


## say goodbye
* goodbye
    - utter_goodbye
