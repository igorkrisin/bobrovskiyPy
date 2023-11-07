//
//  ContentView.swift
//  aliseFlowersTemp
//
//  Created by Игорь Крысин on 21.10.2023.
//

import SwiftUI

struct AuthView: View {
    @State private var isAuth = true
    
    
    @State private var email = ""
    @State private var password = ""
    @State private var confirmPassword = ""
    
    @State private var isTabViewShow = false
    @State private var isShowAlert = false
    @State private var alertMessage = ""
    
    var body: some View {
        
        VStack(spacing: 30) {
            
            Text(isAuth ? "Авторизация" : "Регистрация")
                .padding()
                .padding(.horizontal, 30)
                .font(.title2.bold())
                .background(Color(isAuth ? "ForAuthoriz" : "Mypink"))
                .cornerRadius(30)
                .foregroundColor(isAuth ? Color("Mygray") : Color(.white))
            VStack {
                TextField("Введите логин", text: $email)
                    .padding()
                    .background(Color("ForAuthoriz"))
                    .cornerRadius(12)
                    .padding(8)
                    .padding(.horizontal, 12)
                SecureField("Введите пароль", text: $password)
                    .padding()
                    .background(Color("ForAuthoriz"))
                    .cornerRadius(12)
                    .padding(8)
                    .padding(.horizontal, 12)
                
                if !isAuth {
                    SecureField("Повторите пароль", text: $confirmPassword)
                        .padding()
                        .background(Color("ForAuthoriz"))
                        .cornerRadius(12)
                        .padding(8)
                        .padding(.horizontal, 12)
                }
                Button(isAuth ? "Войти" : "Зарегистрироваться")
                {
                    if isAuth {
                        print("Войти через FireBase")
                        
                        AuthService.shared.signIn(email: email, 
                                                  password: password) { result in
                            switch result {
                                
                            case .success(_):
                                isTabViewShow.toggle()
                            case .failure(let error):
                                alertMessage = "Ошибка авторизации \(error.localizedDescription)"
                                isShowAlert.toggle()
                            }
                        }
                    } else {
                        print("Зарегистрироваться")
                        guard password == confirmPassword else {
                            self.alertMessage = "Пароли не совпадают"
                            self.isShowAlert.toggle()
                            return
                        }
                                
                                
                        AuthService.shared.singUp(email: self.email, password: self.password) { result in
                            switch result {
                                
                            case .success(let user):
                                alertMessage = " Вы зарегестрировались с email \(user.email!)"
                                self.isShowAlert.toggle()
                                self.email = ""
                                self.password = ""
                                self.confirmPassword = ""
                                self.isAuth.toggle()
                            case .failure(let error):
                                alertMessage = " ошибка регистрации \(error.localizedDescription)!"
                                self.isShowAlert.toggle()
                            }
                        }
                        
                       
                    }
                }
                    .padding()
                    .frame(maxWidth: .infinity)
                    .background(Color("Mygray"))
                    .cornerRadius(12)
                    .padding(8)
                    .padding(.horizontal, 12)
                    .font(.title3.bold())
                    .foregroundColor(.white)
                
                Button(isAuth ? "Присоединяйся" : "Уже зарегистрирован")
                {
                    isAuth.toggle()
                }
                    .padding()
                    .frame(maxWidth: .infinity)
                    //.border(Color("Mygray"), width: 4.0)
                    .background(Color("grayOpac30"))
                    .cornerRadius(12)
                    .padding(8)
                    .padding(.horizontal, 12)
                    .font(.title3.bold())
                    .foregroundColor(.white)
                
                
            }
            .padding()
            .padding(.top, 12)
            .padding(.bottom, 12)
            .background(Color("ForAuthoriz"))
            .cornerRadius(24)
            .padding(isAuth ? 30 : 12)
            .alert(alertMessage,
                   isPresented: $isShowAlert) {
                Button { } label: {
                    Text("OK")
                }
            }
    
        }.frame(maxWidth: /*@START_MENU_TOKEN@*/.infinity/*@END_MENU_TOKEN@*/, maxHeight: .infinity)
            .background(Image("bg")
                .aspectRatio(contentMode: .fit)
                .ignoresSafeArea()
                .blur(radius: isAuth ? 0 : 6)
            )
            .animation(Animation.easeInOut(duration: 0.5), value: isAuth)
            .fullScreenCover(isPresented: $isTabViewShow) {
                
                let mainTabBarViewModel = MainTabBarViewModel(user: AuthService.shared.currentUser!)
                
                MainTabBar(viewModel: mainTabBarViewModel)
            }
        
    }
}

#Preview {
    AuthView()
}
