python-payment-slip
===================

Function for generating ESR-numbers for orange swiss payment slips (so called "Oranger Einzahlungsschein").


Usage
-----

	import payment_slip.esr as esr
	print esr.generateCodeline("01", "4378", "85", ">", "94476300000000128001105152", "+", "01200027", ">")
	
	
	