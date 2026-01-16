def sequence(tup):
  if len(tup) < 2:
    return tup

 
  common_difference = tup[1] - tup[0]
  
  # 3. Start generating terms from the last element of the original tuple.
  last_term = tup[-1]
  
  # Use a list to store the new elements since tuples are immutable.
  next_three = []
  
  # 4. Generate the next three terms.
  for _ in range(3):
    # Calculate the next term by adding the common difference
    next_term = last_term + common_difference
    
    # Add the new term to our list
    next_three.append(next_term)
    
    # Update the last_term for the next iteration
    last_term = next_term 
    
  # 5. Return the whole sequence by concatenating the original tuple 
  # with the new elements converted into a tuple.
  return tup + tuple(next_three)

