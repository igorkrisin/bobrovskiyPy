//
//  ViewController.swift
//  MyCalculator
//
//  Created by Игорь Крысин on 20.12.2023.
//

import UIKit

class ViewController: UIViewController {

    
    let regex = #"^[^\d.]*$"#
    var firstNumber: String = ""
    var secondNumber: String = ""
    var summaryNumber: String = ""
    var mathSing: String = ""
    
    
    
    
    var isOperationDuring = false
    
    var isDotPushed = false
    var calcTapped = false
    var mathSingTapped = false
    var isEqualTapped = false
    var isFirstTapped = false
    var minusValue: Bool = false
    
    
    @IBOutlet weak var resultLabel: UILabel!
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        isFirstTapped = false
        
    }
    
    
    
    @IBAction func mathOperation(_ sender: Any) {
        if (sender as AnyObject).tag == 11 {
            mathSing = "/"
        } else if (sender as AnyObject).tag == 12 {
            mathSing = "*"
        } else if (sender as AnyObject).tag == 13 {
            mathSing = "-"
        } else if (sender as AnyObject).tag == 14 {
            mathSing = "+"
        }
        showCalculatorScreen(mathSing)
        mathSingTapped = true
        minusValue = false
    }
    
    
    @IBAction func minusOrPlus(_ sender: Any) {
       assignValueToNumber("+/-")
        if !minusValue && !isMathSing(resultLabel.text!) {
            resultLabel.text! = "-" + resultLabel.text!
            minusValue = true
        } else if minusValue && resultLabel.text!.contains("-") {
            resultLabel.text!.removeFirst()
            minusValue = false
        }
        
    }
    

    @IBAction func percent(_ sender: Any) {
        print("ScecondNumbPErcent: ", secondNumber)
        if mathSing == "+" || mathSing == "-" {
            secondNumber = String((Double(secondNumber)! * 0.01) * Double(firstNumber)!)
        } else if mathSing == "*" || mathSing == "/" {
            secondNumber = String(Double(secondNumber)! * 0.01)
        }
        
        print("ScecondNumbPErcent: ", secondNumber)
    }
    
    
    @IBAction func equal(_ sender: Any) {
        
        isEqualTapped = true
        mathSingTapped = false
        calc()
    }
    
    
    @IBAction func digitButtonAction(_ sender: Any) {
        showCalculatorScreen(String((sender as AnyObject).tag))
        assignValueToNumber(String((sender as AnyObject).tag))
    }
    
    
    @IBAction func dot(_ sender: Any) {
        showCalculatorScreen(".")
        assignValueToNumber(".")
    }
    
    @IBAction func reset(_ sender: Any) {
        secondNumber = ""
        firstNumber = ""
        mathSing = ""
        resultLabel.text! = "0"
        summaryNumber = ""
        
    }
    
    
    func showCalculatorScreen(_ value: String) {

        if isMathSing(value) && value != "." && value != "%" {
            
            print("is math sing")
            resultLabel.text! = ""
            resultLabel.text! = value
            
        } else if (!isFirstTapped) { // первое нажатие удаляем первый 0
            print("first")
            
                resultLabel.text! = ""
            
            resultLabel.text! = value
            isFirstTapped = true
            isOperationDuring = true
            
        } else if isEqualTapped { // показывем результат при нажати на равно
            print("equal tapped")
            resultLabel.text! = ""
            resultLabel.text! = value
            isEqualTapped = false
            isOperationDuring = false // операция окончена
            isFirstTapped = false //первое нажатие в режиме ожидания
            resetValue()
        } else if value == "%" {
            print("%")
            calc()
        } else if value == "." && !resultLabel.text!.contains(".") {
            resultLabel.text! += value
        } else {
            print("else")
            if isMathSing(resultLabel.text!) && secondNumber.count == 0 { //если после знака вводим число - знак надо удалить
                print("если после знака вводим число ", isMathSing(resultLabel.text!) )
                    resultLabel.text! = ""
            }
            print(" resultLabel.text! += value")
            resultLabel.text! += value
        }
    }
    
    
    func assignValueToNumber(_ value: String) {
        print("value assing: ", value)
        
        if !mathSingTapped {
            if value == ("+/-") {
                firstNumber = "-" + firstNumber
            } else {
                firstNumber += value
            }
        } else if !isMathSing(resultLabel.text!) { // что бы при выведении знака на табло невозможно было поставить - перед знаком
            if value == ("+/-") {
                secondNumber = "-" + secondNumber
            } else {
                secondNumber += value
            }
        }
    }
    
    
    func isMathSing (_ value: String) -> Bool {
        let regex = #"^[^\d]*$"#
        let isMatch = value.range(of: regex, options: .regularExpression) != nil
        return isMatch
    }
    
    //make math operation
    
    
    func calc(){
        print("secondNumber: ", secondNumber)
        print("firstNumber: ", firstNumber)
        if firstNumber != "" && secondNumber != "" {
            
            switch mathSing {
            case "/":
                if secondNumber == "0" {
                    resultLabel.text! = "ERROR"
                    return
                }
                if hasDotInSring() { // если число с точкой конвертируем во float
                    summaryNumber = String((Float(firstNumber))! / (Float(secondNumber))!)
                } else { // если нет то в Int
                    summaryNumber = String((Int(firstNumber))! / (Int(secondNumber))!)
                }
                showCalculatorScreen(summaryNumber)
            case "*":
                if hasDotInSring() {
                    summaryNumber = String((Float(firstNumber))! * (Float(secondNumber))!)
                } else {
                    summaryNumber = String((Int(firstNumber))! * (Int(secondNumber))!)
                }
                showCalculatorScreen(summaryNumber)
            case "-":
                if hasDotInSring() {
                    summaryNumber = String((Float(firstNumber))! - (Float(secondNumber))!)
                } else {
                    summaryNumber = String((Int(firstNumber))! - (Int(secondNumber))!)
                }
                showCalculatorScreen(summaryNumber)
            case "+":
                if hasDotInSring() {
                    summaryNumber = String((Float(firstNumber))! + (Float(secondNumber))!)
                } else {
                    summaryNumber = String((Int(firstNumber))! + (Int(secondNumber))!)
                }
                showCalculatorScreen(summaryNumber)
            
                
            default:
                break
            }
        }
    }
    
    func doMathOperations<T: FloatingPoint>(_ firstNumber: T, _  secondNumber: T, _ mathSing: String) -> T? {
        if mathSing ==  "-" { return firstNumber - secondNumber }
        else if mathSing ==  "*" { return firstNumber * secondNumber }
        else if mathSing ==  "+" { return firstNumber + secondNumber }
        guard secondNumber != 0 else {
            resultLabel.text! = "Err"
            return nil
        }
        return firstNumber / secondNumber
    }
    


    func hasDotInSring() -> Bool { //есть ли точка в числах?
        return firstNumber.contains(".") || secondNumber.contains(".")
            
    }
    
    func resetValue (){
        secondNumber = ""
        firstNumber = ""
        mathSing = ""
    }
    
    
    
    
