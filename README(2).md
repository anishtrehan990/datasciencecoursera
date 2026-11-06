# Car Fuel Economy Estimate

## Run the app

Put `ui.R` and `server.R` in the same folder. Install R and the `shiny` package, then open that folder as an RStudio project or run:

```r
install.packages("shiny")
shiny::runApp("path/to/shiny-pitch")
```

Choose horsepower with the slider and automatic or manual transmission with the buttons. The estimated MPG and chart update immediately. The app uses R's built-in `mtcars` data, so there is no data file to install. Instructions are also displayed within the app itself.

## Render the pitch

Open `pitch.Rpres` in RStudio and click **Preview**. RStudio Presenter executes the R chunk and creates the five-slide HTML presentation. Replace the placeholder name and app URL before publishing.

## Publish

Connect RStudio to your shinyapps.io account, then use **Publish** while the app is running, or run `rsconnect::deployApp("path/to/shiny-pitch")` after installing `rsconnect`. Copy the resulting app URL for the first assignment box.

Preview `pitch.Rpres`, then use RStudio's **Publish** button to publish the presentation to RPubs. Copy that public presentation URL for the second box. Upload `ui.R`, `server.R`, `pitch.Rpres`, and this README to a GitHub repository. You can upload these small files through GitHub's **Add file → Upload files** page; local Git is optional.
