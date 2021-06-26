// Implement an algorithm to determine if a string has all unique characters. 
// What if you cannot use additional data structures?
import Foundation

let exampleFalse = "azxzvba"
let exampleTrue = "asdfg"


func isUnique(input: String) -> Bool {
    var characterSet = Set<Character>()

    for character in input {
        if characterSet.contains(character) {
            return false
        }

        characterSet.insert(character)
    }

    return true
}

func isUniqueSlow(input: String) -> Bool {
    var compareString = ""

    for character in input {
        if compareString.contains(character) {
            return false
        } 
        compareString = compareString + [character]
    }

    return true
}

// Solution suggested by book 
func isUniqueASCII(input: String) -> Bool {
    var arr = Array(repeating: false, count: 128)
    for character in input {
        let value = Int(character.asciiValue!)
        if arr[value] {
            return false
        }
        arr[value] = true
    }
    return true
}

// Slow solution suggested by book
func isUniqueSlowBook(input: String) -> Bool {
    
    // sort the string
    var prevChar = Character(" ")
    let sortedStr = input.sorted()

    for char in sortedStr {
        if prevChar == char {
            return false
        }
        prevChar = char
    }

    return true
}

print(isUniqueSlowBook(input: exampleTrue))
