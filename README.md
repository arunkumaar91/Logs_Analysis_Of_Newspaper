## Logs_Analysis_Of_Newspaper

### Project Overview

Built an **internal reporting tool** that will use information from the database **to discover what kind of articles the site's readers like and wish to read**. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loads a web page.

### Software Requirements

- [Python](https://www.python.org/downloads/).

- [VirtualBox](https://www.virtualbox.org/). Virtual Box Software Runs the Virtual Machine

- [Vagrant](https://www.vagrantup.com/downloads.html). Vagrant software configures the VM and lets you share files between your host computer and the VM's filesystem.

### Installation

1. Install VirtualBox and Vagrant.
2. To check vagrant is successfully installed, on your terminal type vagrant --version
3. Next clone [vagrant](https://github.com/udacity/fullstack-nanodegree-vm) repository
4. Download the Data File [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and copy it to the vagrant directory.
5. Copy the content of this current repository into the vagrant direcotry by either cloning or downloading it.

### To Launch Vagrant and import newsdata.sql to vagrant directory

- In the command Prompt, change the directory to vagrant (Where you cloned the vagrant repository)
- Run the Command, vagrant up
- Next, run the command vagrant ssh to login to the newly installed Linux VM.
- Unzip the data file and copy the newsdata.sql file to the vagrant directory
- To Load the newsdata, use the command `psql -d news -f newsdata.sql`
- Type `psql -d news` to connect to news database.

The database news contains three tables:

- Authors table.
- Article table.
- Log table.

### Creating Views

Create reqerrors view using below query

`create view reqerrors as
select to_char(l.time,'FMMonth FMDD FMYYYY') as date, cast(count(l.status) as float) as errors
from log l where status != '200 OK'
group by date
order by errors desc;`

Create reqtotal view using below query

`create view reqtotal as
select to_char(l.time,'FMMonth FMDD FMYYYY') as date, cast(count(l.status) as float) as sum
from log l
group by date
order by sum desc;`

create calc view using below query

`create view calc as
select re.date, ((re.errors/rt.sum) * 100) as percentage
from reqerrors re, reqtotal rt
where rt.date = re.date
order by percentage desc;`


### Running the Python Script

From the terminal, inside the vagrant directory run the file LogsAnalysis.py. Use the below command to run the file

$`python LogsAnalysis.py`   

### License

- Python license is administered by **Python Software Foundation (PSF)**
- Vagrant license provided by **HarshiCorp**
- VirtualBox license provided by **Oracle**
