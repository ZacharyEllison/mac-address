# mac-address

## On the Solution

I started with a dockerfile and worked iteratively

- a `.env` helps to keep the api key that `macaddress.io` requires local
  - It's included in the repo but also in the `.gitignore` so changes aren't pushed by devs
- This being a simple script I made only the one `main.py`
- The address the user provides is cleaned my making sure the characters are alphanumeric or a `'.'` 
  - I made this part intending to expand and support `'-'` in the future
- I defaulted the api to return the vendor information in text in the command line, usable by the user by copying
- I provided the option for the return type to be any of those provided by the api written to a file `mac-address.{file_type}`
  - These files are included in the `.gitignore` for safety as well so they cannot be pushed to the repo


## To Run

1. Copy `.env.example` into a new file `.env` and fill out your API_KEY

2. Build the docker container with the following command

    `docker build . -t api-test`

3. Run the docker image interactively with the following command

    `docker run -it api-test`
