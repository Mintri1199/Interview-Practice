import UIKit

func NucleotideCount(strand: String) -> [String : Int] {
  var nucleotideDict = ["T": 0, "A": 0, "C": 0, "G": 0]
  for character in strand {
    if let occ = nucleotideDict[String(character)] {
      nucleotideDict[String(character)] = occ + 1
    }
  }
  return nucleotideDict
}
