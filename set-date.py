#!/usr/bin/env python
import os
import os.path
import re

# A directory where the post files are stored
post_dir = "posts"

# A format string for the front matter to be output
front_matter = """---
date: %s
---

"""

# A regex that matches the existing front matter to be replaced
front_matter_regex = re.compile(
    r"""
^
(?:
  ---\s*?
  (?:\n.*?)*?
  \n---\s*?
  (?:\n+|$)
)?
""",
    re.VERBOSE,
)

# A format string for the command to get the creation date of a post file
date_command = "TZ=UTC0 git log --date=iso-local --format='%%cd' %s | tail -n 1"

for file in os.listdir(post_dir):
    path = os.path.join(post_dir, file)

    if os.path.isfile(path):
        with open(path, "r") as f:
            content = f.read()

        with open(path, "w") as f:
            date = os.popen(date_command % path).read().rstrip()

            # Insert the front matter at the beginning of a post content (or replace existing front matter)
            content = re.sub(front_matter_regex, front_matter % date, content)

            f.write(content)
