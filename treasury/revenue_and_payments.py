from typing import Dict, List

from treasury.session import FederalTreasurySession


class RevenueAndPayments:
    """
    ## Overview:
    ----

    Revenue:
    Daily overview of federal revenue collections such as income tax
    deposits, customs dutities, fees for government services, fines, and
    loan repayments.

    Payments:

    Listing of payments made through the Judgment Fund including the
    amount paid out, judgement type, legal representatives, agency,
    and association cost.
    """

    def __init__(self, session: FederalTreasurySession) -> None:
        """Initalizes the `RevenueAndPayments` object.

        ### Parameters
        ----
        session: `TreasurySession`
            An initialized session of the `TreasurySession`.

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> revenue_and_payments_service = treasury_client.revenue_and_payments()
        """

        self.treasury_session: FederalTreasurySession = session

    def __repr__(self) -> str:
        """String representation of the `FederalTreasuryClient.RevenueAndPayments` object."""

        str_representation = (
            "<FederalTreasuryClient.RevenueAndPayments (active=True, connected=True)>"
        )

        return str_representation

    def judgement_fund_congress(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100,
    ) -> Dict:

        if fields:
            fields = ",".join(fields)

        if filters:
            filters = ",".join(filters)

        if sort:
            sort = ",".join(sort)

        content = self.treasury_session.make_request(
            method="get",
            endpoint="/v2/payments/jfics/jfics_congress_report",
            params={
                "format": "json",
                "page[number]": page_number,
                "page[size]": page_size,
                "fields": fields,
                "sort": sort,
                "filters": filters,
            },
        )

        return content

    def revenue_collection(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100,
    ) -> Dict:

        if fields:
            fields = ",".join(fields)

        if filters:
            filters = ",".join(filters)

        if sort:
            sort = ",".join(sort)

        content = self.treasury_session.make_request(
            method="get",
            endpoint="/v2/revenue/rcm",
            params={
                "format": "json",
                "page[number]": page_number,
                "page[size]": page_size,
                "fields": fields,
                "sort": sort,
                "filters": filters,
            },
        )

        return content
