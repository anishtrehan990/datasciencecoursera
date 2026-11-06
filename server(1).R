library(shiny)

# Fit once using R's built-in car data.
model <- lm(mpg ~ hp + am, data = mtcars)

shinyServer(function(input, output) {
  estimated_mpg <- reactive({
    predict(model, newdata = data.frame(hp = input$hp,
                                        am = as.numeric(input$am)))[[1]]
  })

  output$estimate <- renderText({
    paste("Estimated fuel economy:", round(estimated_mpg(), 1), "MPG")
  })

  output$comparison <- renderPlot({
    plot(mtcars$hp, mtcars$mpg, pch = 19, col = "gray50",
         xlim = c(50, 350), ylim = c(0, 40),
         xlab = "Horsepower", ylab = "Miles per gallon (MPG)",
         main = "Estimate compared with the sample cars")
    points(input$hp, estimated_mpg(), pch = 19, col = "red", cex = 1.7)
    legend("topright", legend = c("Sample cars", "Your estimate"),
           col = c("gray50", "red"), pch = 19, bty = "n")
  })
})
