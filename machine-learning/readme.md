Machine Learning dev environment

My current dev workflow has gone through a few revisions over the last few months.
I used **Docker** for my initial attempt in order to isolate work environments.
However, this proved unfeasible due to moving files between the docker and local environments.

My current strategy is to:

1. use pipenv with pyenv for workspace isolation.
1. use `jupytext` to convert between a `.py` file and `.ipynb`
1. run a managed jupyter server from PyCharm (seems to work better with PyCharm)
1. write, execute, and debug code with PyCharm in the `.py` file
1. switch to jupyter lab for better visuals

