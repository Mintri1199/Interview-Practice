//
//  A Swift implementation of the Dining Philosophers Problem:
//  https://en.wikipedia.org/wiki/Dining_philosophers_problem
//
//
//          P0
//       f3    f0
//     P3        P1
//       f2    f1
//          P2
//
//
//  Sample output:
//      // Initializing
//      Philosopher: 0  left: 0  right: 3
//      Philosopher: 1  left: 1  right: 0
//      Philosopher: 2  left: 2  right: 1
//      Philosopher: 3  left: 3  right: 2
//      // Start with
//      Acquiring lock for Philosopher: 2 Left:2 Right:1
//      Acquiring lock for Philosopher: 3 Left:3 Right:2
//      Acquiring lock for Philosopher: 0 Left:0 Right:3
//      Acquiring lock for Philosopher: 1 Left:1 Right:0
//      Start Eating Philosopher: 2
//      Releasing lock for Philosopher: 2 Left:2 Right:1
//      Acquiring lock for Philosopher: 2 Left:2 Right:1
//      Start Eating Philosopher: 3
//      Start Eating Philosopher: 0
//      Releasing lock for Philosopher: 3 Left:3 Right:2
//      Releasing lock for Philosopher: 0 Left:0 Right:3
//      Acquiring lock for Philosopher: 0 Left:0 Right:3
//      Acquiring lock for Philosopher: 3 Left:3 Right:2
//      Start Eating Philosopher: 2
//      Start Eating Philosopher: 1
//      Releasing lock for Philosopher: 2 Left:2 Right:1
//      Releasing lock for Philosopher: 1 Left:1 Right:0
//      Acquiring lock for Philosopher: 2 Left:2 Right:1
//      Acquiring lock for Philosopher: 1 Left:1 Right:0
//      Start Eating Philosopher: 0
//      Start Eating Philosopher: 3
//      Releasing lock for Philosopher: 0 Left:0 Right:3
//      Releasing lock for Philosopher: 3 Left:3 Right:2
//      Start Eating Philosopher: 2


// Let's start with two philosopher
//      p0
//   f0    f1
//      p1
// p0 should use f0
// p1 should use f1

import Foundation

let numberOfPhils = 5

// total of how many forks there are
let forksSemaphore: [DispatchSemaphore] = Array(repeating: DispatchSemaphore(value: 1), count: numberOfPhils)

struct ForkPair {
    let leftFork: DispatchSemaphore
    let rightFork: DispatchSemaphore
    
    init(leftIndex: Int, rightIndex: Int) {
        leftFork = forksSemaphore[leftIndex]
        rightFork = forksSemaphore[rightIndex]
    }
    
    // Signalling that both forks has been picked up
    func pickUpBothForks() {
        leftFork.wait()
        rightFork.wait()
    }
    
    // Signalling that both forks has been picked up
    func putDownBothForks() {
        leftFork.signal()
        rightFork.signal()
    }
}

struct philosopher {
    
    let philosopherNumber: Int
    let pairOfForks: ForkPair
    
    var leftIndex: Int
    var rightIndex: Int
    
    init(number: Int) {
        leftIndex = number
        rightIndex = number - 1
        
        // edge case for the first philosopher
        // it will have access to the first and last forks
        if rightIndex < 0 {
            rightIndex += numberOfPhils
        }
        
        philosopherNumber = number
        pairOfForks = ForkPair.init(leftIndex: leftIndex, rightIndex: rightIndex)
        
        print("Philosopher \(number) has forks \(leftIndex) and \(rightIndex)")
    }
    
    func eat() {
        while true {
            print("Locking Philosopher \(philosopherNumber) with forks \(leftIndex) and \(rightIndex)")
            pairOfForks.pickUpBothForks()
            sleep(3)
            print("Philoshoper \(philosopherNumber) has done eating.")
            pairOfForks.putDownBothForks()
            print("Releasing the lock on philosopher \(philosopherNumber)")
        }
    }
}

for i in 0 ..< numberOfPhils {
    let phil = philosopher.init(number: i)
    
    DispatchQueue.global().async {
        phil.eat()
    }
}

for semaphore in forksSemaphore {
    semaphore.signal()
}
