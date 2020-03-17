# Beancount RateSetter UK CSV Importer
Convert [RateSetter UK](https://www.ratesetter.com/) CSV transaction history into [Beancount](http://furius.ca/beancount/) plain text accounting format

## Introduction
This Beancount importer can be used to process the CSV transaction files from RateSetter. It supports both Everyday and ISA accounts.

### Assumptions
The underlying assumption is that you will want to import RateSetter transactions into a Brokerage account. 

For instance I use `Assets:Investments:RateSetter:Brokerage`.

From there all transactions will either
- Fund the brokerage account,
- Lend money out as a new Loan,
- Return money as a capital repayment or
- Return money as an interest payment

### Conveniences
While it is generally preferable to review and match the legs of every transaction after importing, this is very tedious as all RateSetter transactions fall into one of the four types listed above. 

Also capital repayments are generally loaned out again, making the number of transactions in a typical account very large. 

This importer automates this process for you putting all loans, loan repayments and loan interest payment into accounts of your choosing.

## Set up

Set up is quite easy and all it requires is for the appropriate account names to be chosen and passed into the importer constructor in your bean-extract config file.

	CONFIG = [
             RateSetterCSVImporter('Assets:Investments:RateSetter:Brokerage',
                                   'Assets:Investments:RateSetter:Loans',
                                   'Income:Investments:Taxable:RateSetter',
                                   'LenderTransactions.csv')
	]
