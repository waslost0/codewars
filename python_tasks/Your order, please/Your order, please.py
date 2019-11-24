def order(sentence):
  if not sentence:
      return ""
      
  result = []
  s_list = sentence.split()
  
  for i in range(1, len(s_list) + 1):
      for word in s_list:
          if str(i) in word:
              result.append(word)              
              break

  return ' '.join(result)