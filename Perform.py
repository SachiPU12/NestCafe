import cProfile
import re

if __name__ == "__main__":
    cProfile.run('re.compile("foo|bar")')
