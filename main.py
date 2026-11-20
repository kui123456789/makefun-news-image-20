# A news-image-daily entry (Python 3.13, standard library only): the image is the
# entry.png beside this file, and the program copies it to /output/entry.png.
# The image sums up the world news of Friday 20 November 2026 and was drawn
# by draw.py (Pillow, run at build time, not at grading time) from a generated
# hero illustration (hero.png) and six verified news stories.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png"),
    os.path.join(out_dir, "entry.png"),
)
