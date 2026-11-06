# Practical Machine Learning course project

The repository contains `report.Rmd` (source), `report.html` (compiled report), `index.html` (identical copy for GitHub Pages), `analyze.py` (reproducible model), `predictions.txt` (20 answers), and `requirements.txt`. The training and test CSVs are downloaded by the script and do not need to be uploaded to GitHub.

To regenerate from this folder, install Python 3 and R. In a terminal:

```bash
python3 -m pip install -r requirements.txt
python3 analyze.py
```

Then in R:

```r
install.packages(c("rmarkdown", "jsonlite"))
rmarkdown::render("report.Rmd")
```

The R Markdown document also runs `analyze.py` when rendered. The local CSVs come from the two course URLs, if absent. The held-out 20 test cases are only used for final predictions, not validation.

For the prediction quiz, paste the 20 lines of `predictions.txt` in order. For peer review, upload the six named files above and this README to GitHub and provide the repository link. The HTML can be opened directly from the downloaded repository. To show it as a web page, enable GitHub Pages for the main branch root; `index.html` is already supplied. GitHub's website upload works; local Git is optional.
