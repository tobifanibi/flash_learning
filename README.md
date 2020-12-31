# Flash Learning
Proposal: We will build a simple flashcard web app using Flask, aimed at incentivizing children in grades K-8 to remain engaged during remote learning. Students will be able to answer flashcard sets by making drawings or typing submissions. Teachers will be able to add new flash card sets to the system and set grade level and subject tags for a particular flashcard set. We are all relatively new in the program without a whole bunch of web development experience, so our primary goal is to work together to have something functional by the end.


<!-- ABOUT THE PROJECT -->
## About The Project

This project originated as a submission idea for the Oregon State Winter 2020 Hackathon, but the authors continued to work on it beyond the time limits of the competition in order to further develop the functionality of the site. 

The project is hosted live on Heroku at https://learn-with-flash.herokuapp.com/

**Note: When loading the hosted Flash Learning website, please be patient as it takes several seconds for the Heroku server to spin up and load the site files.**


### Built With
* [Flask](https://flask.palletsprojects.com/en/1.1.x/): a Python framework for developing web applications. 
* [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/): a Python framework for responsive web styling.
* [SQLAlchemy](https://www.sqlalchemy.org/): a Python package containing a combination of an SQL toolkit and Object Relational Mapper.

Frontend has been built using [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) and [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5). Backend has been built primarily with [Python](https://docs.python.org/3/) with some small scripts written in [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript).

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

In order to make local changes to Flash Learning, you must first have Python and pip installed on your system. If you need assistance installing these prerequisites, see the folowing steps:
* Python is a programming language. Almost all of this project's code base (particularly the backend) is written in Python. Download the latest version of [Python](https://www.python.org/downloads/) and install onto your local machine.

* Pip is the package installer for Python. Once Python is installed, open your local machine's command line and use the following command to utilize Python to install Pip:
```sh
python get-pip.py -g
```

Git is a version control system. In this project, Git is used to clone (copy) the most up-to-date project files from GitHub to your local machine. Download the latest version of [git](https://git-scm.com/download/win) and install on your local machine.


### Installation

1. Open the command line on your local machine.

2. Enter the following command to use Git to clone this repository to your local machine.
```sh
git clone https://https://github.com/team-penguin-hackathon/flash_learning.git
```
3. Create a virtual environment called `env` within your local cloned repository.
```sh
virtualenv env
```
4. Activate the `env` virtual environment.
```sh
env\Scripts\activate.bat
```
5. Enter the following command to use Pip to install this repository's dependencies.
```sh
pip install -r requirements.txt
```
6. To run a local copy of the website on your local execute the `run.py` file.
```sh
python run.py
```
7. On your browser, navigate to `http://localhost:5000/`. This will update to saved changes in your local directory upon refresh.
8. Occasionally, some of the built-in resources (particularly the javascript scripts) of this project do not update when reloading changes made to files. To bypass these errors, reload the web page and bypass the cache. This can be done using the `Shift + left click Reload button` on Firefox or by entering developer mode on Google Chrome and selecting the `Empty Cache and Hard Reload` option.


<!-- USAGE EXAMPLES -->
## Usage

To use Flash Learning, simply navigate to the site hosted on Heroku at https://learn-with-flash.herokuapp.com/


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://https://github.com/team-penguin-hackathon/flash_learning/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Pull any recent upstream changes (`git pull upstream main`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](https://github.com/asa-leholland/{repo-name}/LICENSE.txt) for more information.



<!-- CONTACT -->
## Contact

Have a question about the project? Feel free to contact us.

[Mohamed Al-Hussein](https://github.com/MohamedAl-Hussein) - 45280604+MohamedAl-Hussein@users.noreply.github.com
[Tobi Fanibi](https://github.com/tobifanibi) - 58971180+tobifanibi@users.noreply.github.com
[Asa LeHolland](https://github.com/asa-leholland) - asaleholland@gmail.com


Project Link: [https://github.com/team-penguin-hackathon/flash_learning](https://github.com/team-penguin-hackathon/flash_learning)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [othneildrew](https://github.com/othneildrew) for creating the [template README file](https://github.com/othneildrew/Best-README-Template) that was used as the starting point for the README for this project. 
* [Mark Doughten](https://github.com/markdoughten) for the initial idea and website concept for this project. 




<!-- MARKDOWN LINKS & IMAGES -->
<!-- none at the moment, will add later on -->