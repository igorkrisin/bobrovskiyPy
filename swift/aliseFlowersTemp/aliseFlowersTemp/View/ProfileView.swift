//
//  ProfileView.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 22.10.2023.
//

import SwiftUI

struct ProfileView: View {
    
    @State var isAvaAletrPresented = false
    @State var isQuitAlertPresent = false
    @State var isAuthViewPresented = false
    
    var body: some View {
        VStack (alignment: .center, spacing: 20){
            HStack (spacing: 20) {
                Image(systemName: "person.fill")
                    .resizable()
                    .frame(width: 80, height: 80)
                    .foregroundColor(Color("Mygray"))
                    .background(Color.gray)
                    .clipShape(Circle())
                    .onTapGesture {
                        isAvaAletrPresented.toggle()
                    }
                    .confirmationDialog("Откуда взять фото ", isPresented: $isAvaAletrPresented) {
                        Button {
                            print("Library")
                        } label: {
                            Text("Из галереи")
                        }
                        Button {
                            print("Camera")
                        } label: {
                            Text("С камеры")
                        }
                    }
                VStack (alignment: .leading, spacing: 12) {
                    Text("Igor Krysin Vasilevich")
                        .bold()
                    Text("+7 9992123434")
                }
                Spacer()
            }.padding()
                .padding(.horizontal, 6)
            
            VStack (alignment: .leading, spacing: 8) {
                Text("Адрес доставки: ")
                    .bold()
                
                Text("Cанкт-Петербург, Малый проспект ВО, 34)")
            }
            
            
            
            List {
                Text("Ваши заказы будут тут: ")
                    .padding(.horizontal,6)
            }.listStyle(.plain)
            
            Button{
                isQuitAlertPresent.toggle()
            } label: {
                Text("Quit")
                    .padding()
                    .padding(.horizontal, 30)
                    .background(Color.red)
                    .foregroundColor(.white)
                    .cornerRadius(20)
            }.padding()
                .confirmationDialog("Хотите выйти?}", isPresented: $isQuitAlertPresent) {
                    Button {
                        isAuthViewPresented.toggle()
                    } label: {
                        Text("Да")
                    }
                    
                }
                .fullScreenCover(isPresented: $isAuthViewPresented, onDismiss: nil) {
                    AuthView()
                }
        }
        
    }
}

#Preview {
    ProfileView()
}
