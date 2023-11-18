//import UIKit
//
//
////1Создай кортеж для двух человек с одинаковыми типами данных и параметрами.
////При том одни значения доставай по индексу, а другие — по параметру.
////Пример (для демонстрации задачи, чтобы было понимание, что надо делать):
//
//let petr = (age: 18, name: "Petr", secondName: "Fedorov")
//let fedor = (age: 28, name: "Fedor", secondName: "Petrov")
//
//petr.0
//petr.1
//petr.2
//
//fedor.age
//fedor.name
//fedor.secondName
//
//
////2Создай массив «дни в месяцах» (12 элементов содержащих количество дней в соответствующем месяце). Используя цикл for и этот массив:
//let dayOnMonths: [Int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
//
//
////выведи количество дней в каждом месяце:
//for numberDay in dayOnMonths {
//    print(numberDay)
//}
//
////используй еще один массив с именами месяцев чтобы вывести название месяца + количество дней:
//let monthInYear: [String] = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
//
//print("\n///////  InArray:  //////////\n")
//
//for i in 0..<dayOnMonths.count {
//    print(monthInYear[i], dayOnMonths[i])
//}
//
////сделай тоже самое, но используя массив кортежей с параметрами (имя месяца, количество дней):
//
//let monthTuplesInArray: [(String, Int)] = [(monthInYear[0], dayOnMonths[0]),(monthInYear[1], dayOnMonths[1]), (monthInYear[2], dayOnMonths[2]), (monthInYear[3], dayOnMonths[3]), (monthInYear[4], dayOnMonths[4]), (monthInYear[5], dayOnMonths[5]), (monthInYear[6], dayOnMonths[6]), (monthInYear[7], dayOnMonths[7]), (monthInYear[8], dayOnMonths[8]), (monthInYear[9], dayOnMonths[0]), (monthInYear[10], dayOnMonths[10]), (monthInYear[11], dayOnMonths[11]) ]
//
//print("\n///////  Intuples:  //////////\n")
//
//for (month, day) in monthTuplesInArray {
//    print( month, day)
//}
//
//
////сделай тоже самое, только выведи дни в обратном порядке (порядок в исходном массиве не меняется):
//print("\n///////  Reverse day for month:  //////////\n")
//for i in 0..<dayOnMonths.count {
//   
//    print(monthInYear[i], dayOnMonths[dayOnMonths.count - i - 1])
//}
//
////для произвольно выбранной даты (месяц и день) посчитай количество дней до конца года
////сделал данное задание при помощи функции, в иделе вынести проверку на правильность ввода дня и месяца в отдельные функцию и вернуть Int, ошибки отловить try , но я думаю это слишком будет
//
//print("\n///////  function howManyDayToEndYear:  //////////\n")
//
//func howManyDayToEndYear( _ monthName: String, _ dayInMonth: Int) -> String {
//    
//    let dayOnMonths: [Int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
//    let monthInYear: [String] = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
//    
//    if !monthInYear.contains(monthName) {
//        return "name month is wrong, please try again"
//    
//    }
//    
//    var numberMonthOnArray: Int = 0
//    var howManyDay: Int = 0
//
//    
//    for i in 0..<monthInYear.count {
//        if monthInYear[i] == monthName {
//            numberMonthOnArray = i
//        }
//    }
//    
//    if dayInMonth < 0 || dayInMonth > dayOnMonths[numberMonthOnArray] {
//        return "number day in month is wrong, please try again"
//    }
//    
//    var countWholeMonth: Int = 0
//    
//    if numberMonthOnArray < 12 {
//        countWholeMonth = numberMonthOnArray + 1
//    } else if  numberMonthOnArray == 12 {
//        countWholeMonth = numberMonthOnArray
//    } else {
//        print("error in numberMonthOnArray")
//    }
//    
//    for i in countWholeMonth..<dayOnMonths.count {
//        howManyDay += dayOnMonths[i]
//    }
//    
//    let recentOfMonth = dayOnMonths[numberMonthOnArray] - dayInMonth
//    
//    return String(howManyDay + recentOfMonth)
//}
//
//print(howManyDayToEndYear("January", 1))
//
////3 Создай словарь, как журнал студентов, где имя и фамилия студента это ключ, а оценка за экзамен — значение.
//
//var journal: [String: Int] = ["Иванов": 5, "Петров": 2, "Сидоров": 4, "Васильев": 3]
//
////Повысь студенту оценку за экзамен
//
//journal.updateValue(4, forKey: "Васильев")
////второй вариант изменения значения в словаре
//journal["Сидоров"] = 5
//
////Если оценка положительная (4 или 5) или удовлетворительная (3), то выведи сообщение с поздравлением, отрицательная (1, 2) - отправь на пересдачу
//journal["Иванов"]
//
//// перебор всех студентов с обращением к ним
//for (nameStudent, noteStudent) in journal {
//    if noteStudent >= 3 {
//        print("\(nameStudent) congratulftion")
//    } else {
//        print("\(nameStudent) let's go to exam again")
//    }
//    
//}
//
//// образение к единичному студента
//if let noteStudent = journal["Иванов"] {
//    if(noteStudent >= 3) {
//        print("congratulation")
//    } else {
//        print("let's go to exam again")
//    }
//        }
// 
//
//
//
////Добавь еще несколько студентов — это будут новые одногруппники!
//
//journal["Леонов"] = 3
//journal["Филимонов"] = 4
//
////Удали одного студента — он отчислен
//
//journal["Петров"] = nil
//
//journal
////Посчитай средний балл всей группы по итогам экзамена.
//var summNoteStudents: Int = 0
//
//for noteStudent in journal.values {
//    summNoteStudents += noteStudent
//}
//
//
//let arrangeNote: Float = Float(summNoteStudents) / Float(journal.count)
//print("arange value note for everyone students: \(arrangeNote)")
//
//import Foundation
//
//let headers = [
//  "accept": "application/json",
//  "content-type": "application/json",
//  "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YzU3ZjM5YzZmZTIwODI5ZWI2YmNlMTM2MDZiNDY0NCIsInN1YiI6IjY1NTNiYWRhNjdiNjEzNDVjYjRkMTRlOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.IAgK1q8_QMXaoiEUrFW6PPRc5BXmIqy737FwLJerOPM"
//]
//
//let request = NSMutableURLRequest(url: NSURL(string: "https://api.themoviedb.org/3/account/20705871/watchlist")! as URL,
//                                        cachePolicy: .useProtocolCachePolicy,
//                                    timeoutInterval: 10.0)
//request.httpMethod = "POST"
//request.allHTTPHeaderFields = headers
//
//let session = URLSession.shared
//let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
//  if (error != nil) {
//    print(error as Any)
//  } else {
//    let httpResponse = response as? HTTPURLResponse
//    print(httpResponse)
//  }
//})
//
//dataTask.resume()

