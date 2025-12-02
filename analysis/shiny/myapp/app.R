library(shiny)
library(airway)
library(ggplot2)

# Load data from Bioconductor (in memory, no local file)
data(airway)
exprs_data <- assay(airway)
genes <- rownames(exprs_data)

ui <- fluidPage(
  titlePanel("Airway RNA-seq Explorer"),
  sidebarLayout(
    sidebarPanel(
      selectInput("gene", "Select gene:", choices = genes, selected = genes[1])
    ),
    mainPanel(
      plotOutput("genePlot")
    )
  )
)

server <- function(input, output) {
  output$genePlot <- renderPlot({
    gene_expr <- exprs_data[input$gene, ]
    df <- data.frame(Sample = colnames(exprs_data), Expression = gene_expr)
    ggplot(df, aes(x = Sample, y = Expression)) +
      geom_bar(stat="identity", fill="steelblue") +
      theme_minimal() +
      ylab("Expression") +
      xlab("Sample")
  })
}

shinyApp(ui, server)

