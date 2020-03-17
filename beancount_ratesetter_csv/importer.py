from beancount.core.data import create_simple_posting
from beancount.ingest.importers import csv
from beancount.ingest.importers.csv import Col


class RateSetterCsvImporter(csv.Importer):

    def __init__(self, brokerage_account, loans_account, interest_account, currency, file_pattern):
        super().__init__({Col.DATE: 'Date', Col.NARRATION1: 'Market', Col.NARRATION2: 'Type', Col.NARRATION3: 'Item',
                          Col.AMOUNT: 'Amount'}, brokerage_account, currency, None,
                         dateutil_kwds={'dayfirst': True}, matchers=[('filename', file_pattern)])
        self._mapping = {"Monthly repayment": loans_account,
                         "Lend order": loans_account,
                         "Repaid loan capital": loans_account,
                         "Repaid loan interest": interest_account,
                         "Interest": interest_account}

    def extract(self, file, existing_entries=None):
        return [self._add_posting(transaction) for transaction in super().extract(file, existing_entries)]

    def _add_posting(self, transaction):
        split = transaction.narration.split(';')
        if len(split) >= 2:
            transaction_type = split[1].strip()
            create_simple_posting(transaction, self._mapping[transaction_type], None, self.currency)
        return transaction
