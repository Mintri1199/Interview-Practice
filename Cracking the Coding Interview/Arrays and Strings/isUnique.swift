// Implement an algorithm to determine if a string has all unique characters. 
// What if you cannot use additional data structures?
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


// print(isUnique(input: exampleFalse))
// print(isUnique(input: exampleTrue))

print(isUniqueSlow(input: exampleTrue))
