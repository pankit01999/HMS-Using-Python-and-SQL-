# HMS-Using-Python-and-SQL-
### Project Description: Hospital Management System

### Overview
The Hospital Management System (HMS) is a comprehensive software application designed to manage and streamline hospital operations. Developed using Python and SQL, this system provides functionalities for managing patient prescriptions, updating records, and performing essential CRUD (Create, Read, Update, Delete) operations. The system is user-friendly and features a graphical user interface (GUI) for easy interaction.

### Key Features

1. **Prescription Management**
   - **Insert Prescription Data**: Users can enter new prescription information into the system. This includes details such as patient ID, doctor ID, medication name, dosage, and administration instructions. The interface includes a button named "Prescription Data" that, when clicked, saves the entered prescription data to the database.
   - **Update Prescription Data**: Allows users to modify existing prescription records. Users can search for a prescription by patient ID or other identifiers and update details as needed.
   - **Delete Prescription Data**: Users can remove prescription records from the system if they are no longer needed or were entered in error.
   - **View Prescription Data**: Users can view and search prescription records based on various criteria such as patient ID, medication name, or date.

2. **Data Entry and Management**
   - **Insert Data**: Use buttons such as "Add New Record" to input new patient or prescription information into the database.
   - **Update Data**: Modify existing records using an "Update" button to ensure the database remains current and accurate.
   - **Delete Data**: Remove outdated or incorrect records with a "Delete" button.
   - **Reset**: Clear all fields on the form or GUI to reset the data entry process and start fresh.
   - **Exit**: Safely close the application and ensure that any unsaved data is handled appropriately.

### Technical Specifications

1. **Backend**:
   - **Database**: SQL (Structured Query Language) for managing and querying the hospital's database. The database includes tables for patients, doctors, and prescriptions.
   - **Python Libraries**: 
     - `sqlite3` or `mysql-connector` for connecting to and managing the SQL database.
     - `tkinter` for creating the graphical user interface (GUI).

2. **Frontend**:
   - **GUI Framework**: `tkinter` for a simple, easy-to-use interface where users can input, update, and delete prescription data.
   - **Buttons and Forms**: 
     - "Prescription Data" button for adding new records.
     - "Update" button for modifying existing records.
     - "Delete" button for removing records.
     - "Reset" button to clear input fields.
     - "Exit" button to close the application.

### User Interface Workflow

1. **Home Screen**:
   - Displays buttons for different functionalities: Add New Record, Update Record, Delete Record, View Records, Reset, and Exit.

2. **Prescription Data Form**:
   - Fields for entering prescription details (patient ID, doctor ID, medication name, dosage, etc.).
   - "Prescription Data" button to submit the form and save data to the database.
   - "Reset" button to clear the form.

3. **Update/Delete Records**:
   - Search functionality to find records by patient ID or other identifiers.
   - Forms and buttons for updating or deleting records.

4. **Exit**:
   - Closes the application and ensures any unsaved data is either saved or discarded based on user preferences.

### Installation and Setup

1. **Dependencies**: Ensure Python is installed along with necessary libraries (`tkinter`, `sqlite3` or `mysql-connector`).
2. **Database Setup**: Initialize the SQL database with the required tables and schemas.
3. **Application Launch**: Run the Python script to start the application and interact with the GUI.

### Future Enhancements

- **Advanced Search**: Implement more sophisticated search functionalities for prescriptions and patient records.
- **User Authentication**: Add user roles and permissions to restrict access to sensitive data.
- **Reporting**: Generate reports on prescription data and patient histories.

This Hospital Management System aims to simplify hospital operations and enhance efficiency in prescription management, making it a valuable tool for healthcare facilities.



![A](https://github.com/user-attachments/assets/a96214a0-3024-439a-baf8-e8f2023581bd)
