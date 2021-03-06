func binarySearch(array: [Int], target: Int) -> Int? {
  var startingPoint = 0
  var endPoint = array.count - 1

  while endPoint >= startingPoint {
    // The middle index of the array if the average of two end points
    let middleIndex = abs((startingPoint + endPoint) / 2)

    if array[middleIndex] == target{
      return middleIndex
    } else if array[middleIndex] > target {
      endPoint = middleIndex - 1
    } else {
      startingPoint = middleIndex + 1
    }
  }
  return nil
}


let array = [0,1,2,3,4,5,6,7,8]
print(binarySearch(array: array, target: 2))