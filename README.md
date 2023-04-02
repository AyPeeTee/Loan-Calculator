<h1 align="center"><strong><em>Loan Calculator</strong></em></h1>
<p align="center"><img src="demo/logo.png" alt="bot-logo" height=350 width=375></p>

# About the project
<p>The third project that I made in Python.</p>
<p>I made this project by following the <a href=https://hyperskill.org/tracks>JetBrains Academy</a> course.</p> 
 
# How to start the programm?
* To start the programm you need to have installed Python. [**Download**](https://www.python.org/downloads/)
* You need to introduce the start arguments. The main argument is **--type**.

## **In case **--type=diff**, you need to pass 3 more arguments:**
  
| --type=diff |
|-------------|
| --principal=NUM |
| --periods=NUM   |
| --interest=NUM  |

### Usage example

```
> python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
Month 1: payment is 65750
Month 2: payment is 65344
Month 3: payment is 64938
Month 4: payment is 64532
Month 5: payment is 64125
Month 6: payment is 63719
Month 7: payment is 63313
Month 8: payment is 62907

Overpayment = 14628
```

---------------------------------

## **In case **--type=annuity**, instend of **--periods** you need to pass **--payment**:**

| --type=annuity  |
|-----------------|
| --principal=NUM |
| --payment=NUM   |
| --interest=NUM  |

### Usage example

```
> python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your loan principal = 800018!
Overpayment = 246622
```
