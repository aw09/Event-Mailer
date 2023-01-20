# Event Mailer 

Send schedule email using python

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* python >= 3.9.5
* virtualenv / venv
* pip3
* google account


### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/aw09/Event-Mailer.git
   cd Event-Mailer
   ```
2. Create and activate virtualenv
    ```
    virtualenv venv
    ./venv/Scripts/activate
    ```
3. Install library
   ```python
   pip install -r requirements.txt
   ```
### Setting Environment Variables
1. Copy or rename .env.example to .env
2. Change SENDER_EMAIL with your google email
3. You can leave the other

### Setting Google Account
1. Login to your google account
2. Go to [GCP Dashboard](https://console.cloud.google.com/apis/dashboard)
3. Create a project
4. Go To "OAuth consent screen" Fill tester with your email
5. Go to Credentials, select “Create credentials” and create a new “OAuth client ID”
6. You will be asked which type of app will use this ID, choose “Other” and give it name
7. Your client ID and secret key must show, Download it.
8. Copy that file to project root folder and rename to "oauth.json"
9. Run
    ```
    python ./init_email.py
    ```
9. It will ask your email, fill it
10. Then it will generate a link like below, open the link in the browser
    ```
    https://accounts.google.com/o/oauth2/auth?client_id=XXXXXXX
    ```
11. Authorize until you get Authorization code like this
    ```
    4/1AWgavdfAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    ```
12. Copy and paste to the terminal
13. If success, you will send email "Great!" to yourself

## Testing
Run this command for testing
    ```
    pytest
    ```
> Prefer to run tests before you run the project.
Because if you run the project first, the test may fail





<!-- USAGE EXAMPLES -->
## Usage
1. Run project
    ```
    python manage.py
    ```
2. Check Swagger 
    ```
    http://localhost:5000/apidocs
    ```