//import Foundation
//
//let headers = [
//  "accept": "application/json",
//  "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YzU3ZjM5YzZmZTIwODI5ZWI2YmNlMTM2MDZiNDY0NCIsInN1YiI6IjY1NTNiYWRhNjdiNjEzNDVjYjRkMTRlOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.IAgK1q8_QMXaoiEUrFW6PPRc5BXmIqy737FwLJerOPM"
//]
//
//let request = NSMutableURLRequest(url: NSURL(string: "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1")! as URL,
//                                        cachePolicy: .useProtocolCachePolicy,
//                                    timeoutInterval: 10.0)
//request.httpMethod = "GET"
//request.allHTTPHeaderFields = headers
//
//let session = URLSession.shared
//let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
//  if (error != nil) {
//    print(error as Any)
//  } else {
//    let httpResponse = response as? HTTPURLResponse
//    print(httpResponse)
//  }
//})
//
//dataTask.resume()


import Foundation

// Структура для хранения данных о фильме
struct Movie: Codable {
    let title: String
    let releaseDate: String
    // Другие необходимые свойства
}

// Функция для загрузки данных с API TMDb
func fetchMovies(completion: @escaping ([Movie]?) -> Void) {
    // Замените YOUR_API_KEY на ваш реальный ключ API TMDb
    let apiKey = "5c57f39c6fe20829eb6bce13606b4644"
    let urlString = "https://api.themoviedb.org/3/discover/movie?api_key=\(apiKey)"
    
    guard let url = URL(string: urlString) else {
        print("Invalid URL")
        completion(nil)
        return
    }
    
    let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
        guard let data = data, error == nil else {
            print("Error fetching data: \(error?.localizedDescription ?? "Unknown error")")
            completion(nil)
            return
        }
        
        do {
            let decoder = JSONDecoder()
            // Распарсивание данных в массив объектов Movie
            let movies = try decoder.decode([Movie].self, from: data)
            completion(movies)
        } catch {
            print("Error decoding JSON: \(error.localizedDescription)")
            completion(nil)
        }
    }
    
    task.resume()
}

// Пример использования функции
fetchMovies { (movies) in
    if let movies = movies {
        for movie in movies {
            print("Title: \(movie.title), Release Date: \(movie.releaseDate)")
        }
    } else {
        print("Failed to fetch movies")
    }
}

