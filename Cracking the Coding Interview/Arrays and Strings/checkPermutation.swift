// Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

// Using list of character occurences if the string all character ascii
func asciiPermutation(for input: String, comparator: String) -> Bool {
    guard input.count == comparator.count else {
        return false
    }

    var charOccurences = Array(repeating: 0, count: 128)

    comparator.forEach { char in
        charOccurences[Int(char.asciiValue!)] += 1
    }

    input.forEach { char in
        charOccurences[Int(char.asciiValue!)] -= 1
    }
    
    return !charOccurences.contains(where: { $0 > 0 || $0 < 0 })
}

// Using sort
func sortPermutation(for input: String, with comparator: String) -> Bool {
    guard input.count == comparator.count else { return false }
    return input.sorted() == comparator.sorted()
}

let comparatorString = "apple"
let trueString = "leppa"
let falseString = "asdfe"
let quickBreak = "as"

print(sortPermutation(for: trueString, with: comparatorString))
