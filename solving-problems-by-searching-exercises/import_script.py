
# Already implemented code from the online repository will be used. The following code imports all from search.py
import httpimport
with httpimport.github_repo('aimacode', 'aima-python', ['utils', 'search'], 'master'):
    from search import *