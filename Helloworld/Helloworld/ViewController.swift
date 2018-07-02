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
    
    
    }
    
    @IBAction func showMessage(sender: UIButton) {
        var EmojiDict = ["Smile": "（≧∇≦）",
                         "hi"   : "( ´ ▽ ` )ﾉ",
                         "Cry"  : "ಥ_ಥ"]
        let selectButton = sender
        if let wordToLookup = selectedButton.tittle.titleLabel?.text {
            if wordToLookup == "Smile" {
                
            }
        let alertController = UIAlertController(title: "welcome", message: "Hello!", preferredStyle: .alert)
        alertController.addAction(UIAlertAction(title: "OK!", style: .default, handler: nil))
        present(alertController, animated: true, completion: nil)
        
    }
    
    
}
