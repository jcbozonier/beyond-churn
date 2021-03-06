# BeyondChurn
## Why does this exist?

This library can be used to analyze event occurences over time. Think customer orders per month, customer service calls per hour, how many times your dog barks each day, etc. Typically when analyzing events like these we need to specify some arbitrary window of time to analyze. We end up comparing these windows on the data set and look for significant changes in frequency.

I don't like arbitrary.

This library enables one to take a set of event frequency data and will partition the data into windows that are not arbitrary. Windows instead are formed based upon the likelihood of the data to have come from a similar underlying event rate. Where the event rate producing the data seems statistically probable to have changed, the window is partitioned into separate epochs.

## Gimme an example
One of the test cases is a stream of event counts that looks like this:

```
[1, 0, 1, 1, 1, 0, 2, 0, 0, 1, 1, 2, 1, 1, 10, 3, 1, 5, 2, 4, 7, 0, 1, 0, 0, 0, 1, 0, 0, 0]
```

By looking at this, you can see that the middle portion seems to have a higher volume of the event than the two outer portions. Running BeyondChurn.run_analysis on this data yields the following partitions:

1. [1, 0, 1, 1, 1, 0, 2, 0, 0], 
2. [1, 1, 2, 1, 1, 10, 3, 1, 5, 2, 4, 7], 
3. [0, 1, 0, 0, 0, 1, 0, 0, 0]

It has analyzed the data and broken it into partitions that seem consistent with an underlying rate of occurence that is specific to that partition.

## Uses
Mainly data mining and simplification of time series data.