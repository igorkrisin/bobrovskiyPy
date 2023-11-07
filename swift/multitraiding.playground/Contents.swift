import UIKit


let recursiveLock = NSRecursiveLock()

class RecursiveMutexTest {
    private var mutex = pthread_mutex_t()
    private var attribute = pthread_mutexattr_t()
    
    init() {
        pthread_mutexattr_init(&attribute)
        pthread_mutexattr_settype(&attribute, PTHREAD_MUTEX_RECURSIVE)
        pthread_mutex_init(&mutex, &attribute)
    }
    
    func firstTask() {
        pthread_mutex_lock(&mutex)
        secondTask()
        pthread_mutex_unlock(&mutex)
        defer {
            pthread_mutex_unlock(&mutex)
        }
    }
    
    private func secondTask() {
        pthread_mutex_lock(&mutex)
        print("FINISH")
        defer {
            pthread_mutex_unlock(&mutex)
        }
    }
}

//let recucive = RecursiveMutexTest()

//recucive.firstTask()

let recursiveLock = NSRecursiveLock()

class RecursiveThread: Thread {
    override func main() {
        recursiveLock.lock()
        print("Thread acquired lock")
        callMe()
        defer {
            recursiveLock.unlock()
        }
        print("exit main")
    }
    func callMe() {
        recursiveLock.lock()
        defer {
            recursiveLock.unlock()
        }
        print("exit callMe")
    }
    
}


let thread = RecursiveThread()
thread.start()
