import mysql.connector

# Establish the connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

# Function to fetch student details by roll number
def rollno(rollno1):
        # Use parameterized query to prevent SQL injection
        sql = f"SELECT * FROM students WHERE rollno = %s"
        
        # Execute the query with the rollno1 value passed as a parameter
        mycursor.execute(sql, (rollno1,))
        
        # Fetch all the results from the query
        myresult = mycursor.fetchall()

        # Check if results exist to avoid errors
        if len(myresult)==2:
            print("error")

        else:

        # Extract the student details
         rollno = myresult[0][0]
         fname = myresult[0][1]
         name = myresult[0][2]
         english = myresult[0][3]
         science = myresult[0][4]
         social = myresult[0][5]
         politics = myresult[0][6]

        # Print the first name (for testing purposes)
         print(f"Student Found: {fname}")

        # Return all the fetched details
        return rollno, fname, name, english, science, social, politics
# Example usage:
# student_details = rollno(1)
# print(student_details)
