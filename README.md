# Database Lab 2: Login & To-Do Application

## 1. Team Members
* Takla Hany Shaker Said (ID: 2304033)

## 2. Technology Stack
* **Back End:** Python (Flask)
* **Front End:** HTML, JavaScript
* **Database:** MySQL (PyMySQL)

## 3. How to Run
1. Clone the repository and navigate to the project folder.
2. Create and activate a Conda environment: `conda create -n flask_todo python=3.11 -y` and `conda activate flask_todo`.
3. Install requirements: `pip install -r requirements.txt`.
4. Run `database/schema.sql` in your MySQL server to create the database and tables.
5. Copy `.env.example` to a new file named `.env`. Update it with your MySQL database credentials and a random Flask secret key.
6. Start the server: `python app.py`.
7. Open `http://127.0.0.1:5000` in your web browser.

## 4. Features Built
* User registration, login, logout, password hashing (bcrypt), and to-do list operations (add, edit, toggle, delete).
* User interface with client-side and server-side validation.
* **Bonus:** Displaying the total count of open to-dos.

## 5. Answers to Questions
**(a) Why do UPDATE and DELETE contain AND user_id = ? and what changes if you remove it?**
To make sure that the user edit only his tasks. If removed the use can try to edit a task for diffrent user by manually edit the todo_id in browser.

**(b) What happens if you insert a to-do for a user_id that does not exist, and which constraint of the lecture is that?**
An error happen and the todo will not be inserted since the user_id is a forign key which mean it should be exists in the user table too.

**(c) Why do you store a hash and not the password?**
To make it more safe so it don't be big problem if leaked

**(d) The name column is NOT NULL: why did you still need your own check for an empty name?**
Null isn't equal empty string so we need to run a validation on the name.