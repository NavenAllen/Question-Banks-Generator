This web application generates Question Banks based on their previous performance of each chapter and question types. It is a simple Django app.



To set things up initially, execute  **python mange.py makemigrations**  
                         **python manage.py migrate**  

To run the app hereafter, execute **python manage.py runserver**
                    
The app is now running on the localhost where you can upload your Marks Data file of two sheets, out of which the sheet containing the older marks should be of the following format:
![Imgur](https://i.imgur.com/CgiZPDr.jpg)

And then, in the next page, you can select whichever chapters and question types you want questions from, and also the number of questions.  
The next page lets you download the question bank which has been generated for each student.
 
