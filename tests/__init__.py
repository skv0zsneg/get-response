import sys
import os

# Insert all packages inside src dir for tests.
PATH_TO_PACKAGE = os.path.join('src')
sys.path.insert(0, PATH_TO_PACKAGE)