//    if(resultLabel.text!.count < 10) {
//        if  resultLabel.text! == "0" && !isOperationDuring && !isDotPushed {
//            resultLabel.text! = ""
//        }
//        if isMathSing(resultLabel.text!) { // если на экране математический знак - удалить перед вводом цифр
//            resultLabel.text! = ""
//        }
//        if calcTapped && !isMathSing(resultLabel.text!) && resultLabel.text?.count != 0 { //  если нажато равно и на экране не матем.  знак, то очищаем экран что бы
//            resultLabel.text! = ""
//           
//            calcTapped = false
//            
//        }
//        
//        
//        
//        if  !isOperationDuring {
//            print(1)
//            resultLabel.text! += value
//            firstNumber += value
//        } else if (isOperationDuring && !isMathSing(value)) {
//            print(2)
//            resultLabel.text! += value
//            secondNumber += value
//        } else if (isOperationDuring && isMathSing(value) && calcTapped) {
//            print("during")
//            mathSing = value
//            resultLabel.text! = value
//        }
//        else {
//            resultLabel.text! = ""
//        }
//    }
//    
    
    
//    //числа кнопки
//    @IBOutlet weak var one: UIButton!
//    @IBOutlet weak var two: UIButton!
//    @IBOutlet weak var three: UIButton!
//    
//    @IBOutlet weak var seven: UIButton!
//    
//    
//    override func viewDidLoad() {
//        super.viewDidLoad()
//       
//        
//    }
//    
//    
//    
//    @IBAction func addOne(_ sender: Any) {
//        if resultLabel.text! == "0" {
//            resultLabel.text! = ""
//        }
//        resultLabel.text! += "1"
//       
//    }
//    
//    @IBAction func dividing(_ sender: Any) {
//        mathSing = "/"
//        calc()
//    }
//    
//    
//    
//    
//    
//    
//    @IBAction func equal(_ sender: Any) {
//        calc()
//    }
//    
//    
//    @IBAction func resetValue(_ sender: Any) {
//        resetBothNumber()
//    }
//    
//    //калькулирование - основная функция
//
//    func calc() {
//        print("calc!")
//        addValueInNUmbers()
//        if !isSecondNumberEmpty() {
//            print("mathSing: ", mathSing)
//            switch mathSing {
//            case "/":
//                resultLabel.text! = String(Float(firstNumber)! / (Float(secondNumber) ?? 100.0) ) // MARK: убрать этот костыль с опционалом!!!
//                    
//                continueCalculation()
//                
//                
//            default:
//                print("press unknown button")
//            }
//        }
//    }
//    
//    //хранимые свойство первого  числа пустое?
//    
//    func isSecondNumberEmpty() -> Bool {
//        if secondNumber == "" {
//            return true
//        }
//        return false
//        
//    }
//    
//    func addValueInNUmbers() {
//        if firstNumber == "" {
//            firstNumber = resultLabel.text!
//            resultLabel.text! = ""
//            print("first: ", firstNumber)
//        } else if isSecondNumberEmpty() {
//            secondNumber = resultLabel.text!
//            resultLabel.text! = ""
//            print("sec: ", secondNumber)
//            print("false")
//        }
//    }
//    
//    func resetBothNumber() {
//        resultLabel.text = "0"
//        firstNumber = ""
//        secondNumber = ""
//    }
//    
//    
//    // продолжение калькуляции, если не нажат знак =
//    func continueCalculation(){
//        firstNumber = resultLabel.text!
//        
//        secondNumber = ""
//        print("secondNumb: ", secondNumber)
//    }
//    

}

