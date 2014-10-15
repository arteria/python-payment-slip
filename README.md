# python-payment-slip

Function for generating ISR-numbers for Orange inpayment slip (ISR), so called "Oranger Einzahlungsschein" (ESR/ESR+).

 


## Usage

	import payment_slip.esr as esr
	print esr.generateCodeline("01", "4378", "85", ">", "94476300000000128001105152", "+", "01200027", ">")
	
	
## More info

* PostFinace [Orange inpayment slip](https://www.postfinance.ch/en/biz/prod/pay/debsolution/inpayref/detail.html) detals
