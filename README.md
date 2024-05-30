# RKI interview challenge

Welcome to this RKI python interview challenge. We are building a small API to help us
with our interview process, but we need your help finishing it.

The checklists below will guide you through the setup of the project and give you a few
small tasks to work on for yourself. Some of the steps may require some online research.

Should you have any questions during the process, please feel free to contact your
interviewers at any time. It's always better to ask, then to get stuck.

## setup and installation
- [x] find this readme file and follow the check-list
- [ ] clone this git repository to your local machine
- [ ] create a new python virtual environment
- [ ] install this project in the new environment

## running and testing
- [ ] start the server with the `interview` command
- [ ] take a look at the api documentation http://127.0.0.1:8000/docs
- [ ] click on the "GET candidates" endpoint, then "Try it out" and "Execute"
- [ ] you should now see a response from the server with a JSON body

## finally, your tasks
- [ ] add your favorite (fictional) interview candidate to the `dummy_database`
- [ ] create a new optional field on the `Candidate` model for `birthday`
- [ ] run the tests with the `pytest` command and ensure they pass
- [ ] bonus task: create a `POST` endpoint to add new candidates to the `dummy_database`
