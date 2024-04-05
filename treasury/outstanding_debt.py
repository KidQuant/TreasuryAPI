from typing import Dict, List

from treasury.session import FederalTreasurySession


class OutstandingDebtInstruments:

    def __init__(self, session: FederalTreasurySession) -> None:

        self.treasury_session: FederalTreasurySession = session

    def __repr__(self) -> str:
        """string representation of the `FederalTreasuryClient.OutstandingDebtInstruments` object."""

        # define the string representation
        str_representation = "<FederalTreasuryClient.OutstandingDebtInstruments (active=True, connected=True)>"

        return str_representation

    def rates_of_exchange(
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
            endpoint="/v1/accounting/od/rates_of_exchange",
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

    def mature_unredeemed_debt(
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
            endpoint="/v1/accounting/od/saving_bonds_mud",
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

    def piece_information_by_series(
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
            endpoint="/v1/accounting/od/savings_bonds_pcs",
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

    def saving_bonds_report(
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
            endpoint="/v1/accounting/od/saving_bonds_report",
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

    def federal_debt_by_month(
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
            endpoint="/v1/accounting/od/schedule_fed_debt",
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

    def federal_debt_fiscal_ytd(
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
            endpoint="/v1/accounting/od/schedules_fed_debt_fytd",
            params={
                "format": "json",
            },
        )

        return content

    def saving_bond_securities(
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
            endpoint="/v1/accounting/od/slgs_savings_bonds",
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

    def state_and_local_gov_securities(
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
            endpoint="/v1/accounting/od/slgs_securities",
            param={
                "format": "json",
                "page[number]": page_size,
                "page[size]": page_size,
                "fields": fields,
                "sort": sort,
                "filters": filters,
            },
        )

        return content
