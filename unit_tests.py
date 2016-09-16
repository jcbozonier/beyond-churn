import nose.tools as nt
import BeyondChurn as bc
import numpy as np

def given_data_with_single_significant_bin_test():
  # Given
  first_event_data = [0]*50
  event_rate_hypotheses = bc.compute_hypothesis_probabilities(first_event_data)

  # When finding credible interval
  interval = bc.find_credible_interval(event_rate_hypotheses)
  # Should
  nt.assert_almost_equals(interval[0], 0.1, places=4)
  nt.assert_almost_equals(interval[1], 0.1, places=4)

  # When checking similarity
  self_similar = bc.windows_are_similar(first_event_data, first_event_data)
  # Should
  nt.assert_true(self_similar)

def given_data_with_which_varies_but_centers_on_one_test():
  # Given
  first_event_data = np.random.poisson(1, size=15)
  event_rate_hypotheses = bc.compute_hypothesis_probabilities(first_event_data)
  
  # When finding credibility interval
  interval = bc.find_credible_interval(event_rate_hypotheses)
  # Should
  nt.assert_less_equal(interval[0],1, 'Interval should include the mean rate, 1.')
  nt.assert_greater_equal(interval[1],1, 'Interval should include the mean rate, 1.')
