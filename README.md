# Beancount RateSetter UK CSV Importer
Convert [RateSetter UK](https://www.ratesetter.com/) CSV transaction history into [beancount](http://furius.ca/beancount/) plain text accounting format

## Introduction
This beancount importer can be used to process the CSV transaction files as downloaded from RateSetters site. It supports both Everyday and ISA accounts

### Assumptions
The underlying assumption is that you will want to import RateSetter transactions into a Brokerage account. 

For instance I use `Assets:Investments:RateSetter:Brokerage`.

From there all transactions will either
- Fund the brokerage account,
- Lend money out as a new Loan,
- Return money as a capital repayment or
- Return money as an interest repayment
