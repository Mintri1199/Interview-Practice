
class ListNode {
    var val: Int?
    var next: AnyObject?
    init(value: Int) {
        self.val = value
        self.next = nil
    }
}

class Solution {

    func mergeLinkedList(list: [[Int]]) -> [Int] {
        var done = false
        var copyList = list
        var smallestValue: (Int, Int)? = nil
        var resultList: [Int] = []
        while !done{
            smallestValue = nil  // tuple (index, value)

            for (index , value) in copyList.enumerated() {
                if smallestValue == nil {
                    smallestValue = (index, value[0])
                } else if value[0] < smallestValue!.1{
                    smallestValue = (index, value[0])
                }
            }

            resultList.append(smallestValue!.1)
            copyList[smallestValue!.0].removeFirst()

            if copyList[smallestValue!.0].isEmpty {
                copyList.remove(at: smallestValue!.0)
            }

            if copyList.count == 0 {
                done = true
            }
        }
        return resultList
    }

    func mergeLinkedListInout(list: inout [[Int]]) -> [Int] {
        var done = false
        var smallestValue: (Int, Int)? = nil
        var resultList: [Int] = []
        while !done{
            smallestValue = nil  // tuple (index, value)

            for (index , value) in list.enumerated() {
                if smallestValue == nil {
                    smallestValue = (index, value[0])
                } else if value[0] < smallestValue!.1{
                    smallestValue = (index, value[0])
                }
            }

            resultList.append(smallestValue!.1)
            list[smallestValue!.0].removeFirst()

            if list[smallestValue!.0].isEmpty {
                list.remove(at: smallestValue!.0)
            }

            if list.count == 0 {
                done = true
            }
        }
        return resultList
    }

}
let listOne = [1, 4, 5]
let listTwo = [1, 3, 4]
let listThree = [2, 6]

var listOfLists = [listOne, listTwo, listThree]

let solution = Solution()
//print(solution.mergeLinkedList(list: listOfLists))
print(solution.mergeLinkedListInout(list: &listOfLists))