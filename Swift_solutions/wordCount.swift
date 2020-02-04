// Exercism Exercise: Word Count
// Given a phrase, count the occurrences of each word in that phrase.
// For example for the input "olly olly in come free"

// Example output:

// olly: 2
// in: 1
// come: 1
// free: 1

// Ok, so I think a way to do this is to create a Histogram / Multiset
// This data structure is prefer since the it keep track of the occurence of
// unique keys.

// So our histogram would look like this
// Dictionary{ uniqueWord: occurence }

// Some edge cases we have to consider are
// a empty string,
// invalid input (anything that is not a string)
// non-alpha string (a string of numbers)

// For the sake of simplicity, I will return a nil value for bad inputs and edge case inputs

func getWordCount(text: String) -> [String : Int]? {
  // Cover empty string edge case
  if text.isEmpty {  // O(1)
    return nil  // O(1)
  }
  // Initialize our histogram
  var histogram: [String : Int] = [:]  // O(1)

  // Split our text input into an array of substring
  let wordArray = text.split(separator: " ")  // O(n) where n is the length of the text

  // Loop through the array and build our histogram
  wordArray.forEach { (substring) in  // O(w) where w is the number of words
    // Change substring into string
    let word = String(substring)  // O(1)
    // Increment the value if the word exist
    // If not then give it default value of 0 and increment it
    histogram[word, default: 0] += 1  // O(1)
  }
  return histogram
}

// Time: O(n) + O(w) = O(n)
// Space: O(w) + O(set(w)) where w is the number of words

let example = "olly olly in come free"

let resultHistogram = getWordCount(text: example)

//if let result = resultHistogram {
//  result.forEach({ (word, occurence) in
//    print(word + ": " + "\(occurence)")
//  })
//}

// This solution is pretty good but it could be improve
// A way that we could improve this is populating the histogram as we spliting
// the word instead of having an array to store the words first

func betterGetWordCount(text: String) -> [String : Int]? {
  // Cover empty string edge case
  if text.isEmpty {  // O(1)
    return nil  // O(1)
  }
  // Initialize our histogram
  var histogram: [String : Int] = [:]  // O(1)

  // initialize a variable to keep track at our current word
  var currentWord: String = ""  // O(1)

  for character in text {  // O(n) where n is the number of character
    // Convert into string
    let strCharacter = String(character)  // O(1)

    if strCharacter == " " && currentWord.isEmpty == false {   // O(1)
      histogram[currentWord, default: 0] += 1  // O(1)
      currentWord = ""  // O(1)
    } else if !strCharacter.isEmpty {  // O(1)
      // Add the character to the current word
      currentWord += strCharacter  // O(1)
    }
  }
  return histogram  // O(1)
}
// Time: O(n)
// Space: O(w) where w is the number of unique words

let result = betterGetWordCount(text: example)

if let result = result {
  result.forEach { (word, occurence) in
    print(word + ": " + "\(occurence)")
  }
}
