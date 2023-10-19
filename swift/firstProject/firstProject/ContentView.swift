//
//  ContentView.swift
//  firstProject
//
//  Created by Игорь Крысин on 30.09.2023.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack (alignment: .leading) {
            Text("Welcome to")
                .font(.system(size: 40)).fontWeight(.heavy)
            Text("Swift Pizza")
                .fontWeight(/*@START_MENU_TOKEN@*/.bold/*@END_MENU_TOKEN@*/)
                .font(.title)
                .foregroundColor(.blue)
            Spacer()
            VStack (alignment: .leading, spacing: 24){
                HStack (alignment: .top, spacing: 20) {
                    Image(systemName: "bag").resizable()
                        .frame(width: 40, height: 40)
                        .foregroundColor(Color(UIColor.systemBlue).opacity(0.8))
                    VStack (alignment: .leading, spacing:  4){
                        Text("Order Everything").font(.headline).bold()
                        Text("Our whole menu is available in the app")
                            .font(.subheadline)
                    }
                }
                HStack (alignment: .top, spacing: 20) {
                    Image(systemName: "bag").resizable()
                        .frame(width: 40, height: 40)
                        .foregroundColor(Color(UIColor.systemBlue).opacity(0.8))
                    VStack (alignment: .leading, spacing:  4){
                        Text("Order Everything").font(.headline).bold()
                        Text("Our whole menu is available in the app")
                            .font(.subheadline)
                    }
                }
                HStack (alignment: .top, spacing: 20) {
                    Image(systemName: "bag").resizable()
                        .frame(width: 40, height: 40)
                        .foregroundColor(Color(UIColor.systemBlue).opacity(0.8))
                    VStack (alignment: .leading, spacing:  4){
                        Text("Order Everything").font(.headline).bold()
                        Text("Our whole menu is available in the app")
                            .font(.subheadline)
                    }
                }
                
            }
            Spacer()
            Button(action: {}){
                Text("Button").foregroundColor(.white).bold()
                }.frame(width: 350, height: 60)
                .background(Color(UIColor.systemBlue))
                .opacity(0.8).cornerRadius(12)
            

        }.padding(.all, 40)
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
