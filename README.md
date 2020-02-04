# Student-Powered Chatbot
This is an ongoing project for the Udacity Bertelsmann AI Program where this RASA chatbot will be utilized. The data is coming from past quizzes currently from the #lesson_3_nn. The data will be expanded as we collect more answers from previous quizzes. 

A couple of housekeeping rules. In order to install the RASA library and all of its depencies and run everything correctly, please run the folowing commands from this [Stackoverflow post](https://stackoverflow.com/questions/46713653/installing-rasa-on-windows). You may need to downgrade your tensorflow version to 1.15.0 depending on whether you have the newest one.

To train the models, type in this command: 
`python -m rasa train` 

To view the cross-validation score from training the model, type in this command: 
`python -m rasa test nlu -u nlu.md --config config.yml --cross-validation`

For running the chatbot, please do the following:
`python -m rasa run actions --actions actions --debug (the debug flag is optional)`

Then: 
`python -m rasa shell --endpoints endpoints.yml`



