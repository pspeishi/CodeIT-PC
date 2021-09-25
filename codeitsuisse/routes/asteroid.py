import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluateAsteroid():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    result=[]
    for test_case in data['test_cases']:
        result.append(asteroid(test_case))
    logging.info("My result :{}".format(result))
    return jsonify(result)


# "AAABBCC" -> ['AAA','BB','CC']
def groupedArray(our_input):
  n = len(our_input)
  grouped_array = []

  curr_count = 1
  prev_asteroid = our_input[0]
  for i in range(1, n):
      curr = our_input[i]
      if curr == prev_asteroid:
          curr_count += 1
      else:
          curr_group = prev_asteroid*curr_count
          grouped_array.append(curr_group)
          prev_asteroid = curr
          curr_count = 1
  curr_group = prev_asteroid*curr_count
  grouped_array.append(curr_group)
  return grouped_array

# Create dict of alphabet count
def alphabet_dict(our_input):
  our_dict={}
  for asteroid in our_input:
    if asteroid in our_dict.keys():
      curr_count = our_dict[asteroid]
      curr_count += 1
      our_dict.update({asteroid: curr_count})
    else:
      our_dict[asteroid]=1
  return our_dict

def countScore(our_dict):
    count = 0
    for key,value in our_dict.items():
        if value >= 10:
            count += (value * 2)


        elif value >= 7 and value < 10:

            count += (value * 1.5)

        elif value <= 6:
            count += value
    return round(count)


def findOrigin(array):
    arrayIndex = 0
    originCount = -1
    arrayIndex = len(array) // 2

    for i in range(int(arrayIndex)):
            originCount += len(array[i])

    originCount += (len(array[arrayIndex]) // 2) + 1

    return originCount

def asteroid(inputValue):
    score = countScore(alphabet_dict(inputValue))
    origin = findOrigin(groupedArray(inputValue))
    output = {}
    output["input"] = inputValue
    output["score"] = score
    output["origin"] = origin
    return output

