What is CMS?

CMS, or Covid Management System, is a sophisticated solution designed for storing, updating, viewing, and representing data related to Covid patients and the dedicated medical staff. The system leverages a Python code seamlessly integrated with MySQL.

To set up CMS in your local environment, follow these steps:

1. Clone the repository into your local environment using the command: `git clone https://github.com/imkkapoor/Covid-Management-System.git`
2. Open the CMS.py file and update the MySQL connector parameters, including host, user, database, and passwd, to align with your local environment.
3. Ensure you have installed all the necessary dependencies: pandas, mysql-connector, and matplotlib. Use the following commands:
   - `pip install pandas`
   - `pip install mysql-connector-python`
   - `pip install matplotlib`
4. Create the required structured tables, as outlined in the provided PDF ([data structure of MySQL tables.pdf](data%20structure%20of%20MySQL%20tables.pdf)), in the designated database. Here are the commands:
   - `CREATE TABLE staff (id INT(7) UNIQUE, name CHAR(40), age INT(3), gender CHAR(3), area CHAR(40), joining_date DATE, post CHAR(40), salary INT(10));`
   - `CREATE TABLE patient (id INT(7) UNIQUE, name CHAR(40), age INT(3), gender CHAR(2), area VARCHAR(40), detection_date DATE);`
5. With these steps completed, you are ready to input sample data and start utilizing the system. Best of luck!
