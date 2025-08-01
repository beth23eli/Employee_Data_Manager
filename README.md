# Employees payroll management
This is app that has the main feature to manage employees payroll.
It was built with:
- ```PostgreSQL``` as the relational database to store the data about employees, their salaries, and related data. I created the database company_management_db and then, three tables:
  - The ```employees``` table contains the following columns:
      - id - the identifier of an employee;
      - name - the first name of an employee;
      - surname - the last name of an employee;
      - cnp_number - the personal identification number of an employee;
      - email - the email address of an employee;
      - position_id - the foreign key referencing the positions table, indicating the employee’s job title and associated base salary;
      - manager_id – the foreign key referencing the managers table, identifying the manager responsible for the employee;
      - num_worked_days - how many days did the employee worked in the previous month;
      - num_vacation_days - how many vacation days did the employee take;
      - bonuses - the sum of existent bonuses;
      - created_at - when the employee was added to the database as record. <br/><br/>
  - The ```managers``` table contains the following columns:
      - id - the identifier of a manager;
      - name - the first name of a manager;
      - surname - the last name of a manager;
      - email - the email address of a manager.
    <br/><br/>
  - The ```positions``` table contains the following columns:
      - id - the identifier of a position;
      - title - the name of an existent position in the company;
      - salary - the salary paid to an employee that has a certain position.
    <br/><br/>
- ```Python with Flask``` as the app server that processes the user requests and interacts with the database to get employee data. To communicate with the interface, I created the routes:
    - ROUTE: /operations/generation/createAggregatedEmployeeData, method: POST -  This route is used to make the request for generating the excel file with the  employees' data for the manager;
    - ROUTE: /operations/generation/createPdfForEmployees, method: POST - This route was created to make the request for generating the personalized PDF files for each employee that contains information about the salary for the previous month;
    - ROUTE: /employees/operations/sending/sendAggregatedEmployeeData, method: POST -  This route is used to make the request for sending the excel file to the manager via email;
    - ROUTE: /employees/operations/sending/sendPdfToEmployees, method: POST - This route was created to make the request for sending the generated pdfs to each employee;
    - ROUTE: /employees/operations/generation/createArchive, method: POST - This route was created to make the request for generating the archive with all Excel and PDF files;
    - ROUTE: /employees/all, method: GET - This route was created to obtain all the employees;
    - ROUTE: /employees/positions/all, method: GET - This route was created to obtain all the existent positions.
    <br/><br/>
- ```ReactJS``` for the UI. The user interface is a SPA.
    <br/><br/>
- ```Docker Compose``` as the tool used for managing and running the multi-container Docker app. It creates 3 containers: the first one is for the backend, the second one is for the database and the third is for the frontend.


### Important additions:
- Packages:
    - ```Faker``` – Used to seed the database with realistic fake employee and manager data;
    - ```fpdf``` – Used to create the encrypted PDF salary reports per employee;
    - ```openpyxl``` – Used to generate the excel file;
    - ```flask_mail``` – Sends emails to managers and employees, with optional file attachments (PDF/Excel).

- ORM:
    - ```SQLAlchemy``` – Used for mapping Python classes to database tables and managing relationships between models.
- Blueprints:
    - Added ```employees``` blueprint for encapsulating all routes and logic for managing employee records;
    - Added ```generation``` blueprint for encapsulating all routes and logic for generating the required files;
    - Added ```sending``` blueprint for encapsulating all routes and logic for sending the files;
    - Added ```positions``` blueprint for encapsulating all routes and logic for managing positions.

  
## Running this app:
You will need to have Docker installed. If you are using Windows, it is needed to follow along inside of WSL or WSL2, where you are going to run shell commands.

__Step 1__: Clone this repo anywhere you want and move into the directory:
```
git clone https://github.com/beth23eli/Employee_Data_Manager.git

cd Employee_Data_Manager
```

__Step 2__: Copy an example .env file because the real one is git ignored:
```
cp .env.example .env
```

__Step 3__: Start **wsl**:
```
wsl
```
__Step 4__: Open **Docker Desktop**.
 

__Step 5__: Run the **docker-compose** file to build the images and to run the containers:
```
docker-compose up --build 
```

__Step 6__: You can check it out in a browser by visiting <a href="http://localhost:3000">http://localhost:3000</a>



### Cleanup
To close the app, run:
```
docker-compose down
```
To also delete the volumes, run:
```
docker-compose down -v
```