# Beancount Importer for RateSetter UK CSVs
Convert [RateSetter UK](https://www.ratesetter.com/) CSV transaction history into [Beancount](http://furius.ca/beancount/) plain text accounting format.

## Introduction
This Beancount importer can be used to process the CSV transaction files from RateSetter. It supports both Everyday and ISA accounts.

### Assumptions
The underlying assumption is that you will want to import RateSetter transactions into a Brokerage account. 

For instance I use `Assets:Investments:RateSetter:Brokerage`.

From there all transactions will either:
- Fund or withdraw funds from the brokerage account,
- Lend money out as a new loan,
- Return money as a capital repayment or
- Earn money as an interest payment

### Conveniences
While it is generally preferable to review and match the legs of every transaction after importing, this is very tedious as all RateSetter transactions fall into one of the four types listed above. 

Also capital repayments are generally loaned out again, making the number of transactions in a typical account very large. 

This importer automates this process for you by putting all the loan, loan repayment and loan interest payment transactions into accounts of your choosing.

### Balance Assertions
Unfortunately the CSV transaction file from RateSetter does not contain any balance information so automatic balance assertions can not be added by the importer. 

## Set up
Set up is quite easy and all it requires is for the appropriate account names to be chosen and passed into the importer constructor in your bean-extract config file.

    from beancount_ratesetter_csv import RateSetterCSVImporter
     
	CONFIG = [
             RateSetterCSVImporter('Assets:Investments:RateSetter:Brokerage', # Brokerage Account
                                   'Assets:Investments:RateSetter:Loans',     # Loans Account
                                   'Income:Investments:Taxable:RateSetter',   # Interest Account
                                   'GBP',                                     # Currency String
                                   'LenderTransactions.csv')                  # Filename Regular Expression
	]
