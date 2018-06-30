//
//  ViewController.swift
//  Helloworld
//
//  Created by Shih on 2018/6/26.
//  Copyright © 2018年 Shih. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    let fullScreenSize = UIScreen.main.bounds.size
    
    var myButton = UIButton(type: .contactAdd)
    myButton.center = CGPoint(
    x: fullScreenSize.width * 0.4,
    y: fullScreenSize.height * 0.2)
    self.view.addSubview(myButton)
    
}
