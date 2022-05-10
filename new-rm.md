# coding-interview-questions

a repo for coding interview questions.

## Local Setup

1. minimum python version = 3.7 (works with 3.10)
2. create virtualenv
3. `pip install --upgrade pip`
4. `pip install poetry`
5. `poetry install`
6. this also uses pre-commit. I had weird issue with poetry and pre-commit,
   you may need to `pip install pre-commit`
7. `pre-commit install`

the `jarvis-autotest` folder has scripts that run on PRs.  You should be able to
run them locally with no issues


## Adding Questions

**After you add a question, you can run `pytest tests` locally to check if you
have the correct setup.**

create sub-folders that have a README.md that is used for instructions
and a starter module

group by language and title

example:

`python/tdd_log_retrieval/`

inside it should contain

- `starter.py` : required - basic starter code for candidate
- `README.md` : required - candidate instructions
- `SOLUTION.md` : optional - for solution notes
- `solution.py` : optional - for solution code

### accepted languages and formatting

all files follow the pattern of

- (S|s)tarter.<code_suffix>,
- README.md
- (S|s)olution.<code_suffix>,
- SOLUTION.md

the folder that the code is in is snake_case that gets translated to a question title.

```
questions/
└── bash
    └── my_code_question
        ├── README.md
        ├── SOLUTION.md
        ├── solution.sh
        └── starter.sh
```

This will create a question titled "My Code Question" with language "bash" and will write
the contents of those files to the question.

#### Supported languages and their file syntax are:

**Languages that expect capitalized files names _use_ capitalized file names**

- C_PLUS_PLUS: dir -> `c_plus_plus`, file -> `starter.cpp`
- C_SHARP: dir -> `c_sharp`, file -> `Starter.cs`  # Caplitalized!
- JAVA: dir -> `java`, file -> `Starter.java`  # Capitalized!
- JAVASCRIPT: dir -> `javascript`, file -> `starter.js`
- MYSQL: dir -> `mysql`, file -> `starter.sql`
- POSTGRESQL: dir -> `postgresql`, file -> `starter.sql`
- PYTHON_3: dir -> `python`, file -> `starter.py`
- R: dir -> `r_lang`, file -> `starter.R`
- SCALA: dir -> `scala`, file -> `Starter.scala`  # Capitalized!
- TEXT: dir -> `text`, file -> `starter.txt`

Add more languages as needed

## use with coderpad

For now, you are stuck copying changes from repo to coderpad by hand :(

this will need to be updated

## other docs

We have old versions of questions here:

https://datarobot.atlassian.net/wiki/search?text=interview%20questions

https://drive.google.com/drive/u/0/search?q=interview%20questions

and our internal coderpad docs:

https://datarobot.atlassian.net/wiki/spaces/ENG/pages/843022745/Coderpad
