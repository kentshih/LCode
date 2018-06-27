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

    @IBAction func showMessage(sender: UIButton) {
        let alertController = UIAlertController(title: "Welcome!", message: "Hello World!", preferredStyle: <#T##UIAlertControllerStyle#>)
        alertController.addAction(UIAlertAction(title: <#T##String?#>, style: <#T##UIAlertActionStyle#>, handler: <#T##((UIAlertAction) -> Void)?##((UIAlertAction) -> Void)?##(UIAlertAction) -> Void#>))
        present(alertController, animated: true, completion: nil)
    }

}

