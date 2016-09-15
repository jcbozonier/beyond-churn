import numpy as np
import scipy.stats as ss

def find_smallest_credible_hypothesis(hypothesis_probability_pairs):
  hypotheses, probabilities = zip(*hypothesis_probability_pairs)
  cumsum_probabilities= list(reversed(np.array(list(reversed(probabilities))).cumsum()))
  cumsum_hypothesis_probabilities = list(zip(hypotheses, cumsum_probabilities))
  for cumsum_hypothesis_probability in cumsum_hypothesis_probabilities:
    if cumsum_hypothesis_probability[1] <= .975:
      most_likely_smallest_hypothesis = cumsum_hypothesis_probability[0]
      break
  return most_likely_smallest_hypothesis

def find_largest_credible_hypothesis(hypothesis_probability_pairs):
  hypotheses, probabilities = zip(*hypothesis_probability_pairs)
  cumsum_probabilities= list(np.array(list(probabilities)).cumsum())
  cumsum_hypothesis_probabilities = list(zip(hypotheses, cumsum_probabilities))
  for cumsum_hypothesis_probability in cumsum_hypothesis_probabilities:
    if cumsum_hypothesis_probability[1] >= .975:
      most_likely_largest_hypothesis = cumsum_hypothesis_probability[0]
      break
  return most_likely_largest_hypothesis

def find_credible_interval(hypothesis_probability_pairs):
  return (find_smallest_credible_hypothesis(hypothesis_probability_pairs),
          find_largest_credible_hypothesis(hypothesis_probability_pairs))


def compute_hypothesis_probabilities(event_counts):
  hypotheses = np.linspace(start=0.1, stop=100, num=1000)
  current_probabilities = np.ones(len(hypotheses))/np.ones(len(hypotheses)).sum()
  for event_count in event_counts:
    unnormalized_hypothesis_probabilities = ss.poisson.pmf(event_count, hypotheses)
    normalized_hypothesis_probabilities = unnormalized_hypothesis_probabilities / unnormalized_hypothesis_probabilities.sum()
    current_probabilities *= normalized_hypothesis_probabilities
    current_probabilities = current_probabilities / current_probabilities.sum()
  return list(zip(hypotheses, current_probabilities))
    
def find_breaking_point(event_count_series):
  epoch_count = len(event_count_series)
  for i in range(1, epoch_count-1):
    # split data into pre and post window
    pre_window = event_count_series[:i]
    post_window = event_count_series[i:]
    # test for change
    if not windows_are_similar(pre_window, post_window):
      return pre_window, post_window #(i, np.mean(pre_window), np.mean(post_window))
  return None

def windows_are_similar(pre_window, post_window):
  pre_window_hypothesis_probabilities = compute_hypothesis_probabilities(pre_window)
  post_window_hypothesis_probabilities = compute_hypothesis_probabilities(post_window)

  pre_window_credibility_interval = find_credible_interval(pre_window_hypothesis_probabilities)
  post_window_credibility_interval = find_credible_interval(post_window_hypothesis_probabilities)
    
  return (post_window_credibility_interval[0] <= pre_window_credibility_interval[1] and post_window_credibility_interval[0] >= pre_window_credibility_interval[0]) or \
         (pre_window_credibility_interval[0] <= post_window_credibility_interval[1] and pre_window_credibility_interval[0] >= post_window_credibility_interval[0])

def do_dynamic_window_partition(arbitrary_window):
  result = find_breaking_point(arbitrary_window)
  if result is None:
    return [arbitrary_window,]
  else:
    #print(result[1])
    return [result[0],] + do_dynamic_window_partition(result[1])

def reverse_aggregated_partition_list(partitions):
    reversed_partition_list = list(reversed(partitions))
    aggregated_partition_list = []

    current_partition = reversed_partition_list[0]
    for i in range(len(reversed_partition_list)):
      if i+1 >= len(reversed_partition_list):
        aggregated_partition_list.append(current_partition)
        break
      else:
        next_partition = reversed_partition_list[i + 1]
        should_merge = windows_are_similar(current_partition, next_partition)
        if should_merge:
          # reversed order in append because we're in backwards land
          current_partition = next_partition + current_partition
        else:
          aggregated_partition_list.append(current_partition)
          current_partition = next_partition
    return list(reversed(aggregated_partition_list))

def run_analysis(event_counts):
  partitions = do_dynamic_window_partition(event_counts)
  return reverse_aggregated_partition_list(partitions)
