WordPress on EC2 linux and RDS


Launch EC2 Instance
1.Choose EC2 from AWS.
2. You have to create an instance.
3. Select Amazon Linux AMI(64-bit). 
4. Choose Free tier for the instance type.
5. For the security group, I choose SSH for type, Source anywhere.
6. Go into review sheet to double check everything and launch instance, and download the key pair. (***.pem)

Create a RDS
1.Go to EC2 and Create security group from AWS.
2.Add a all traffic rule in inbound rule, destination choose anywhere. 
3.Go to RDS from AWS.
4.Choose the Standard Create as a database creation method.
5.Engine options select MySQL.
6.I used “Genghua” as my master username.
7.I type my own master password.
8.Select Yes in Publicly accessible in Connectivity.
9.Existing VPC security groups chooses default and the one I just created
from security group.
10.Check everything and then create database.
11.Open MySQL Workbench.
12.Add a MySQL connection
13.Hostname corresponding to RDS endpoint.
14.Username corresponding to master username.
15.Port 3306
16.Password corresponding to master password.
17.After get into work page create a table call WordePress
18.Add two columns, word(CHAR(255)) and count(INT)

MapReduce
1.Open terminal and find out where the pem file is
2.Type ssh -i <***.pem> ec2-user@<Public IPv4 DNS>(ssh -i labhw.pem ec2-user@ec2-35-175-250-179.compute-1.amazonaws.com)
3.Go to  https://www.gutenberg.org/ and find out ht “The Jungle Book By Rudyard Kipling”.
4.Get the link of the book.
5.Back to terminal and type wget <link>
6.Use mv to change the name of book: mv 75-0.txt hw.txt
7.Create a python file call map to mapping the data: nano map.py
8.Create a python file call reduce to reducing the data from map: nano reduce.py
9.Create a python file call sql to connect the result to MySQL: nano sql.py
10.Type <cat hw.txt | python map.py | sort | python reduce.py | python sql.py>, it will start to upload the result to database.