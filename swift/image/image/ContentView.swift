//
//  ContentView.swift
//  image
//
//  Created by Игорь Крысин on 21.10.2023.
//

import SwiftUI

struct ContentView: View {
    var imageURL = URL(string: "https://cataas.com//cat?type=square")
    var body: some View {
        VStack {
            AsyncImage(url: imageURL) { phase in
                switch phase {
                case .empty:
                    ProgressView("Like this")
                case .success(let image):
                    image
                        .resizable()
                        .frame(width: 300, height: 300)
                case .failure:
                    Image(systemName: "shippingbox")
                default:
                    EmptyView()
                }
           
            }
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
