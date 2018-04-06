from l5_functions.my_first_package import card_has_errors,cvv_check,region_check,expiry_check,print_bank

card_check_test = card_has_errors('')
expiry_check_test = expiry_check('')
cvv_check_test = cvv_check('')
bank_check_test = print_bank(card_check_test)
region_check_test = region_check(card_check_test)