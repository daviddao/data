# Data from experiments

## Experiments
- Random Sampling Dataset: Randomly selected 16730 trees from STBase using equipartition (250 Iterations using RF Opt)
- Worst Case Dataset: 16730 trees from STBase with average RF-Score of 1.0 (1 Iteration, 250 Iterations and 500 Iterations)
- Synthetic Rogue: Dummy data set with a Rogue Taxon (E) in an otherwise identical small tree dataset
- Random Rogue: Randomly introduced an X Taxon into a tree set with (otherwise) average RF-Score of 0.0 (comprehensive topology)
- Rogue Detection: Example Dataset from RogueNaRok (Comparision with Andres Algorithm as Screenshot)

## Plots
- Comparision 250 Iterations (Worst Case Dataset vs. Random Data Set)
- Histogramm of RF distances in Worst Case Dataset after (50, 100, 150, ..., 500 Iterations)

## Scripts
- Used to generate plots

## Results 
- Multiple iterations yield much better than single iteration
- Works best in worst case dataset
- Possible to identify rogue taxa (when metric is RF distance)
- Slow (due to Python Implementation)
