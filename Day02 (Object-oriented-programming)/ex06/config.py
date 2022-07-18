NUM_OF_STEP = 3

INPUT_FILE = 'data.csv'

OUTPUT_FILE = 'report'

HAS_HEADER = True

MESSAGE_SUCCESS = 'The report has been successfully created'

MESSAGE_FAIL = 'The report hasn’t been created due to an error'

WEB_HOOK_URL = 'https://hooks.slack.com/services/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'

REPORT = """Report
We have made {} observations of tossing a coin: {} of them were tails and {} of them were heads.\
The probabilities are {}% and {}%, respectively. \
Our forecast is that in the next {} observations we will have: {} tail and {} heads."""
