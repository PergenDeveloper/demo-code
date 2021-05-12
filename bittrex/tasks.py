from __future__ import absolute_import, unicode_literals
from celery import shared_task

from bittrex.models import BTCSummary

from bittrex.clients import Bittrex

client = Bittrex()


@shared_task(name='load_data_from_api')
def load_data_from_api():
    data = client.get_btc_summary()
    if data:
        # Save data to database
        BTCSummary.objects.create(
            symbol=data['symbol'],
            high=float(data['high']),
            low=float(data['low']),
            volume=float(data['volume']),
            quote_volume=float(data['quoteVolume']),
            percent_change=float(data['percentChange']),
            updated_at=data['updatedAt'],
        )

