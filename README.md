# Show me some COMMITment

This is a tool that uses Natural Language Processing to detect nonsense in commit messages. It employs a Bag-of-Words model with scikit-learn's Logistic Regression to predict whether a commit message is minimally explicative. A Git hook is then used to block messages that don't meet the minimum requirements.

Here’s what you need to know before using this tool:

## Data Collection and Categorization

I used the Python script located at `analysis/commit_analysis.py`, which utilizes the GitHub API to collect commit message data from a few repositories—mostly from freshman students' projects. It generated about 1,000 lines of data, which I then manually categorized.

## Model Creation and Analysis

I applied a Bag-of-Words approach combined with Logistic Regression to predict whether a message meets minimal standards. I used the `recall` metric for evaluation and a confusion matrix to check for class imbalance.

Throughout this process, I had to return and collect additional data several times due to imbalance issues. Once finalized, I saved the model parameters as a pickle file.

## Git Hook

The script `install_hooks.sh` installs the Git hook into the current repository. To do so, simply run the following command in Git Bash:

```
bash install_hooks.sh
```

This script makes the `commit-msg` file (located at `scripts/hooks/commit-msg`) executable and places it in the hidden `.git/hooks` directory.

The `commit-msg` script invokes the Python program `commit_check.py`, which reads the current commit message, loads the model parameters from the pickle file, and categorizes the message. If the result is negative, the commit is blocked and the following error message is shown:

```
[X] Commit blocked: message classified as invalid.
Please write a clearer or more meaningful commit message.
```