import BeyondChurn, numpy as np

def made_up_three_variable_event_stream_test():
  data = [1,0,1,1,1,0,2,0,0,1,1,2,1,1,10,3,1,5,2,4,7,0,1,0,0,0,1,0,0,0]
  print('Before: {0}'.format(data))
  print('After: {0}'.format(BeyondChurn.run_analysis(data)))

def constant_single_variable_event_stream_test():
  data = [2, 0, 2, 6, 5, 3, 3, 1, 0, 2, 2, 3, 5, 1, 4, 2, 4, 5, 3, 2, 
          4, 2, 1, 4, 2, 4, 2, 4, 0, 2, 3, 4, 4, 6, 1, 1, 3, 3, 1, 3, 
          1, 2, 1, 1, 6, 3, 3, 1, 2, 5]
  print('Before: {0}'.format(data))
  print('After: {0}'.format(BeyondChurn.run_analysis(data)))

def two_variable_event_stream_test():
  data = [2, 1, 1, 1, 1, 3, 3, 2, 1, 2, 3, 0, 0, 1, 6, 0, 2, 3, 2, 1, 2, 2, 2, 
          3, 3, 3, 0, 2, 3, 0, 3, 6, 2, 3, 1, 0, 0, 2, 1, 8, 6, 6, 3, 4, 7, 3, 
          6, 3, 10, 8, 6, 3, 0, 9, 4, 4, 2, 9, 6, 3, 6, 6, 1, 4, 8, 5, 6, 8, 5, 
          3, 3, 6, 9, 5, 8, 8, 7, 4, 5, 8]
  print('Before: {0}'.format(data))
  print('After: {0}'.format(BeyondChurn.run_analysis(data)))

def random_three_variable_event_stream_test():
  data = list(np.random.poisson(2, size=40)) + \
         list(np.random.poisson(6, size=40)) + \
         list(np.random.poisson(2, size=40))
  print('Before: {0}'.format(data))
  print('After: {0}'.format(BeyondChurn.run_analysis(data)))

print('Running made_up_three_variable_event_stream_test')
made_up_three_variable_event_stream_test()

print('Running constant_single_variable_event_stream_test')
constant_single_variable_event_stream_test()

print('Running two_variable_event_stream_test')
two_variable_event_stream_test()

print('Running random_three_variable_event_stream_test')
random_three_variable_event_stream_test()









