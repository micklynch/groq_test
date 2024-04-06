# Description
Simple repo to play with Groq.com and assess the prediction speeds.

# Set-up
Clone this repo by typing to following into your terminal:
```
$ git clone https://github.com/micklynch/groq_test.git
```

## Dependencies
To set up the environment, I am using [Poetry](https://python-poetry.org/). You can find the instructions on how to install it [here](https://python-poetry.org/docs/#installation).

Once you have it installed, you can get the project dependencies by running:
```
poetry install
```
Then open an poetry shell by running:
```
poetry shell
```

## Environmental Variables
Copy the `.env.template` file to `.env`.

Replace the `GROQ_API_KEY` with one that you get from GROQ. To create a Groq API key, visit https://console.groq.com/keys and generate a new key.

## Run
Run the code by typing:
```
python main.py
```
Watch the response come back super fast! ⚡⚡⚡

Edit the file to change the prompt.
